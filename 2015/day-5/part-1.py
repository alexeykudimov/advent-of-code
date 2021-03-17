with open('input', 'r') as input_file:
    input_data = input_file.read()

from string import ascii_lowercase as alphabet
disallowed_strings = ['ab', 'cd', 'pq', 'xy']
vowels = 'aeiou'


def vowels_count(string):
    return len([char for char in string if char in vowels])


def double_chars(string):
    return any([char*2 in string for char in alphabet])


def disallowed_patterns(string):
    return any([pattern in string for pattern in disallowed_strings])


def nice_string(string):
    return all([vowels_count(string) >= 3,
               double_chars(string),
               not disallowed_patterns(string)])


def total_nice_strings(data):
    return sum([nice_string(string) for string in data.split()])


print(total_nice_strings(input_data))
