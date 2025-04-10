import os
import json

from lecture_searching.generators import ordered_sequence

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    allowed_fields = {"unordered_numbers", "ordered_numbers", "dna_sequence"}
    if field not in allowed_fields:
        return None

    with open(file_path, mode="r") as file:
        data = json.load(file)
    return data[field]



def linear_seach(sekvence, hledane_cislo):
    positions = []
    for i, val in enumerate(sekvence):
        if val == hledane_cislo:
            positions.append(i)
    numbers_dict = {"positions":positions, "count":len(positions)}
    return numbers_dict


def pattern_search(sekvence, vzor):
    indexy = set()
    delka_sekvence = len(sekvence)
    delka_vzoru = len(vzor)
    for i in range(delka_sekvence - delka_vzoru + 1):
        if sekvence[i:i+delka_vzoru] == vzor:
            indexy.add(i)
    return indexy


def binary_search(numbers, num):
    left = 0
    right = len(numbers) - 1
    while left < right:
        half = (left + right) // 2
        if numbers[half] == num:
            return half
        elif numbers[half] > num:
            right = half - 1
        elif numbers[half] < num:
            left = half + 1
    return None

def main():
    numbers = read_data("sequential.json", "unordered_numbers")
    print(numbers)
    serazeny = read_data("sequential.json", "ordered_numbers")
    numbers_dict = linear_seach(numbers, 9)
    print(numbers_dict)
    sekvence = read_data("sequential.json", "dna_sequence")
    indexy = pattern_search(sekvence, "ATA")
    print(indexy)
    pulkovani = binary_search(serazeny, 102)
    print(pulkovani)



if __name__ == '__main__':
    main()