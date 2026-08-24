class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #O(m*nlogn) solution due to sorting:
        #res=defaultdict(list)
        #for s in strs:
        #    sorted_s = "".join(sorted(s))
        #    res[sorted_s].append(s)
        #return list(res.values())
#--------------------------------------------
        #O(m*n) soln:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
            res[tuple(count)].append(s)
        return list(res.values())

        #concepts:
        #1 res[tuple(count)].append(s) converts the list count into an immutable tuple so it can serve as a dictionary key.
        #2 count[ord(c) - ord("a")] += 1 converts the character into an array index (0 for 'a', 1 for 'b', etc.) and increments its count. For example, "cat" yields a frequency list where indices for 'a', 'c', and 't' are set to 1.













