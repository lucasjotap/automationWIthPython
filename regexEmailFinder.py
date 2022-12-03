import re

regex = re.compile(r'@gmail.com')
matchObject = regex.search('My e-mail is batwoman@gmail.com')
print(f'Found in e-mail address {matchObject.group()}')
