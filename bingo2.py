import random
min=1
max=6
x=0
y=0
sum=0
m=0
n=0


roll_again="yes"
m=input("m")
n=input("n")

array=[[False for x in range(m)]for y in range(n)]
    
def cross():   
    for i in range(0,m):
        cookie=True
        for j in range(0,n):
            if (array[j][i]==False):
                cookie=False
                
        if(cookie):
            print "bingo"
            return False
        
       
        
        for i in range(0,n):
            cookie=True
            for j in range(0,m):
                if(array[i][j]==False):
                    cookie=False
                    
            if(cookie):
                print "bingo"
                return False
                
    return True
while (roll_again == "yes" or roll_again == "y") and cross(): 
    print "Rolling the die"
    print "The value is"
    dice=random.randint(min,max)
    if sum+dice<=m*n:
        sum=sum+dice
    else:
        sum=sum+dice-m*n
    roll_again = raw_input("Roll the die again?")
    x=(sum-1)%m
    y=(sum-1)/m
    if y%2==1:
        x=m-x-1
    array[y][x]=True 
    for i in range(n):
        print array[i]
    print (dice)
    print(x)
    print(y)
    print(sum)
    
    
