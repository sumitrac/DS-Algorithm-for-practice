
from collections import defaultdict


Input = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(strings):
    # returnList = []
    # dict = defaultdict(list)

    # for item in strs:
    #     key = "".join(sorted(list(item)))
    #     dict[key].append(item)

    # for i in dict.values():
    #     returnList.append(i)
    # return returnList

    anagrams_dict = {}

    for word in strings:
        word_as_list = [char for char in word]
        word_as_list.sort()
        key = tuple(word_as_list)
        if anagrams_dict.get(key):
            anagrams_dict[key].append(word)
        else:
            anagrams_dict[key] = [word]

    answer = []

    for key, value in anagrams_dict.items():
        answer.append(value)
    return answer

print(groupAnagrams(Input))
# print(Input)