# Write your solution for algorithm 4 below
#Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. The comparison should be case-insensitive.
#Sample input: 'I love software engineering'
#Sample output: ['engineering', 'I', 'love', 'software']

sample_string = "I love software engineering"

sorted_strings = sorted(sample_string.split(), key = str.lower)
print(sorted_strings)