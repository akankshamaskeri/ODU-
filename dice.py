import random
min = 1
max = 6
x=0
y=0
sum=0
roll_again = "yes"

while (roll_again == "yes" or roll_again == "y") and sum!=64:
    print "Rolling the die"
    print "The value is"
    dice=random.randint(min,max)
    if sum+dice<=64:
        sum=sum+dice
    roll_again = raw_input("Roll the die again?")
    x=sum%8
    y=sum/8
    if y%2==1:
      x=7-x
      
    print (dice)
    print(x)
    print(y)
    print(sum)