import random
mat = [['','',''],['','',''],['','','']]
marked = 9

cnt = 0

userMove = input('enter you character * or o: ')
computerMove = ''
if(userMove == '*'):
    computerMove = 'o'
else:
    computerMove = '*'

while(marked):

  if(cnt%2 == 0):
    print("User move: ")
    row = int(input("enter the row: "))
    col = int(input("enter the col: "))
    if(mat[row][col] == ''):
        mat[row][col] = userMove
    else:
        print('place not empty')
        continue;
  else:
    print("Computer move: ")
    row = random.randint(0,2)
    col = random.randint(0,2)
    val = random.randint(0,1)
    if(mat[row][col] == ''):
        mat[row][col] = computerMove
    else:
        print('place not empty')
        continue;

  cnt+=1
  marked -= 1


  if((mat[0][0] == '*' and mat[1][1] == '*' and mat[2][2] == '*') or (mat[0][0] == '*' and mat[0][1] == '*' and mat[0][2] == '*')
    or (mat[1][0] == '*' and mat[1][1] == '*' and mat[1][2] == '*')
    or (mat[2][0] == '*' and mat[2][1] == '*' and mat[2][2] == '*') or (mat[0][2] == '*' and mat[1][1] == '*' and mat[2][0] == '*')
    or 
     (mat[0][0] == '*' and mat[1][0] == '*' and mat[2][0] == '*') or (mat[0][1] == '*' and mat[1][1] == '*' and mat[2][1] == '*')
    or (mat[0][2] == '*' and mat[1][2] == '*' and mat[2][2] == '*')
   
    ):
        if(userMove == '*'):
            print("user wins")
        else:
            print("computer wins")
        break

  elif((mat[0][0] == 'o' and mat[1][1] == 'o' and mat[2][2] == 'o') or (mat[0][0] == 'o' and mat[0][1] == 'o' and mat[0][2] == 'o')
    or (mat[1][0] == 'o' and mat[1][1] == 'o' and mat[1][2] == 'o')
    or (mat[2][0] == 'o' and mat[2][1] == 'o' and mat[2][2] == 'o') or (mat[0][2] == 'o' and mat[1][1] == 'o' and mat[2][0] == 'o')
     or 
     (mat[0][0] == 'o' and mat[1][0] == 'o' and mat[2][0] == 'o') or (mat[0][1] == 'o' and mat[1][1] == 'o' and mat[2][1] == 'o')
    or (mat[0][2] == 'o' and mat[1][2] == 'o' and mat[2][2] == 'o')
    ):
        if(userMove == 'o'):
            print("user wins")
        else:
            print("computer wins")
        break
    

  
  print(mat)


