def find_all(word):
    anagrams = []
    for index, char in enumerate(word):
        word_without_char = word[:index] + word[index+1:]
        new_word = char + word_without_char
        anagrams.append(new_word)
    return anagrams

def recurse_append_anagrams(first_word, letters):
    anagrams = []
    if len(letters) == 0:
        return first_word
    # for index, char in enumerate(letters):
    #     word_without_char = letters[:index] + letters[index+1:]
    #     list_of_anagrams = recurse_append_anagrams(char, word_without_char)
    #     for anagram in list_of_anagrams:
    #         anagrams.append(first_word+anagram)
    #     #[anagrams.append(first_word+anagram) for anagram in list_of_anagrams]
    #
    # print(anagrams)
    return anagrams
