import random
import turtle


L = 1023

T = turtle.Turtle()
T.pensize(7)
T.hideturtle()
T.speed(0)
board = turtle.Screen()
board.setworldcoordinates(0, 0, L+1, L+1)


    


def setposition(x,y): 
    T.penup()
    T.setposition(x,y)
    T.pendown()
    return 

def horizontal():
    T.seth(0)
    setposition(0,L//3)
    T.forward(L)
    setposition(0,(2*L)//3)
    T.forward(L)
    

def vertical():
    setposition(L//3,0)
    T.seth(90)
    T.forward(L)
    setposition((2*L)//3,0)
    T.forward(L)
    



def draw_cross(angle, x, y): 
    s = L//3
    d = int((2*s*s)**0.5)
    setposition(x+s//2, y+s//2)
    T.seth(angle)
    T.forward(d-320)
    

def cross(x,y):            
    T.pensize(20)
    T.pencolor("light blue")
    draw_cross(45, x, y)
    draw_cross(225, x, y)
    draw_cross(135, x, y)
    draw_cross(315, x, y)
    

def circle(x,y):            
    T.pensize(20)
    T.pencolor("red")
    T.seth(90)
    radius=(1/9)*L
    setposition(x+L/18,y+L/6)
    T.circle(-radius)

def draw_pattern(symbol, move,dictionary):
    
    coordinates = dictionary[move]
    if symbol == 'O':
        circle(coordinates[0],coordinates[1])
    elif symbol == 'X':
        cross(coordinates[0],coordinates[1])
    return


def check_corner(move): 
    return move in ["1","3","7","9"]

def check_center(move): 
    return move=="5"

def check_edge(move):   
    return move in ["2", "4", "6", "8"]

def check_draw(places_taken):   
    return len(places_taken)==9

def generate_choice():
    while True:
        user_choice = input("Would you like Cross (X) or Noughts (O)?: ")
        user_choice = user_choice.upper()
        if user_choice != 'X' and user_choice != 'O':
            print ("Enter a valid symbol!")
        else:
            break
    return user_choice

def comp_choice(user_choice):
    if user_choice == 'X':
        return 'O'
    else:
        return 'X'


def check_win(current_list): 
    win = [["1","2","3"],["4","5","6"],["7","8","9"],["1","4","7"],["2","5","8"],["3","6","9"],["1","5","9"],["3","5","7"]]
    for win_move_list in win:
        cnt = 0
        for win_move in win_move_list:
            if win_move in current_list:
                cnt += 1
        if cnt == 3:
            return True
    return False


def win_or_block(computer_moves, user_moves):
    win = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['1', '5', '9'], ['3', '5', '7'], ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9']]
    for move_list in win:
        cnt = 0
        for i in range(len(move_list)):
            if move_list[i] in computer_moves:
                move_list[i] = '-1'
                cnt += 1
        for move in move_list:
            if cnt == 2 and move != '-1' and move not in user_moves:
                return move
    return -1


def computer_first_turn():

    return random.choice(["1","3","5","5","5","7","9"]) #5 added multiple times to make probability of a center chosen roughly equal to that of a corner

def check_position(position,computer_moves,user_moves):
    if position not in computer_moves and position not in user_moves:
        return True
    return False



def user_input(places_taken,dictionary):
    while True:
        user = input("Enter your move (1-9): ")
        if user in places_taken:
            print("This space is already occupied!")
        else:
            if isValid(user,dictionary):
                return user
            else:
                print("Enter a valid move!")
            
def user_turn(user_moves,places_taken,dictionary,user_symbol):
    user=user_input(places_taken,dictionary)
    user_moves.append(user)
    places_taken.append(user)
    draw_pattern(user_symbol,user,dictionary)
    return user




def computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol):
    
    computer_moves.append(computer)
    places_taken.append(computer)
    coordinates=dictionary[computer]
    draw_pattern(computer_symbol,computer,dictionary)


def freeplay(first_in_free_play,user_moves,computer_moves,places_taken,dictionary,user_symbol,computer_symbol):
    
    
    
    if first_in_free_play=="user":
        
        user=user_turn(user_moves,places_taken,dictionary,user_symbol)
    
    while True:
        if win_or_block(computer_moves,user_moves)!=-1:
            computer=win_or_block(computer_moves,user_moves)
        elif win_or_block(user_moves,computer_moves)!=-1:
            computer=win_or_block(user_moves,computer_moves)
        else:
            computer=random_move(places_taken)
            
                
        computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol) 
            
        if check_win(computer_moves) or check_win(user_moves) or check_draw(places_taken):
            break
        user=user_turn(user_moves,places_taken,dictionary,user_symbol)
        if check_win(computer_moves) or check_win(user_moves) or check_draw(places_taken):
            break
    return user_moves,computer_moves,places_taken

def display_result(computer_moves,user_moves):
    if check_win(computer_moves):
        print("Computer Won")
    elif check_win(user_moves):
        print("User Won")
    else:
        print("It's a draw!")

def random_corner(places_taken):
    
    corners_list=["1","3","7","9"]
    for i in corners_list:
        if i not in places_taken:
            computer=i
    return computer

def other_corner(computer,places_taken):
    rows_and_columns=[["1","2","3"],["4","5","6"],["7","8","9"],["1","4","7"],["2","5","8"],["3","6","9"]]
    for row_column in rows_and_columns:
        if (computer in row_column) and row_column[1] not in places_taken:
            row_column[1]="0"
            index=row_column.index(computer)
            row_column[index]="0"
            row_column.sort()
            computer=row_column[2]
            break
    
    return computer

    

def generate_choice():
    while True:
        user_symbol = input("Would you like Cross (X) or Noughts (O)?: ")
        user_symbol = user_symbol.upper()
        if user_symbol != 'X' and user_symbol != 'O':
            print ("Enter a valid symbol!")
        else:
            break
    return user_symbol

def comp_choice(user_symbol):
    if user_symbol == 'X':
        return 'O'
    else:
        return 'X'
    
def isValid(user, dictionary):
    if dictionary.get(user,0) != 0:
        return True
    return False


def random_move(places_taken):
    
    non_repeated=False
    while not(non_repeated):
        computer=random.choice(["1","2","3","4","5","6","7","8","9"])
        if computer not in places_taken:
            non_repeated=True
    return computer
     
        
def user_corner(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken,user1):
    check_corner_dict = {'1':['6', '8'], '3':['4', '8'], '9':['2', '4'], '7':['2', '6']}
    corner_mid_dict = {'16' : '4', '18' : '2', '38' : '2', '34' : '6', '92' : '8', '94' : '6', '72' : '8', '76' : '4'}
    cnt = 0
    while not(check_win(computer_moves)):
        cnt += 1
        user = user_turn(user_moves,places_taken,dictionary,user_symbol)
        
        if not(check_draw(places_taken)) and not(check_win(user_moves)):
            if cnt == 1 and user == str((2*int(computer_moves[0])) - int(user1)):
                comp = random.choice(['2', '4', '6', '8'])
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
                cnt += 1
            elif cnt == 1 and user in check_corner_dict[user1]:
                new_list_ele = []
                list_ele = ['2', '4', '6', '8']
                for ele in list_ele:
                    if ele != corner_mid_dict[user1+user] and check_position(ele,computer_moves,user_moves):
                        new_list_ele.append(ele)
                cnt += 5
                user2 = user
                comp = random.choice(new_list_ele)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif cnt == 7 and user1+user2 in corner_mid_dict and user1+user in corner_mid_dict:
                list_ele = ['1', '3', '7', '9']
                new_list_ele = []
                for ele in list_ele:
                    if ele != str((2*int(computer_moves[0])) - int(user1)) and ele != user1:
                        new_list_ele.append(ele)
                comp = random.choice(new_list_ele)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif win_or_block(computer_moves, user_moves) != -1:
                    comp = win_or_block(computer_moves, user_moves)
                    computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif win_or_block(user_moves, computer_moves) != -1:
                    comp = win_or_block(user_moves, computer_moves)
                    computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            else:
                comp = random_move(computer_moves+ user_moves)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
        else:
            break


def user_center(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken,user1):
    cnt = 0
    while not(check_win(computer_moves)):
        cnt +=1
        user = user_turn(user_moves, user_moves + computer_moves, dictionary,user_symbol)
        
        if not(check_draw(user_moves+computer_moves)) and not(check_win(user_moves)):
            if user == str(2*int('5') - int(user1)) and cnt == 1:
                    new_list_ele = []
                    list_ele = ['1', '3', '7', '9']
                    for ele in list_ele:
                        if check_position(ele,computer_moves,user_moves):
                            new_list_ele.append(ele)
                    comp = random.choice(new_list_ele)
                    computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif win_or_block(computer_moves, user_moves) != -1:
                comp = win_or_block(computer_moves, user_moves)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif win_or_block(user_moves, computer_moves) != -1:
                comp = win_or_block(user_moves, computer_moves)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            else:
                comp = random_move(places_taken)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
                
        else:
            break


def user_edge(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken,user1):
    edge_dict_check = {'24':'9', '42':'9', '26':'7', '62':'7', '68':'1', '86':'1', '48':'3', '84':'3'}
    edge_dict = {'2':['7', '9'], '4':['3', '9'], '6':['1', '7'], '8':['1', '3']}
    edge_corner= {'61' : '3', '67' :'9', '81' : '7', '83' : '9', '43' : '1', '49': '7', '27': '1', '29': '3'}
    edge_mid = {'39':'6', '13' : '2', '17' : '4', '31' : '2', '93' : '6', '97' : '8', '79' : '8', '71' : '4'}
    cnt = 0
    while not(check_win(computer_moves)):
        cnt += 1
        user = user_turn(user_moves, places_taken, dictionary,user_symbol)
        if not(check_draw(places_taken)) and not(check_win(user_moves)):
            if user == str((2*int(computer_moves[0])) - int(user1)):
                comp = random.choice(['1', '3', '7', '9'])
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif cnt == 1 and user in edge_dict[user1]:
                new_list_ele = []
                list_ele = ['1', '3', '7', '9']
                for ele in list_ele:
                    if ele == edge_corner[user1+user]:
                        new_list_ele.append(ele)
                cnt += 3
                user2 = user
                comp = random.choice(new_list_ele)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif cnt == 1 and check_edge(user):
                new_list_ele = []
                list_ele = ['1', '3', '7', '9']
                for ele in list_ele:
                    if ele != edge_dict_check[user1+user]:
                        new_list_ele.append(ele)
                comp = random.choice(new_list_ele)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
                
            elif cnt == 5 and check_corner(user):
                new_list_ele = []
                list_ele = ['2', '4', '6', '8']
                for ele in list_ele:
                    if check_position(ele,computer_moves,user_moves) and ele != edge_mid[user2+user]:
                        new_list_ele.append(ele)
                comp = random.choice(new_list_ele)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif win_or_block(computer_moves, user_moves) != -1:
                comp = win_or_block(computer_moves, user_moves)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            elif win_or_block(user_moves, computer_moves) != -1:
                comp = win_or_block(user_moves, computer_moves)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
            else:
                comp=random_move(places_taken)
                computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
                
        else:
            break

def user_first(user_symbol,computer_symbol,user_moves, computer_moves, dictionary,places_taken):
    
    user = user_turn(user_moves, places_taken, dictionary,user_symbol)
    
    if check_corner(user) and len(user_moves) == 1:
        comp = '5'
        computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
        user_corner(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken,user)
        
    elif len(user_moves) == 1 and check_center(user):
        comp = random.choice(['1', '3', '7', '9'])
        computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
        user_center(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken,comp)
        
    elif len(user_moves) == 1 and check_edge(user):
        comp = '5'
        computer_turn(comp,computer_moves,places_taken,dictionary,computer_symbol)
        user_edge(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken,user)
    return computer_moves,user_moves




def computer_first(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken):
    
    while True:
    
        #computer goes first
            
            
            computer=computer_first_turn()
                      
            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
           
                    
            #computer goes to center
            if check_center(computer):
                
                user=user_turn(user_moves,places_taken,dictionary,user_symbol)
            #user has two choices. Edge or Corner
                    
                        
                if check_edge(user):
                    #user chooses edge
                    edge_dictionary={"2":["7","9"],"4":["3","9"],"6":["1","7"],"8":["1","3"]}
                    computer=random.choice(edge_dictionary[user])
                    computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                    user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                    if win_or_block(computer_moves,user_moves)!=-1:
                        computer=win_or_block(computer_moves,user_moves)
                        computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                        
                        break
                    else:
                        computer=win_or_block(user_moves,computer_moves)
                    
                    computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                    
                    user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                    computer=win_or_block(computer_moves,user_moves)
                    computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                    break
                    
                else:
                    #user chooses corner
                    if check_corner(user):
                        computer=str(10-int(user))
                        computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                        
                        user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                        #user chooses edge
                        if check_edge(user):
                            if win_or_block(user_moves,computer_moves)!=-1:
                                computer=win_or_block(user_moves,computer_moves)
                            else:
                                computer=random_corner(places_taken)
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            
                            user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                            computer=win_or_block(computer_moves,user_moves)
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            break
                        #user chooses corner
                        elif check_corner(user):
                            computer=win_or_block(user_moves,computer_moves)
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            user_moves,computer_moves,places_taken=freeplay("user",user_moves,computer_moves,places_taken,dictionary,user_symbol,computer_symbol)
                            break
                
            else:
                #computer goes to corner in the first turn
                if check_corner(computer):
                    #user choice
                                          
                    user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                    #user chooses center
                    if check_center(user):
                        computer=str(10-int(computer))
                        computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                        user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                        #user chooses corner
                                              
                        if check_corner(user):
                            
                          computer=win_or_block(user_moves,computer_moves)
                          computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                          user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                          computer=win_or_block(computer_moves,user_moves)
                          computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                          break
                        elif check_edge(user):
                            user_moves,computer_moves,places_taken=freeplay(computer,user_moves,computer_moves,places_taken,dictionary,user_symbol,computer_symbol)
                            break
                    #user doesnt choose center
                    else:
                        
                        if check_corner(user):
                            
                            computer=random_corner(places_taken)
                            
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                            if win_or_block(computer_moves,user_moves)!=-1:
                                computer=win_or_block(computer_moves,user_moves)
                                computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                                break
                            else:
                                computer=random_corner(places_taken)
                                computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                                
                            user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                            computer=win_or_block(computer_moves,user_moves)
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            
                            break

                        elif check_edge(user):
                            print
                            computer=other_corner(computer,places_taken)
                            if not(check_corner(computer)):
                                computer=random_corner(places_taken)
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                            if win_or_block(computer_moves,user_moves)!=-1:
                                computer=win_or_block(computer_moves,user_moves)
                                computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                                break
                            elif win_or_block(user_moves,computer_moves)!=-1:
                                computer=win_or_block(user_moves,computer_moves)
                                
                            else:
                                computer=random_corner(places_taken)
                                
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)
                            user=user_turn(user_moves,places_taken,dictionary,user_symbol)
                            computer=win_or_block(computer_moves,user_moves)
                            computer_turn(computer,computer_moves,places_taken,dictionary,computer_symbol)

                            
                            
                            break    
                        
    return computer_moves,user_moves                            
                        
                            
                        
                        
                
   
def main():
    
    
    
    horizontal()
    vertical()

    user_moves=[]
    computer_moves=[]
    places_taken=[]
    dictionary={"1":[0,(2*L//3)],"2":[L//3,2*L//3],"3":[2*L//3,2*L//3],"4":[0,L//3], "5":[L//3,L//3],"6":[2*L//3,L//3],"7":[0,0],"8":[L//3,0],"9":[2*L//3,0]}
    user_symbol=generate_choice()
    computer_symbol=comp_choice(user_symbol)
    while True:
        first_choice=input("Who would you like to play first? (C)omputer or (U)ser: ")
        first_choice=first_choice.upper()
        if first_choice=="C" or first_choice=="U":
            break
    if first_choice=="U":
        computer_moves,user_moves = user_first(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken)
    else:
        computer_moves,user_moves = computer_first(user_symbol,computer_symbol,user_moves,computer_moves,dictionary,places_taken)

    display_result(computer_moves,user_moves)
    play_again = input("Would you like to play (and lose, lol) again?(Y/N): ")
    play_again = play_again.upper()
    if play_again == 'Y':
        turtle.clearscreen()
        setposition(0,0)
        T.color("black")
        main()

main()
    

