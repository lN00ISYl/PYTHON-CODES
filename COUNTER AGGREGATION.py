from collections import Counter
import random


student_list = [" Jorose ", " Louise ", " Daniel ", " Victoria ", 
                " R-Mia ", " Paul ", " Vincent "," Jasper ", " Kristine ", " Kyran ", " Dirk ", " Arcel "]
#manual version
dict = {}

for student in student_list:
    if student not in dict:
        dict[student] = 0
    dict[student] += 1
print(dict) 

#counter version with 100 random choices
randomizer = random.choices(student_list, k=100)

counter= Counter(randomizer)
print(counter)


#counter version with getting how many in the list are there
ran = Counter(student_list)
print(ran)


# adding some thing in the dictionary or list 
ran.update(["Karlos","shania","dirk"])
print(ran)