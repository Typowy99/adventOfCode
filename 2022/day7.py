with open('input/7.txt', 'r') as file:
    commands = [line.strip() for line in file.readlines()]


def create_file_system(file_system, file_path, file):

    directory = "-".join(file_path)
    file_system[directory] = file_system.get(directory, []) + [file]

    return file_system


def replace_file(file_system):
    
    sorted_file_system = dict(sorted(file_system.items(), reverse=True))
    
    for key,value in sorted_file_system.items():
        for folder in value:
            if folder.startswith("dir"):
                name = key + f'-{folder[4:]}'
                file_system[key] = file_system.get(key) + file_system.get(name)

    return file_system 


def replace_to_size(file_system):

    new_file_system = dict()
    for key,value in file_system.items():
        for folder in value:
            size = folder.split()[0]
            if size.isnumeric():
                new_file_system[key] = new_file_system.get(key, 0) + int(size)

    return new_file_system


def main():

    file_path = ['/']
    file_system = {}

    for com in commands:

        if com.startswith("$ cd /"):
            file_path = ['/']
            continue

        elif com.startswith("$ cd .."):
            file_path.pop()
            continue

        elif com.startswith("$ cd"):
            name = com.split()[2]
            file_path.append(name)
            continue

        elif com.startswith("$ ls"):
            continue
        
        file_system = create_file_system(file_system, file_path, com)


    file_system = replace_file(file_system)

    file_system = replace_to_size(file_system)

    suma = 0
    list_1 = []
    free_space = 30000000 - (70000000 - file_system['/'])

    for key, value in file_system.items():
        if value <= 100000:
            suma += value

        if value >= free_space:
            list_1.append(value)
    
    print(f"Answer 1: {suma}")
    print(f"Answer 2: {min(list_1)}")


if __name__ == "__main__":
    main()