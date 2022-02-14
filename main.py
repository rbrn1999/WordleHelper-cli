import os

#get word list

# default to use word list from Linux or macOS
# if you're using aother OSs:
# change path to "./words" or path to your custom file
words = open("/usr/share/dict/words", "r")
word_list = words.read().split()
words.close()
print(len(word_list))

#get 5 character long words
word_list = [word for word in word_list if len(word) == 5]

green_letters = {} # {int: char}
yellow_letters = {} # {char: [int]}
gray_letters = set() # {char}

WORD_LEN = 5

def match_green(word):
    for pos in green_letters:
        if word[pos] != green_letters[pos]:
            return False
    return True

def match_yellow(word):
    for chr in yellow_letters:
        if chr not in word:
            return False
        occurs = [i for i, v in enumerate(word) if v == chr]
        if len(set(occurs).intersection(yellow_letters[chr])):
            return False
    return True

def match_gray(word):
    for i, chr in enumerate(word):
        if chr in gray_letters:
            if i in green_letters and green_letters[i] == chr:
                 continue
            if chr in yellow_letters:
                 gp = [i for i in range(WORD_LEN) if i in green_letters and green_letters[i] == chr]
                 lp = [i for i in range(WORD_LEN) if word[i] == chr]
                 if chr in yellow_letters and len(yellow_letters[chr]) >= len(set(lp).difference(gp)):
                     continue
            return False
    return True
 

def showWords(wordList):
    for i, word in enumerate(word_list):
        end = '\n' if (i+1) % 6 == 0 else ' '
        print(word, end=end)
    if len(word_list)+1 % 6:
        print()

showPrev = False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if showPrev:
        showWords(word_list)
    attemp = input('Enter your word: ')
    colors = input('Enter the colors of the letters (gyx): ')

    for i in range(WORD_LEN):
        if colors[i] == 'g':
            green_letters[i] = attemp[i]
            if attemp[i] in yellow_letters and i in yellow_letters[attemp[i]]:
                yellow_letters[attemp[i]].remove(i)
        elif colors[i] == 'y':
            yellow_letters.setdefault(attemp[i], []).append(i)
        elif colors[i] == 'x':
            gray_letters.add(attemp[i])

    

    word_list = list(filter(match_green, word_list))
    word_list = list(filter(match_yellow, word_list))
    word_list = list(filter(match_gray, word_list))

    confirm = input(f'show {len(word_list)} possible answers? [y]/n: ')
    if confirm.lower() != 'n':
        showPrev = True
        showWords(word_list)
    else:
        showPrev = False
    
    confirm = input(f'continue? [y]/n: ')

    if confirm.lower() == 'n':
        break