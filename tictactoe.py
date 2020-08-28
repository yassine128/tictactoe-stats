
# Mail: yassineseddaoui@gmail.com
# Discord username: cursedbuddy#1127

import random
import time
import os
import sys
import numpy as np
from termcolor import colored

global v50
v50 = 0
grid = [0,0,0,0,0,0,0,0,0]
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

count = 0
counto = 0
def simulation():
    count = 0
    counto = 0
    for i in range(9):   # [1,0,0,0,0,4,0,0,0]
        gridx = grid.copy()

        if i == 0:
            c1 = gridx[0] + gridx[3] + gridx[6]
            if c1 == 2:
                count = count+1
        if i == 2:
            c2 = gridx[1] + gridx[4] + gridx[7]
            if c2 == 2:
                count = count+1
        if i == 3:
            c3 = gridx[2] + gridx[5] + gridx[8]
            if c3 == 2:
                count = count+1
        if i == 4:
            d1 = gridx[0] + gridx[4] + gridx[8]
            if d1 == 2:
                count = count+1
        if i == 5:
            d2 = gridx[2] + gridx[4] + gridx[6]
            if d2 == 2:
                count = count+1
        if i == 6:
            c4 = gridx[0] + gridx[1] + gridx[2]
            if c4 == 2:
                count = count+1
        if i == 7:
            c5 = gridx[3] + gridx[4] + gridx[5]
            if c5 == 2:
                count = count+1
        if i == 8:
            c6 = gridx[6] + gridx[7] + gridx[8]
            if c6 == 2:
                count = count+1

    gridx.clear()
    
    for i in range(9):   # [1,0,0,0,0,4,0,0,0]
        grido = grid.copy()

        if i == 0:
            c1 = grido[0] + grido[3] + grido[6]
            if c1 == 8:
                counto = counto+1
        if i == 2:
            c2 = grido[1] + grido[4] + grido[7]
            if c2 == 8:
                counto = counto+1
        if i == 3:
            c3 = grido[2] + grido[5] + grido[8]
            if c3 == 8:
                counto = counto+1
        if i == 4:
            d1 = grido[0] + grido[4] + grido[8]
            if d1 == 8:
                counto = counto+1
        if i == 5:
            d2 = grido[2] + grido[4] + grido[6]
            if d2 == 8:
                counto = counto+1
        if i == 6:
            c4 = grido[0] + grido[1] + grido[2]
            if c4 == 8:
                counto = counto+1
        if i == 7:
            c5 = grido[3] + grido[4] + grido[5]
            if c5 == 8:
                counto = counto+1
        if i == 8:
            c6 = grido[6] + grido[7] + grido[8]
            if c6 == 8:
                counto = counto+1
    grido.clear()

    passing = 0

    
    if count > counto:
        print(colored('Player X is dominating', 'red'))
        print('X has '+str(count)+' chances of winning')
        print('O has '+str(counto)+' chances of winning')
        print(' ')
    if count < counto:
        print(colored('Player O is dominating', 'red'))
        print('X has '+str(count)+' chances of winning')
        print('O has '+str(counto)+' chances of winning')
        print(' ')
    if count == 0 and counto == 0:
        print(colored('No one is dominating', 'green'))
        print('X has '+str(count)+' chances of winning')
        print('O has '+str(counto)+' chances of winning')
        print(' ')
        passing = 1
    if count == counto and passing == 0:
        if (player/2).is_integer() == True:
            print(colored('X is going to win!', 'yellow'))
            print('X has '+str(count)+' chances of winning')
            print('O has '+str(counto)+' chances of winning')
            print(' ')
        if (player/2).is_integer() == False:
            print(colored('O is going to win!', 'yellow'))
            print('X has '+str(count)+' chances of winning')
            print('O has '+str(counto)+' chances of winning')
            print(' ')
    

def tie():
    if 0 not in grid:
        print("Game ended! It's a tie :(")
        sys.exit()

def printboard():
    print('')
    print('')
    print(str(board[0])+"|"+str(board[1])+"|"+str(board[2]))
    print("-+-+-")
    print(str(board[3])+"|"+str(board[4])+"|"+str(board[5]))
    print("-+-+-")
    print(str(board[6])+"|"+str(board[7])+"|"+str(board[8]))


def checkwinner():
    global v50
    c1 = grid[0] + grid[3] + grid[6]
    c2 = grid[1] + grid[4] + grid[7]
    c3 = grid[2] + grid[5] + grid[8]
    d1 = grid[0] + grid[4] + grid[8]
    d2 = grid[2] + grid[4] + grid[6]
    
    if sum(grid[:3]) == 3 or sum(grid[3:6]) ==3 or sum(grid[6:9]) == 3:
        print("X WON")
        sys.exit()
        v50 = 1
    elif c1 == 3 or c2 == 3 or c3 ==3:
        print("X WON")
        sys.exit()
        v50 = 1
    elif d1 == 3 or d2 == 3:
        print("X WON")
        sys.exit()
        v50 = 1
    if sum(grid[:3]) == 12 or sum(grid[3:6]) ==12 or sum(grid[6:9]) == 12:
        print("O WON")
        sys.exit()
        v50 = 1
    elif c1 == 12 or c2 == 12 or c3 ==12:
        print("O WON")
        sys.exit()
        v50 = 1
    elif d1 == 12 or d2 == 12:
        print("O WON")
        sys.exit()
        v50 = 1

v2 = 0
player = 0

print(str(1)+"|"+str(2)+"|"+str(3))
print("-+-+-")
print(str(4)+"|"+str(5)+"|"+str(6))
print("-+-+-")
print(str(7)+"|"+str(8)+"|"+str(9))
print(' ')
print('This is the numbers to navigate on the board!')
print('Press Enter to start the game!')
input()
os.system('cls')

while(True):
    if (player/2).is_integer() == True:
        xmove = input('X turn: ') 
        try:
            xmove = int(xmove)
        except:
            print('Please enter only numbers :(')
            time.sleep(5)
            break
        if isinstance(int(xmove), int) == True:
            xmove = int(xmove)
            if xmove <= 9: 
                if grid[xmove-1] == 0:
                    grid[xmove-1] = 1
                    board[xmove-1] = 'X'
                    os.system("cls")
                    player=player+1
                    printboard()
                    checkwinner()
                    tie()
                    simulation()
                    count = 0
                    counto = 0
                else:
                    print('Case choice not available')
            else:
                print('Position not available')
        else:
            print('Position not available')
    if (player/2).is_integer() == False:
        xmove = input('O turn: ')
        try:
            xmove = int(xmove)
        except:
            print('Please enter only numbers :(')
            time.sleep(5)
            break
        if isinstance(int(xmove), int) == True:
            xmove = int(xmove)
            if int(xmove) <= 9:
                if grid[xmove-1] == 0:
                    grid[xmove-1] = 4
                    board[xmove-1] = 'O'
                    os.system("cls")
                    printboard()
                    player=player+1
                    checkwinner()
                    tie()
                    simulation()
                    count = 0
                    counto = 0
                else:
                    print('Case choice not available')
            else:
                print('Position not available')
        else:
            print('Position not available')


