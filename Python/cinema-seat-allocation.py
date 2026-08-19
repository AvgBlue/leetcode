from typing import List


class Solution:
    def max_groups_for_row_mask(self, num_mask: int) -> int:
        

        allow_sit_mask={0b_011_1111_110:2,0b_000_1111_000:1,0b_000_0011_110:1,0b_011_1100_000:1}
        for mask in allow_sit_mask:
            if (~num_mask)&mask==mask:
                return allow_sit_mask[mask]
        return 0
        # result=0    
        #run=0
        # for bit_index in range(10):
        #     bit = 1 << bit_index

        #     if not num_mask & bit:
        #         run+=1
        #     else:
        #         run=0
        #         continue
        #     if run==4:
        #         result+=1
        #         run=0 
        # return result
    
    masks={0: 2, 1: 2, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1, 11: 1, 12: 1, 13: 1, 14: 1, 15: 1, 16: 1, 17: 1, 18: 1, 19: 1, 20: 1, 21: 1, 22: 1, 23: 1, 24: 1, 25: 1, 26: 1, 27: 1, 28: 1, 29: 1, 30: 1, 31: 1, 32: 1, 33: 1, 64: 1, 65: 1,96: 1, 97: 1, 128: 1, 129: 1, 130: 1, 131: 1, 132: 1, 133: 1, 134: 1, 135: 1, 160: 1, 161: 1, 192: 1, 193: 1, 224: 1, 225: 1, 256: 1, 257: 1, 258: 1, 259: 1, 260: 1, 261: 1, 262: 1, 263: 1, 288: 1, 289: 1, 320: 1, 321: 1, 352: 1, 353: 1, 384:1, 385: 1, 386: 1, 387: 1, 388: 1, 389: 1, 390: 1, 391: 1, 416: 1, 417: 1, 448: 1, 449: 1, 480: 1, 481: 1, 512: 2, 513: 2, 514: 1, 515: 1, 516: 1, 517: 1, 518: 1, 519: 1, 520: 1, 521: 1, 522: 1, 523: 1, 524: 1, 525: 1, 526: 1, 527: 1, 528: 1,529: 1, 530: 1, 531: 1, 532: 1, 533: 1, 534: 1, 535: 1, 536: 1, 537: 1, 538: 1, 539: 1, 540: 1, 541: 1, 542: 1, 543: 1, 544: 1, 545: 1, 576: 1, 577: 1, 608: 1, 609: 1, 640: 1, 641: 1, 642: 1, 643: 1, 644: 1, 645: 1, 646: 1, 647: 1, 672: 1, 673: 1, 704: 1, 705: 1, 736: 1, 737: 1, 768: 1, 769: 1, 770: 1, 771: 1, 772: 1, 773: 1, 774: 1, 775: 1, 800: 1, 801: 1, 832: 1, 833: 1, 864: 1, 865: 1, 896: 1, 897:1, 898: 1, 899: 1, 900: 1, 901: 1, 902: 1, 903: 1, 928: 1, 929: 1, 960: 1, 961: 1, 992: 1, 993: 1}
    def maxNumberOfFamilies(
        self, n: int, reservedSeats: List[List[int]]
    ) -> int:
        row_masks={}
        for reserve in reservedSeats:
            row_masks[reserve[0]]=row_masks.get(reserve[0],0)| (1<<(reserve[1]-1))
        sum=0
        for mask in row_masks.values():
            sum+=self.masks.get(mask,0)

        result=2*(n-len(row_masks))+sum
        return result


if __name__ == "__main__":
    solution = Solution()

    examples = [
        (3, [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]], 4),
        (2, [[2, 1], [1, 8], [2, 6]], 2),
        (4, [[4, 3], [1, 4], [4, 6], [1, 7]], 4),
    ]
    dic_result={}
    for i in range(2**10):
        result=solution.max_groups_for_row_mask(i)
        if result>=1:
            solution.masks[i]=result
    for n, reserved_seats, expected in examples:
        result = solution.maxNumberOfFamilies(n, reserved_seats)
        print(f"Expected: {expected} | Result: {result}")

    
