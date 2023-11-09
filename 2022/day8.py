with open('input/8.txt', 'r') as file:
    trees_file = [line.strip() for line in file.readlines()]

def solution1(trees, x_y, direct):

    nums = list()

    for y, row in enumerate(trees):

        for x, num in enumerate(row):

            num = int(num)

            match direct:

                case "row":
                    location = f"{x}-{y}"

                case "row-reverse":
                    location = f"{len(trees) - 1 - x}-{y}"

                case "column":
                    location = f"{y}-{x}"

                case "column-reverse":
                    location = f"{y}-{len(trees) - 1 - x}"

            if x == 0:
                nums.append(num)
                if not location in x_y:
                    x_y.append(location)
                continue

            if num > nums[-1]:
                nums.append(num)
                if not location in x_y:
                    x_y.append(location)

        nums = []
    
    return x_y


def main():
    x_y = list()

    row_trees = trees_file
    row_reverse_trees = [row[::-1] for row in row_trees]

    column_trees = list()
    for y in range(len(row_trees[0])):
        num = ""
        for x in range(len(row_trees)):
             num += row_trees[x][y]
        column_trees.append(num)

    column_reverse_trees = [row[::-1] for row in column_trees]

    # count for left-right trees
    x_y = solution1(row_trees, x_y, "row")

    # count for right-left trees
    x_y = solution1(row_reverse_trees, x_y, "row-reverse")
        
    # count for top-bottom trees
    x_y = solution1(column_trees, x_y, "column")

    # count for bottom-top trees
    x_y = solution1(column_reverse_trees, x_y, "column-reverse")
    
    print(f"Answer 1: {len(x_y)}")


if __name__ == "__main__":
    main()