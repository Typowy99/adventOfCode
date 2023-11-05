backpack_list = []
num = 0
three_backpack = 0

with open("txt/1.txt", "r") as file:

    for line in file.readlines():
        if len(line) > 1:
            num += int(line.strip())
        else:
            # add backpack
            backpack_list.append(num)
            num = 0

# biggest backpack
print(max(backpack_list))

# biggest 3 backpack
backpack_list.sort()
print(sum(backpack_list[-3:]))


        


