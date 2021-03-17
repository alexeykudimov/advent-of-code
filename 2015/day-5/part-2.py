with open('input', 'r') as input_file:
    input_data = input_file.read()


def non_overlapping_pair(string):
    for pos, ch in enumerate(string[:-2]):
        if f'{ch}{string[pos+1]}' in string[pos+2:]:
            found = True
            break
    else:
        found = False

    return found


def pair_with_letter_between(string):
    return any([string[pos+2] == ch for pos, ch in enumerate(string[:-2])])


def nicer_string(string):
    return non_overlapping_pair(string) and pair_with_letter_between(string)


def total_nicer_strings(data):
    return sum([nicer_string(string) for string in data.split()])


print(total_nicer_strings(input_data))
