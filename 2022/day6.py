with open('input/6.txt', 'r') as file:
    packet = file.read()


def solution(part):
    marker = ""

    for x, letter in enumerate(packet):

        if not letter in marker:
            marker += letter

        else:
            index = marker.find(letter)
            marker = marker[index + 1:] + letter

        match part:
            case 1:
                if len(marker) == 4:
                    return x + 1
            case 2:
                if len(marker) == 14:
                    return x + 1

def main():
    
    # if you want part 2 change the value.
    print(f"Answer: {solution(2)}")


if __name__ == "__main__":
    main()