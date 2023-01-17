import re

regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_object = regex.findall('Cell: 415-555-9999 Work: 212-555-9000')
print(match_object)