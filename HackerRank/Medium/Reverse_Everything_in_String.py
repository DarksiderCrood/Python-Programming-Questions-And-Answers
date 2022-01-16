def checkAndPrint(text):
    # Write your code here
    words = text.split(" ")
    new_words = []
    for word in words:
        new_words.append(word[::-1])
    letters = ' '.join(new_words)
    print(letters.swapcase())

if __name__ == '__main__':
    text = "Hello World" # input()

    checkAndPrint(text)