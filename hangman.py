import random

def hangman():
    word_list = ["Python", "Java", "computer", "hacker", "painter"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
              "_______      ",
              "|            ",
              "|      |     ",
              "|      0     ",
              "|     /|\    ",
              "|     / \    ",
              "|            ",
              ]
    rletters = list(word)
    # print(rletters)
    board = ["_"] * len(word)
    # print(board)
    win = False
    print(win)
    print("ハングマンへようこそ！")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
            # print(cind)
            # print(board)
            # print(rletters)
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け！正解は{}.".format(word))


hangman()
