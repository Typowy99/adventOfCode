moves = []

stacks = {
    1: "NBDTVGZJ",
    2: "SRMDWPF",
    3: "VCRSZ",
    4: "RTJZPHG",
    5: "TCJNDZQF",
    6: "NVPWGSFM",
    7: "GCVBPQ",
    8: "ZBPN",
    9: "WPJ"
}

with open('input/5.txt', 'r') as file:
    for line in file:
        moves.append([int(s) for s in line.split() if s.isdigit()])


def solution(part):

    global stacks

    for move in moves:
        c = move[0]
        f = move[1]
        t = move[2]

        match part:
            case 1:
                stacks[t] = stacks[t] + stacks[f][-c:][::-1]
            case 2:
                stacks[t] = stacks[t] + stacks[f][-c:]
                stacks[f] = stacks[f][:-c]

    end_word = "".join(letter[-1] for letter in stacks.values())
    return end_word


def main():
    
    # if you want part 2 change the value.
    print(f"Answer: {solution(2)}")


if __name__ == "__main__":
    main()