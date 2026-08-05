class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        #sort_ele=sorted(freq.keys(),key=freq.get,reverse=True)
        #return sort_ele[:k]
        buckets=[ [] for _ in range(len(nums)+1)]
        for num,fr in freq.items():
            buckets[fr].append(num)
        
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res
        