#imports
import random

#defining the grid
grid = [
    ["1","2","3"],
    ["4","5","6"],
    ["7","8","9"]]

#definition: print grid
def printGrid():
    for n in grid:
        print(n)

#definition: check if player won, play can be X or O
def checkWon(play,new_grid):
    #check rows
    if new_grid[0][0] == play and new_grid[0][1] == play and new_grid[0][2] == play:
        return True
    elif new_grid[1][0] == play and new_grid[1][1] == play and new_grid[1][2] == play:
        return True
    elif new_grid[2][0] == play and new_grid[2][1] == play and new_grid[2][2] == play:
        return True
    #check columns
    elif new_grid[0][0] == play and new_grid[1][0] == play and new_grid[2][0] == play:
        return True
    elif new_grid[0][1] == play and new_grid[1][1] == play and new_grid[2][1] == play:
        return True
    elif new_grid[0][2] == play and new_grid[1][2] == play and new_grid[2][2] == play:
        return True
    #check diagonals
    elif new_grid[0][0] == play and new_grid[1][1] == play and new_grid[2][2] == play:
        return True
    elif new_grid[0][2] == play and new_grid[1][1] == play and new_grid[2][0] == play:
        return True
    return False

#definition: dupe board
def getgridCopy(grid):
    dupegrid = []
    row_number = 0
    for row in grid:
        dupegrid.append([])
        for element in row:
            dupegrid[row_number].append(element)
        row_number = row_number+1
    return dupegrid

#game intro
print("tictactoe...three in a row...")
printGrid()
print("")

#rounds count
rounds = 0

#GAME BEGIN

#pick a side and computer's first move
while True:
    player = input("Would you like to be X or O? ")
    player = player.capitalize()
    if player == "X":
        computer = "O"
        break
    elif player == "O":
        computer = "X"
        print("")
        print("Computer is X and plays first.")
        cpu_turn = random.randint(1,10)
        grid[int((cpu_turn-1)/3)][int((cpu_turn-1)%3)] = str(computer)
        #print grid
        printGrid()
        break


#GAMEPLAY LOOP
while True:

    #player plays
    while True:
        print("")
        player_turn = int(input(f"Player {player} where would you like to place your {player}? "))
        if grid[int((player_turn-1)/3)][int((player_turn-1)%3)] == "X" or grid[int((player_turn-1)/3)][int((player_turn-1)%3)] == "O":
            print("Please pick a free position!")
        else:
            break

    grid[int((player_turn-1)/3)][int((player_turn-1)%3)] = str(player)

    #print grid
    printGrid()

    #check if player won 
    if checkWon(str(player),grid) == True:
        print("")
        print(f"Player {player} wins!")
        break

    #check for draw
    rounds = rounds +1
    if rounds == 5:
        print("It's a draw~")
        break

    #computer plays
            
    #ranking of moves
    moverank = []

    # check for wins
    for a in range(1,10):
        if grid[int((a-1)/3)][int((a-1)%3)] in ["1","2","3","4","5","6","7","8","9"]:
            grid[int((a-1)/3)][int((a-1)%3)] = str(computer)
            if checkWon(str(computer),grid) == True:
                moverank.append(a)
            grid[int((a-1)/3)][int((a-1)%3)] = str(a)
    print(moverank)

    #check for blocks
    for b in range(1,10):
        simulate = getgridCopy(grid)
        if simulate[int((b-1)/3)][int((b-1)%3)] in ["1","2","3","4","5","6","7","8","9"]:
            simulate[int((b-1)/3)][int((b-1)%3)] = str(player)
            print(simulate)
            if checkWon(str(player),simulate) == True:
                moverank.append(b)
    print(moverank)

    #check for center
    if grid[int((5-1)/3)][int((5-1)%3)] in ["1","2","3","4","5","6","7","8","9"]:
        moverank.append(5)

    #check for corners
    for c in [1,3,7,9]:
        if grid[int((c-1)/3)][int((c-1)%3)] in ["1","2","3","4","5","6","7","8","9"]:
            moverank.append(c)

    #check for other availabilities
    for e in [2,4,6,8]:
        if grid[int((e-1)/3)][int((e-1)%3)] in ["1","2","3","4","5","6","7","8","9"]:
            moverank.append(e)

    #deciding computer's play
    chosen = moverank[0]
    grid[int((chosen-1)/3)][int((chosen-1)%3)] = str(computer) 

    #print grid
    print("")
    print("Computer plays:")
    printGrid()

    #check if computer won 
    if(checkWon(str(computer),grid) == True):
        print("")
        print(f"Player {computer} wins!")
        break
