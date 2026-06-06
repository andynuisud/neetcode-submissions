class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = [[] for _ in range(len(nums) + 1)]
        hashMap = defaultdict(int)

        for i in nums: 
            hashMap[i] += 1

        for key, value in hashMap.items():
            bucket[value].append(key)

        res = []

        for i in range(len(bucket)-1, -1, -1):

            for num in bucket[i]: 
                res.append(num)
                if len(res) == k: 
                    return res 

        return res