import re 

regex_one = re.compile(r'\d\d\d-\d\d\d-\d\d\d')
regex_two = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
regex_three = re.compile(r'\w\w\w\w\W')

match_object_one = regex_one.findall('Cell: 454-545-5454 Work: 998-989-8989')
match_object_two = regex_two.search('Cell: 454-545-5454 Work: 998-989-8989')
match_object_three = regex_two.findall('Cell: 454-545-5454 Work: 998-989-8989')
match_object_four = regex_three.findall('Cell: 454-545-5454 Work: 998-989-8989')

print(match_object_one)
print(match_object_two.group())
print(match_object_three)
print(match_object_four)