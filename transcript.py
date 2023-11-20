import random
input1 = open("catlogue_database/username.txt", "r")
output = open("catlogue_database/cameron.txt", 'w')

for i in input1:
    output.write(i.rstrip() + str(random.randint(1980, 2021)) + "-" + str(random.randint(1, 12)) + '\n')
