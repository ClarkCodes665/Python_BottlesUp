#Bottles Up by: Crystal Clark | CSIT 111 | CLW

#This program calculates the number of bottles that 
#have been collected over the course of one week. 

#Initialize the starting value.

addedUp = 0
 
#Display the number of bottles collected per day.
for bottles in range(1):
    bottles = int(input('Day 1: How many bottles have you collected today? '))
    bottles = int(input('Day 2: How many bottles have you collected today? '))
    bottles = int(input('Day 3: How many bottles have you collected today? '))
    bottles = int(input('Day 4: How many bottles have you collected today? '))
    bottles = int(input('Day 5: How many bottles have you collected today? '))
    bottles = int(input('Day 6: How many bottles have you collected today? '))
    bottles = int(input('Day 7: How many bottles have you collected today? '))
    addedUp = addedUp + bottles    
#end for

#Display the number of bottles collected over the course of 7 days.
if addedUp > 7 and addedUp <= 49:
    print("Sweet!! You're on a roll with",addedUp,"bottles recycled this week.")
elif addedUp > 50:
    print('Incredible! Look at you, recycling',addedUp,'bottles this week!')
elif addedUp <= 7 and addedUp > 0:
    print("You've recycled",addedUp,"bottles this week. That's a good start, keep it up!")
elif addedUp == 0:
    print("Recycling is important! Let's start collecting!!")
#end if
  


#Using floor division, divide the negative number of hotdogs needed by 10,then
    #negate the resulting value. This will then round the number of hotdog packages
    #up to the nearest whole number. 
