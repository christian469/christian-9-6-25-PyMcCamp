# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
print("hello from day4")

#recap
import random 

for count in range(10):
    randomnumber = random.randint(1, 200)
    print(randomnumber)

########################################################################
# Task 1:


counter = 0
while counter < 5:
    print(counter)
    counter = counter + 1

########################################################################
# Task 2:
question =  "A woman, while at the funeral of her sister met a guy. She and this guy just clicked and she fell in love then and there. However, she got distracted and did not get his number and could not find him. A week later she murdered her brother. Why did she murder her brother?"
hidden_answer = 'The woman murdered her brother because she wanted the new guy to come to her brother'
guess= input( question )
while guess !=hidden_answer:
    print
########################################################################
# Additional exercises: