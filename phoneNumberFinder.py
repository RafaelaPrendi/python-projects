import re
def findPhoneNumber(text):#regex style
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')#create the pattern
    #mo = phoneNumRegex.search(text)#search for it, it returns a match object
    mo = phoneNumRegex.findall(text) #find all occurences, it returns a list of strings
    print(mo)#print the found number

def isPhoneNumber(text):#4150-555-1010
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True
#message = input()
message = ' call me in 415-555-1010 or in my office line number at 415-555-9999 . Goodbye!'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ', chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone number')

#using verbose
re.compile(r"""
(\d\d\d) | # area code
(\(\d\d\d\)) # or with actual parenthesis , no dash
\d\d\d # first 3 digits
-
\d\d\d\d# last 4 digits
\sx\d{2,4} # extension like x1234
""", re.VERBOSE | re.DOTALL | re.IGNORECASE)

#with regex
findPhoneNumber(message)