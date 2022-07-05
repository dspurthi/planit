# Challenge 2:
# Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring
# case. If there is more than one character with equal highest occurrences, return the character that appeared first
# within the string.
# For example:
# Input: "Character"
# Output: c
def character_with_high_occurrences(s):
    new_string = s.lower()
    dict_of_count = {}
    for char in new_string:
        if char not in dict_of_count:
            dict_of_count[char] = 1
        else:
            dict_of_count[char] += 1
    occurences_list = dict_of_count.values()
    highest_occurences_count = max(occurences_list)
    chars = []
    for key, value in dict_of_count.items():
        if highest_occurences_count == value:
            chars.append(key)
    if len(chars) == 1:
        print(chars)
    else:
        ind = len(new_string)
        for char in chars:
            i = new_string.index(char)
            if i < ind:
                ind = i
        print(s[ind])

character_with_high_occurrences("Character")