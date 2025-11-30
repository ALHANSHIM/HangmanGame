import random 
words = ["mohammed", "men", "good"] 
print("#######  Welcome to hangman game  ######\n\n")
print(f"\n\n#######  You have {len(words)} words in your bank word  ######\n\n")
none = 1
while none != 0:

    intro = int(input("Enter\n1. for help\n\n2. for add word\n\n3. for remove word\n\n4. for play\n"))

    if intro == 1:
        print("""
         1. think about word.
         2. enter the latter.
         3. if the latter in word will show it.
         4. if the latter not in the word will loss one try.
         5. good luck.

         """)
        did = input("type yes to play or no for come back to menu:").lower()
        if did == "yes":
            none -= 1
        elif did == "no":
            none = 1
    elif intro == 2:
       add_word = input("Enter the word:")
       words.append(add_word)
       print("the word added")
       print(f"\n\n#######  You have {len(words)} words in your bank word  ######\n\n")
       did = input("type yes to play or no for come back to menu:").lower()
       if did == "yes":
           none -= 1
       elif did == "no":
           none = 1
    elif intro == 3:
       remove_word = input("Enter the word that you want to remove:")
       words.remove(remove_word)
       print("the word removed")
       print(f"\n\n#######  You have {len(words)} words in your bank word  ######\n\n")
       did = input("type yes to play or no for come back to menu:").lower()
       if did == "yes":
         none -= 1
       elif did == "no":
         none = 1
    elif intro == 4:
       print("let's play")
       break

word = random.choice(words) 

len_word = len(word) 
trys = 7
errors = 0
hangman_stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    ========= 
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    ========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    ========= 
    ''',
    '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    '''
]


none = ["_ "] * len(word)
print("".join(none))

while "_ " in none and trys > 0:
    enter = input("enter the latter:")
    found = False
    for i in range(len(word)):
        if word[i] == enter:
            none[i] = enter
            found = True

    if found:
        print(f"your trys is {trys}")

    if enter not in word:
        errors += 1
        trys -= 1
        print(f"you lost one try {trys}")
        print(hangman_stages[errors])

    print("".join(none))

if trys == 0:
    print("you lose")

else:
    print("##################")
    print("##################\n")
    print("you win\n")
    print("##################")
    print("##################")
