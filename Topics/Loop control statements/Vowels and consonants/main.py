vowel = "aeiou"
s = input()
for i in s:
    if i.isalpha():
        if i in vowel:
            print("vowel")
        else:
            print("consonant")
    else:
        break
