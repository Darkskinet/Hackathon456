# Tic Tac Toe
from random import randint
def pb(xstate, ostate):
    a = 'X' if xstate[0] == 1 else 'O' if ostate[0] == 1 else '0' 
    b = 'X' if xstate[1] == 1 else 'O' if ostate[1] == 1 else '1' 
    c = 'X' if xstate[2] == 1 else 'O' if ostate[2] == 1 else '2' 
    d = 'X' if xstate[3] == 1 else 'O' if ostate[3] == 1 else '3' 
    e = 'X' if xstate[4] == 1 else 'O' if ostate[4] == 1 else '4' 
    f =  'X' if xstate[5] == 1 else 'O' if ostate[5] == 1 else '5' 
    g = 'X' if xstate[6] == 1 else 'O' if ostate[6] == 1 else '6' 
    h = 'X' if xstate[7] == 1 else 'O' if ostate[7] == 1 else '7'
    i =  'X' if xstate[8] == 1 else 'O' if ostate[8] == 1 else '8'
    print(f"{a} I  {b}  I {c}")
    print("-------------")
    print(f"{d} I  {e}  I {f}")
    print("-------------")
    print(f"{g} I  {h}  I {i}")
def sum(a, b, c):
    return a + b + c

def sum1(xstate):
    ref = 0
    for i in xstate:
        ref = i + ref
    return ref

def sum2(ostate):
    ref2 = 0
    for i in ostate:
        ref2 = i + ref2
    return ref2

def sum3(a, b):
    return a + b
        
def winner(xstate, ostate):
    Possibilities = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in Possibilities:
        if sum(xstate[i[0]], xstate[i[1]], xstate[i[2]]) == 3:
            print("X is the winner")
            return 1
            
        if sum(ostate[i[0]], ostate[i[1]], ostate[i[2]]) == 3:
            print("O is the winner")
            return 0
    return -1 
            
        
xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1
while True:
    print("\n")
    pb(xstate, ostate)
    print("\n")
    l = winner(xstate, ostate)
    ab = sum1(xstate)
    ab1 = sum2(ostate)
    if sum3(ab, ab1) == 9:
        print("\n""It's a Tie")
        break
    if l != -1:
        print("Game Over !!!!")
        break
    if turn == 1:
        print("It's X's Turn")
        a = int(input("Enter a value: "))
        xstate[a] = 1
        turn = turn - 1
    else:
        print("It's O's Turn")
        a = int(input("Enter a value: "))
        ostate[a] = 1
        turn = turn + 1

        
