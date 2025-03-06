pattern = ["  #","#  ","# #","###"]
numPattern  = [[3,0,3,3,2,3,3,3,3,3],
               [2,0,0,0,2,1,1,0,2,2],
               [2,0,3,3,3,3,3,0,3,3],
               [2,0,1,0,0,0,2,0,2,0],
               [3,0,3,3,0,3,3,0,3,3]
              ]
s=input()
for row in range(5):
    for column in s:
        print(pattern[numPattern[row][int(column)]], end=" ")
    print()