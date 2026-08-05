class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1

        sort_ele=sorted(freq.keys(),key=freq.get,reverse=True)
        return sort_ele[:k]
            
        