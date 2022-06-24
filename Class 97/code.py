userInput = input("Enter your statement :")
characterCount = 0
wordCount = 1

for i in userInput:
    characterCount = characterCount + 1

    if i == ' ' :
        wordCount = wordCount + 1

print(wordCount)
print(characterCount)