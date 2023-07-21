#TIC TAK TOE

#function that displays the board
    #-gonna be physically printing the board
#Choose a row and column [row][column]
#The user inputs are going to be the row(integer) and column(integer)
def display_table(tableArray):
    #x,x,x
    #x,x,x
    #x,x,x
    print("ready to play tic tac toe?") #O(1)
    
    #make this a function to display the board everytime we need it
    for i in range(len(tableArray)):#O(n)               #O(n^2) nested for loops
        for j in range(len(tableArray[0])):#O(n)
            print(tableArray[i][j], "|",end = "")
        #new line
        print("\n","----------")
def tic_tac_toe():
    x = 'F'
    tableArray = [[x,x,x,],[x,x,x,],[x,x,x,]]  
    won = False
    Player_1 = input("First player choose X or O: ")
    moves = 0 
    
    while not won: #O(n)
        #let user input the row and column
        row = int(input("Enter the row from 0-2: "))
        col = int(input("Enter the column 0-2: "))

        #if the element in the array is greater then 0 then that means a user has already placed somthing at that spot
        if (tableArray[row][col] == "F" ):#O(1)
            
            #row = int(input("Enter the row from 0-2: "))
            #col = int(input("Enter the column 0-2: "))
            
            tableArray[row][col] = Player_1
            display_table(tableArray)
            moves += 1
            
            #player chooses a location and we check if they won or not
            won = win_condition(tableArray, Player_1)
            if(not won):
                Player_1 = input("Next Player: Enter a character(X/O): ")
            
    print("thank you for playing")
            
       
            
        
    #check for win condition
    #Rows
def win_condition(tableArray, Player_1) -> bool:
    for i in range(len(tableArray)):
        if tableArray[i][0] == tableArray[i][1] == tableArray[i][2] == Player_1:
            return True
    #check colunmns
    for i in range(len(tableArray[0])):
        if tableArray[0][i] == tableArray[1][i] == tableArray[2][i] == Player_1:
            return True
    #Diagonals
    if tableArray[0][0] == tableArray [1][1] == tableArray[2][2] == Player_1:
        return True
    if tableArray[0][2] == tableArray [1][1] == tableArray[2][0] == Player_1:
        return True
    
    return False 

#Switch Players

tic_tac_toe()
    
 



    

