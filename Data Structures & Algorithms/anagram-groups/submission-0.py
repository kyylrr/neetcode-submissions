from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        answer =[]

        for letters in strs:
            ordered = tuple(sorted(letters))
            anagram_map[ordered].append(letters)
        for value in anagram_map.values():
            answer.append(value)
        return answer
        