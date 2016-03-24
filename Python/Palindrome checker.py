def main():
    userWord = input("Enter a word: ")
    lengthWord = len(userWord) - 1
    reversedWord = ""

    for n in range(len(userWord)):
        reversedWord = reversedWord + userWord[lengthWord - n]

    if userWord == reversedWord:
        print(userWord, "is a palindrome")
    else:
        print(userWord, "is not a palindrome")
        

main()
