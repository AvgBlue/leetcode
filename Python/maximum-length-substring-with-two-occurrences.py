class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        len_s=len(s)
        if len_s==2:
            return 2
        result=2
        freq={}

        freq[s[0]]=1
        freq[s[1]]=freq.get(s[1],0)+1

        start=0

        for i in range(2,len_s):
            c=s[i]
            freq[c]=freq.get(c,0)+1
            while freq[c]>2:
                freq[s[start]]-=1
                start+=1
            new_len=i-start+1
            if new_len>result:
                result=new_len
        return result



if __name__ == "__main__":
    solution = Solution()

    print(solution.maximumLengthSubstring("bcbbbcba")==4)
    print(solution.maximumLengthSubstring("aaaa")==2)
    print(solution.maximumLengthSubstring("bbbab")==3)

