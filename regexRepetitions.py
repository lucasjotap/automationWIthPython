import re

haRegex = re.compile(r'(Ha){3}')
matchObject = haRegex.search('HaHaHa')
print(matchObject.group())

matchObjectTwo = haRegex.search('Ha')
if matchObjectTwo == None:
    print('No pattern found.')
