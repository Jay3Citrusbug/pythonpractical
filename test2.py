un=[]
random_puzzle = [
    ["$", "#", "#", "$", "#"], 
    ["%", "%", "%", "#", "#"], 
    ["$", "$", "%", "$", "%"]
    ]
for i in random_puzzle:
    for j in i:
        if j not in un:
            un.append(j)
print(un)

for i in range(len(un)):
    count = 0
    
    for j in range(len(random_puzzle)):
        for s in range(len(random_puzzle[j])): #len(random_puzzle[0])=5
            if un[i] == random_puzzle[j][s]:   #un[i]=$
                temp = random_puzzle[i][count]
                random_puzzle[i][count] = random_puzzle[j][s]
                random_puzzle[j][s] = temp
                count += 1
            else:
                count += 0
                
                
print(random_puzzle)
print("Count is ",count)
                





                
        

       
    
