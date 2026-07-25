class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = defaultdict(list)
        answer = []

        for words in strs:
            key = tuple(sorted(words))
            mapped[key].append(words)
        for final in mapped.values():
            answer.append(final)
        return answer