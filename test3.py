a=[ [0,0,0,1,1,1,0,0,0],
    [1,0,1,0,1,1,5,6,7],
    [7,7,7,9,9,9,0,0,0],
    [0,0,0,1,1,5,0,0,7],
    [1,2,3,4,5,6,7,8,9],
    [1,1,0,0,0,0,3,7,8],
    [7,7,7,6,7,0,0,0,8],
    [6,5,1,1,0,0,0,3,3],
    [1,1,4,0,0,0,2,2,2]
]

# for i in range(len(a)-2):
#     for j in range(len(a[i])-2):
#         print(a[i][j],end=' ')
#     print("")

final_arr=[]
count=0
sum_ans=0
for i in range(len(a)-2):
    for j in range(len(a[i])-2):
        ls_arr= [
        a[i][j],a[i][j+1],a[i][j+2],         #0  0  0
        a[i+1][j+1],                          #  0
        a[i+2][j],a[i+2][j+1],a[i+2][j+2]    #7  7  7
        ]
        # print(ls_sum)
        k=(sum(ls_arr))                       #21
        
        
        if k>sum_ans:
            final_arr=ls_arr
            sum_ans=k
            
print(final_arr)
print(sum_ans)

        
