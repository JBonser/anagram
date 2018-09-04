def find_all(word):
    anagrams = []
    for index, char in enumerate(word):
        word_without_char = word[:index] + word[index+1:]
        new_word = char + word_without_char
        anagrams.append(new_word)
    return anagrams

def recurse_append_anagrams(first_word, remaining_letters):
    return ["ab"]
