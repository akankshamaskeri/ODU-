import random
min = 1
max = 6
x=0
y=0
sum=0
m=0
n=0
roll_again = "yes"
m=input("m")
n=input("n")

while (roll_again == "yes" or roll_again == "y") and sum!=m*n:
    print "Rolling the die"
    print "The value is"
    dice=random.randint(min,max)
    if sum+dice<=m*n:
        sum=sum+dice
    roll_again = raw_input("Roll the die again?")
    x=sum%m
    y=sum/m
    if y%2==1:
     x=m-x-1
      
    print (dice)
    print(x)
    print(y)
    print(sum)
