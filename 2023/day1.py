import re
from typing import List, Dict


def read_file(file_path: str) -> List[str]:
    """
    Reads a file and returns its lines as a list of strings.

    :param file_path: Path to the file to be read.
    :return: List of lines in the file.
    """
    with open(file_path, "r") as file:
        return file.readlines()


def extract_numbers(line: str, number_words: List[str]) -> Dict[int, int]:
    """
    Extracts numbers from a line of text, both as digits and words.

    :param line: A line of text to extract numbers from.
    :param number_words: List of number words like "one", "two", etc.
    :return: A dictionary with positions of numbers and their corresponding integer values.
    """
    digit_numbers = {index: int(char) for index, char in enumerate(line) if char.isdigit()}

    for index, word in enumerate(number_words):
        for match in re.finditer(word, line):
            digit_numbers[match.start()] = index + 1

    return digit_numbers


def process_lines(lines: List[str], number_words: List[str]) -> List[Dict[int, int]]:
    """
    Processes a list of lines, extracting numbers from each line.

    :param lines: List of lines to process.
    :param number_words: List of number words to recognize.
    :return: A list of dictionaries, each representing the numbers found in a line.
    """
    line_numbers = []
    for line in lines:
        nums_in_line = extract_numbers(line, number_words)
        line_numbers.append(nums_in_line)
    return line_numbers


def calculate_sum(line_numbers: List[Dict[int, int]]) -> int:
    """
    Calculates a sum based on the extracted numbers from each line.

    :param line_numbers: List of dictionaries, each containing numbers extracted from a line.
    :return: The calculated sum.
    """
    total_sum = 0
    for numbers in line_numbers:
        if numbers:
            num_max = max(numbers)
            num_min = min(numbers)
            combined_number = str(numbers[num_min]) + str(numbers[num_max])
            total_sum += int(combined_number)
    return total_sum


# Main execution
number_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
file_lines = read_file("input/1.txt")
numbers_per_line = process_lines(file_lines, number_words)
total_sum = calculate_sum(numbers_per_line)

print(total_sum)
