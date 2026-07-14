from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for _str in strs:
            frequencies = [0] * 26

            for _char in _str:
                _char_index = ord(_char) - 97

                frequencies[_char_index] += 1

            anagrams[bytes(frequencies)].append(_str)

        return [x for x in anagrams.values()]

        