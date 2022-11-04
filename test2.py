# # un=[]
# # random_puzzle = [
# #     ["$", "#", "#", "$", "#"], 
# #     ["%", "%", "%", "#", "#"], 
# #     ["$", "$", "%", "$", "%"]
# #     ]
# # for i in random_puzzle:
# #     for j in i:
# #         if j not in un:
# #             un.append(j)
# # print(un)

# # for i in range(len(un)):
# #     count = 0
    
# #     for j in range(len(random_puzzle)):
# #         for s in range(len(random_puzzle[j])): #len(random_puzzle[0])=5
# #             if un[i] == random_puzzle[j][s]:   #un[i]=$
# #                 temp = random_puzzle[i][count]
# #                 random_puzzle[i][count] = random_puzzle[j][s]
# #                 random_puzzle[j][s] = temp
# #                 count += 1
# #             else:
# #                 count += 0
                
                
# # print(random_puzzle)
# # print("Count is ",count)



# # another method

# # un=[]
# # random_puzzle = [
# #     ["$", "#", "#", "$", "#"], 
# #     ["%", "%", "%", "#", "#"], 
# #     ["$", "$", "%", "$", "%"]
# #     ]
# # for i in random_puzzle:
# #     for j in i:
# #         if j not in un:
# #             un.append(j)
# # print(un)

# # count=0
# # count1=0
# # count2=0
# # for i in range(len(random_puzzle)):
# #     for j in range(len(random_puzzle[i])):
# #         # print(random_puzzle[i][j],end=" ")
# #         if random_puzzle[0][j]!="#":
# #             random_puzzle[0][j]="#"
# #             count += 1
# #         elif random_puzzle[1][j]!="%":
# #             random_puzzle[1][j]="%"
# #             count1 += 1
# #         elif  random_puzzle[2][j]!="$":
# #             random_puzzle[2][j]="$"
# #             count2 += 1
# #         else:
# #             pass
            
# # print(random_puzzle)
# # print(count)
# # print(count1)
# # print(count2)
# # print("total count is",count+count1+count2)

                          


