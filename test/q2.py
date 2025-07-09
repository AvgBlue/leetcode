# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(moves):
    if len(moves) % 2 != 0:
        return False
    count_dict = {">": 0, "<": 0, "^": 0, "v": 0}
    set_x_coordinates = set()
    set_y_coordinates = set()

    position = (0, 0)
    possible_moves = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}

    def applay_move(position, move):
        return (
            position[0] + possible_moves[move][0],
            position[1] + possible_moves[move][1],
        )

    for i, direction in enumerate(moves):
        if direction in [
            ">",
            "<",
        ]:  # when we move in the x we dont see a new y so it a time to record it
            set_x_coordinates.add(position[0])
        else:  # when we move in the y we dont see a new x so it a time to record it
            set_y_coordinates.add(position[1])
        count_dict[direction] += 1
        position = applay_move(position, direction)
        if position == (0, 0) and i != len(moves) - 1:
            return False

    is_vertical_balanced = count_dict["^"] == count_dict["v"]
    is_horizontal_balanced = count_dict[">"] == count_dict["<"]
    is_horizontal_move_present = count_dict[">"] != 0 or count_dict["<"] != 0
    is_vertical_move_present = count_dict["^"] != 0 or count_dict["v"] != 0
    is_two_x_coordinates = len(set_x_coordinates) == 2
    is_two_y_coordinates = len(set_y_coordinates) == 2
    is_back_to_origin = position == (0, 0)

    return (
        is_vertical_balanced
        and is_horizontal_balanced
        and is_horizontal_move_present
        and is_vertical_move_present
        and is_two_x_coordinates
        and is_two_y_coordinates
        and is_back_to_origin
    )


def main():
    test_cases = [
        (">>>^^^<<<vvv", True),
        ("<vvv>>^^^<", True),
        (">^<v>^<v", False),
        (">>^^<<vv", True),
        (">>>>^<<<v", False),
        (">>>>vvvv<<<<^^^^", True),
        (">v<^", True),  # goes in a small square but revisits origin too early
        ("^>v<", True),  # valid square but revisits origin at step 3
    ]

    for i, (moves, expected) in enumerate(test_cases):
        result = solution(moves)
        status = "PASS" if result == expected else "FAIL"
        print(
            f"Test case {i + 1}: {moves} → {result} (expected: {expected}) → {status}"
        )


if __name__ == "__main__":
    main()
