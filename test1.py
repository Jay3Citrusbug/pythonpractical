from random import randrange

fruits=['apples','oranges','bananas','mangoes','grapes','strawberry','Pineapple','Melon','Avocado','Kiwi']

print(len(fruits))
man=list()
com=[]
score=0

for i in range(0,len(fruits)):
 
    rf=randrange(0,len(fruits)-1)  #0-9 ma koi pan number
    length = len(fruits[rf])//2  #apple aave to aeni length divide by 2
    que = fruits[rf][0:length]  #[0:3]=app
    print("here is your queston", i+1, que, "...")  #app....
    ans=input("fill the word :")
    
    final=que+ans
    if final in fruits:
        score = score+1
        com.append('{}'.format('|'))
        
        if i==9:
          com.pop()
          com.append('{}'.format('--------------------'))
      
            
          for h in com: 
            print(h) 
            
    else:
     if final not in fruits:
        if i<5:
          man.append('{}  {}'.format('|','|'))
          
        if i==5:
            man.append('{}  {}'.format('|','0'))
        elif i==6:
          man.append('{}  {}'.format('|','-'))
        elif i==7:
          man.pop()
          man.append('{}  {}{}'.format('|','-','|'))
        elif i==8:
          man.pop()
          man.append('{}  {}{}{}'.format('|','-','|','-'))
        elif i==9:
         
          man.append('{}   {}'.format('|','/\\'))
          
        for r in man:
          print(r)
   
else:
      print("Game is finish")
      print("your score is",score)


