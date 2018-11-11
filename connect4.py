#Initialise a playing board
playGame=True
column0 = 5
columns=["0","1","2","3","4","5","6"]
board=[
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
    [".",".",".",".",".",".","."],
    ]

#initialise functions
def pboard():
    print(columns)
    for i in range(len(board)):
        print(board[i])

#main game loop
print("Welcome to connect 4")
print("X will go first")
#print("To take a turn, choose a column")
pboard()

while playGame:

    Xturn = input("X Please choose a column")
    if Xturn =="0":
        board[column0][0] = "X"
        column0 = column0 - 1

    pboard()

    Oturn = input(" O Please choose a column")
    if Oturn =="0":
        board[column0][0] = "O"
        column0= column0 - 1


    pboard()