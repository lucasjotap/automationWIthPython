import re

regex = re.compile('@gmail.com')
matchObject = regex.search('My e-mail is batwoman@gmail.com')
print(f'Found in e-mail address {matchObject.group()}')
