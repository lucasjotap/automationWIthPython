import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
search = phoneNumRegex.search('My number is (454) 555-5452.')
# areaCode, mainNumber = search.groups()
# print(f'Phone number found: {search.group()}')
print(search.group(1))
# print(search.group(0))
print(search.group(2))
# print(search.group())
# print(search.groups())
# print(areaCode)
# print(mainNumber)