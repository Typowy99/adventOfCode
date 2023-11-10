with open('input/8.txt', 'r') as file:
    trees_file = [line.strip() for line in file.readlines()]

def solution(direct, trees, x_y, scenic_score):

    visible_tree = list()

    for y, row in enumerate(trees):

        for x, tree in enumerate(row):

            match direct:

                case "row":
                    location = f"{x}-{y}"

                case "row-reverse":
                    location = f"{len(trees) - 1 - x}-{y}"

                case "column":
                    location = f"{y}-{x}"

                case "column-reverse":
                    location = f"{y}-{len(trees) - 1 - x}"

            # ------ part 1 ------ #
            tree = int(tree)

            if x == 0 or tree > visible_tree[-1]:
                visible_tree.append(tree)
                if location not in x_y:
                    x_y.append(location)
        
            # ------ part 2 ------#  
            count = 0

            for next_tree in range(x + 1, len(row)):
                
                count += 1
                # if blocked viev or taller tree or last tree
                if int(row[next_tree]) == tree or int(row[next_tree]) > tree or x == len(row) - 1:
                    break
            
            #add visible tree each side
            scenic_score[location] = scenic_score.get(location, 1) * count
            
        visible_tree = []
    
    return x_y, scenic_score


def main():

    x_y = list()
    scenic_score = dict()

    # count for left-right trees
    x_y, scenic_score = solution("row", trees_file, x_y, scenic_score)

    # count for right-left trees
    row_reverse_trees = [row[::-1] for row in trees_file]
    x_y, scenic_score = solution("row-reverse", row_reverse_trees, x_y, scenic_score)
        
    # count for top-bottom trees
    column_trees =  [''.join(row[x] for row in trees_file) for x in range(len(trees_file))]
    x_y, scenic_score = solution("column", column_trees, x_y, scenic_score)

    # count for bottom-top trees
    column_reverse_trees = [row[::-1] for row in column_trees]
    x_y, scenic_score = solution("column-reverse", column_reverse_trees, x_y, scenic_score)
    
    #answer
    print("Answer 1:", len(x_y))
    print("Answer 2:", max(scenic_score.values()))


if __name__ == "__main__":
    main()