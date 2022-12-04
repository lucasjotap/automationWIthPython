import re

# Without the question mark the regex becomes greedy.
greedyRegex = re.compile(r'(Ha){3,5}')
matchObject = greedyRegex.search('HaHaHaHaHa')
print(matchObject.group())

# With the question mark the algorithm becomes non-greedy.
nonGreedyRegex = re.compile(r'(Ha){3,5}?')
matchObjectTwo = nonGreedyRegex.search('HaHaHaHaHa')
print(matchObjectTwo.group())

