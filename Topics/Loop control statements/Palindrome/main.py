word = input()
word = word.strip()
word_len = len(word)
sliced_word = word[word_len::-1]  # slicing
if word == sliced_word:
    print("Palindrome")
else:
    print("Not palindrome")
