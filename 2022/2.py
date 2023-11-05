y1 = {'X': 1, 'Y': 2, 'Z': 3}
x1 = {'A': 1, 'B': 2, 'C': 3}

win = {'A': 2, 'B': 3, 'C': 1}
lose = {'A': 3, 'B': 1, 'C': 2}

with open('2.txt', 'r') as file:
    moves = [line.split() for line in file.readlines()]
        

def solution1():
    pkt = 0
    for line in moves:

        x = x1[line[0]]
        y = y1[line[1]]

        match y - x:
            case 1 | -2:
                pkt += 6 + y
            case -1 | 2:
                pkt += y
            case 0:
                pkt += 3 + y       
    return pkt


def solution2():
    pkt = 0
    for line in moves:
        match line[1]:
            case 'X':
                # lose
                pkt += lose[line[0]]
            case 'Y':
                # draw
                pkt += 3 + x1[line[0]]
            case 'Z':
                #win
                pkt += 6 + win[line[0]]    
    return pkt


print(f"Answer 1: {solution1()}")
print(f"Answer 2: {solution2()}")
