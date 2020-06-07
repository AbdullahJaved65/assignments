def hangman(word):
    win = False
    print("Welcome To Hangman!")
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    wrong = 0

    while wrong < len(stages) - 1:
        character = input("Guess the letter: ")
        if character in remaining_letters:
            char_index = remaining_letters.index(character)
            board[char_index] = character
            remaining_letters[char_index] = "$"
        else:
            wrong += 1
            print((" ".join(board)))
            print("\n".join(stages[0:wrong +1]))
        if "_" not in board:
            print("You won!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("You lost. It was {}".format(word))

hangman("abdullah")