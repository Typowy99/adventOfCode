with open('4.txt', 'r') as file:
    pairs = [line.strip().split(",") for line in file.readlines()]


def contain_other(pair1, pair2):
    
    start, end = 0, 1
    if pair1[start] <= pair2[start] and pair1[end] >= pair2[end]:
        return True

    if pair2[start] <= pair1[start] and pair2[end] >= pair1[end]:
        return True
    return False


def overlaps(pair1, pair2):

    start, end = 0, 1
    if pair1[end] >= pair2[start] and pair1[start] <= pair2[end]:
        return True
    return False



def solution(num):
    pkt = 0
    for pair in pairs:
        pair1 = list(map(int, pair[0].split("-")))
        pair2 = list(map(int, pair[1].split("-")))
        
        match num:
            case 1:
                if contain_other(pair1, pair2):
                    pkt += 1
            case 2:
                if overlaps(pair1, pair2):
                    pkt += 1
    return pkt


print(f"Answer 1: {solution(1)}")
print(f"Answer 2: {solution(2)}")