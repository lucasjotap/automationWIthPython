def isPhoneNumber(var):
    if len(var) != 12:
        return False
    for i in range(0, 3):
        if not var[i].isdecimal():
            return False
    if var[3] != '-':
        return False
    for i in range(4, 7):
        if not var[i].isdecimal():
            return False
    if var[7] != '-':
        return False
    for i in range (8, 12):
        if not var[i].isdecimal():
            return False
    return True

x = '444-555-5555'
y = isPhoneNumber(x)

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print(f"Phone number found {chunk}")
print("Search done!")