import os

#get word list

#method using nltk
# import nltk
# # nltk.download() # use when first run
# word_list = nltk.corpus.words.words()

#method using system words, only for Linux or macOS

words = open("/usr/share/dict/words", "r")
word_list = words.read().split()
words.close()
print(len(word_list))

#get 5 character long words
word_list = [word for word in word_list if len(word) == 5]

green_letters = {}
yellow_letters = {}
gray_letters = set()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        mode = int(input(
'''
1. add a green letter
2. add a yellow letter
3. add gray letters
4. show {} candidates
5. reset
6. enter any other input to exit
choose an option: '''
        .format(len(word_list))))
    except (ValueError, TypeError):
        mode = 0

    if mode == 1:
        positionIndex = int(input("position: ")) - 1
        letter = input("letter: ")
        green_letters[positionIndex] = letter
    elif mode == 2:
        positionIndex = int(input("position: ")) - 1
        letter = input("letter: ")
        yellow_letters[positionIndex] = letter
    elif mode == 3:
        letters = input("letters(seperate by space): ").split()
        for letter in letters:
            gray_letters.add(letter)
    elif mode == 4:
        for word in word_list:
            print(word, end=' ')
        input("\npress enter to continue ...")
        continue
    elif mode == 5:
        words = open("/usr/share/dict/words", "r")
        word_list = words.read().split()
        words.close()
        green_letters = {}
        yellow_letters = {}
        gray_letters = set()
        continue
    else:
        confirm = input("are you sure you want to exit? (y/[n]) ")
        if confirm.lower() == 'y':
            break
        else:
            continue

    #gray
    tempList = []
    for word in word_list:
        valid = True
        for c in gray_letters:
            if c in word:
                valid = False
                break
        if valid:
            tempList.append(word)

    word_list = tempList.copy()  

    #green
    tempList = []
    for word in word_list:
        # check each green letter
        valid = True
        for i in range(5):
            if i not in green_letters:
                continue
            if word[i].lower() != green_letters[i].lower():
                valid = False
                break
        if valid:
            tempList.append(word)
    word_list = tempList.copy()

    #yellow
    tempList = []
    for word in word_list:
        # check each yellow letter
        valid = True
        for i in range(5):
            if i not in yellow_letters:
                continue
            if yellow_letters[i].lower() not in word or yellow_letters[i].lower() == word[i].lower():
                valid = False
                break
        if valid:
            tempList.append(word)
    word_list = tempList.copy()

