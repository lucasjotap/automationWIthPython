import re 

regex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')
match_object = regex.findall('Cell: 454-545-5454 Work: 998-989-8989')
match_object_two = regex.search('Cell: 454-545-5454 Work: 998-989-8989')

print(match_object)
print(match_object_two.group())