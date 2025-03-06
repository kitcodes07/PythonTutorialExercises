
def check_sudoku(input_list):
    sudoku=[]
    for i in range(9):
       #sudoku.append(input())
       sudoku.append(input_list[i])

    count = 0
    for i in range(9):
      if 45 != sum(int(ch) for ch in sudoku[i]):
          print("row", sum(int(ch) for ch in sudoku[i]))
          count += 1
          break
    for r0, r1, r2, r3, r4, r5, r6, r7, r8  in zip(sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8]):
      column = [int(r0), int(r1), int(r2), int(r3), int(r4), int(r5), int(r6), int(r7), int(r8)]
      print(column)
      if 45 != sum(column):
           print("column", sum(column))
           count += 1
           break
    total=[0,0,0,0,0,0,0,0,0]
    #3x3 tiles checker
    for z in range(3):
        x = z * 3
        for y in range(3):
            for i in range(3):
                total[x + 0] += int(sudoku[i + x][y])
                total[x + 1] += int(sudoku[i + x][y+3])
                total[x + 2] += int(sudoku[i + x][y+6])
    for i in total:
        if i != 45:
            count += 1
            break
    if count == 0:
        print("Yes")
    else:
        print("No")

sample_input1=["295743861",
               "431865927",
               "876192543",
               "387459216",
               "612387495",
               "549216738",
               "763524189",
               "928671354",
               "154938672"]

sample_input2=["195743862",
               "431865927",
               "876192543",
               "387459216",
               "612387495",
               "549216738",
               "763524189",
               "928671354",
               "254938671"]

check_sudoku(sample_input1)
check_sudoku(sample_input2)

# the challenge is the boxes