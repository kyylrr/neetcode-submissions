from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        answer =[]
        for num in nums:
            freq[num] +=1
        sorted_list = sorted(freq.items(), key=lambda number: number[1], reverse = True)
        for i in range(k):
            answer.append(sorted_list[i][0])
        return answer