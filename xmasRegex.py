import re 

regex = re.compile(r'\d+\s\w+')
match_object = regex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge")
print(match_object)

vowel_regex = re.compile(r'[aeiouAEIOU]')
match_object_two = vowel_regex.findall("RoboCop eats baby food. BABY FOOD")
print(match_object_two)