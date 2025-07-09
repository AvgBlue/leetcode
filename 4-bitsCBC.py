from typing import List


def toy_cipher_encrypt_block(block: List[bool], key: int) -> List[bool]:
    assert len(block) == 4
    plaintext = bits_to_int(block)
    assert 0 <= plaintext < 16
    assert 0 <= key < 16

    s_box = [
        0b1110,
        0b0100,
        0b1101,
        0b0001,
        0b0010,
        0b1111,
        0b1011,
        0b1000,
        0b0011,
        0b1010,
        0b0110,
        0b1100,
        0b0101,
        0b1001,
        0b0000,
        0b0111,
    ]

    def permute(n: int) -> int:
        b = [(n >> i) & 1 for i in reversed(range(4))]  # [b3, b2, b1, b0]
        reordered = [b[1], b[3], b[0], b[2]]
        return sum(bit << (3 - i) for i, bit in enumerate(reordered))

    xored = plaintext ^ key
    substituted = s_box[xored]
    permuted = permute(substituted)

    return int_to_bits(permuted, 4)


def toy_cipher_decrypt_block(block: List[bool], key: int) -> List[bool]:
    assert len(block) == 4
    ciphertext = bits_to_int(block)
    assert 0 <= ciphertext < 16
    assert 0 <= key < 16

    s_box = [
        0b1110,
        0b0100,
        0b1101,
        0b0001,
        0b0010,
        0b1111,
        0b1011,
        0b1000,
        0b0011,
        0b1010,
        0b0110,
        0b1100,
        0b0101,
        0b1001,
        0b0000,
        0b0111,
    ]

    inv_s_box = [0] * 16
    for i, val in enumerate(s_box):
        inv_s_box[val] = i

    def inverse_permute(n: int) -> int:
        b = [(n >> i) & 1 for i in reversed(range(4))]
        reordered = [b[2], b[0], b[3], b[1]]
        return sum(bit << (3 - i) for i, bit in enumerate(reordered))

    inv_permuted = inverse_permute(ciphertext)
    inv_substituted = inv_s_box[inv_permuted]
    decrypted = inv_substituted ^ key

    return int_to_bits(decrypted, 4)


def bits_to_int(bits: List[bool]) -> int:
    """
    Convert a list of boolean bits to an integer.
    The most significant bit is bits[0].
    """
    return sum((1 << (len(bits) - 1 - i)) if b else 0 for i, b in enumerate(bits))


def int_to_bits(n: int, width: int = 4) -> List[bool]:
    """
    Convert an integer to a list of boolean bits of given width.
    The most significant bit is at index 0.
    """
    return [(n >> i) & 1 == 1 for i in reversed(range(width))]


def chunk_bits(bits: List[bool], block_size: int = 4) -> List[List[bool]]:
    assert len(bits) % block_size == 0, "Bits length must be a multiple of block size"
    return [bits[i : i + block_size] for i in range(0, len(bits), block_size)]


def pad_bits(bits: List[bool], block_size: int = 4) -> List[bool]:
    remainder = len(bits) % block_size
    pad_len = (block_size - remainder) if remainder != 0 else 0
    padding = [False] * pad_len
    length_block = int_to_bits(pad_len, block_size)
    return bits + padding + length_block


def unpad_bits(bits: List[bool], block_size: int = 4) -> List[bool]:
    if len(bits) < block_size:
        raise ValueError("Too short to contain padding info")

    pad_info_block = bits[-block_size:]
    pad_len = bits_to_int(pad_info_block)

    if pad_len > len(bits) - block_size:
        raise ValueError("Padding too long")

    return bits[: -(block_size + pad_len)]


def xor_blocks(a: List[bool], b: List[bool]) -> List[bool]:
    assert len(a) == len(b), "Blocks must be the same length"
    return [bit_a != bit_b for bit_a, bit_b in zip(a, b)]


def toy_CBC_encrypt_bits(plaintext_bits: List[bool], key: int, iv: int) -> List[bool]:
    padded_bits = pad_bits(plaintext_bits)
    blocks = chunk_bits(padded_bits, 4)
    result: List[bool] = []

    prev_block = int_to_bits(iv, 4)
    for block in blocks:
        xored_block = xor_blocks(block, prev_block)
        cipher_block = toy_cipher_encrypt_block(xored_block, key)
        result.extend(cipher_block)
        prev_block = cipher_block

    return result


def toy_CBC_decrypt_bits(cipher_bits: List[bool], key: int, iv: int) -> List[bool]:
    blocks = chunk_bits(cipher_bits, 4)
    result: List[bool] = []

    prev_block = int_to_bits(iv, 4)
    for block in blocks:
        decrypted_block = toy_cipher_decrypt_block(block, key)
        plain_block = xor_blocks(decrypted_block, prev_block)
        result.extend(plain_block)
        prev_block = block

    return unpad_bits(result)


class PaddingOracle:
    def __init__(self, key: int, iv: int):
        self._key = key
        self._iv = iv

    def query(self, cipher_bits: List[bool]) -> bool:
        try:
            _ = toy_CBC_decrypt_bits(cipher_bits, self._key, self._iv)
            return True  # padding valid
        except ValueError:
            return False  # padding error


def PaddingOracle_attack_full_massage(
    cipher_bits: List[bool], oracle: PaddingOracle
) -> List[bool]:
    return cipher_bits


if __name__ == "__main__":

    key: int = 0x8
    iv: int = 0xE
    plaintext_bits: List[bool] = (
        int_to_bits(0xD)
        + int_to_bits(0xA)
        + int_to_bits(0x4)
        + int_to_bits(0x1)
        + [True]
    )
    print("Plaintext bits:", plaintext_bits)
    cipher_bits = toy_CBC_encrypt_bits(plaintext_bits, key, iv)
    print("Ciphertext bits:", cipher_bits)

    oracle: PaddingOracle = PaddingOracle(key, iv)

    attack_result_bits = PaddingOracle_attack_full_massage(cipher_bits, oracle)

    print("attack_result_bits:", attack_result_bits)
    assert attack_result_bits == plaintext_bits, "Decryption failed"
    print("Decryption successful")
