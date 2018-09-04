def find_all(word):
    anagrams = []
    for index, char in enumerate(word):
        word_without_char = word[:index] + word[index+1:]
        anagrams += recurse_append_anagrams(char, word_without_char)
    return anagrams

def recurse_append_anagrams(first_word, letters):
    anagrams = []
    if not len(letters):
        return first_word
    for index, char in enumerate(letters):
        word_without_char = letters[:index] + letters[index+1:]
        list_of_anagrams = recurse_append_anagrams(char, word_without_char)
        [anagrams.append(first_word+anagram) for anagram in list_of_anagrams]
    return anagrams
