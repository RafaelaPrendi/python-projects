#! python3
import re, pyperclip
'''
Get the text off the clipboard.
Find all phone numbers and email addresses in the text.
Paste them onto the clipboard.
'''
#  a regex for phone nr
phoneRegex = re.compile(r'''
    # 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
( 
((\d\d\d) | (\(\d\d\d\))) ?     # area code optional
(\s|-)              # first separator
\d\d\d              # first 3 digits
-                   # separator
\d\d\d\d            # last 4 digits
(((ext(\.)?\s) | x) # extension word part optional
(\d{2, 5})) ?       # extension number part optional 
 )
''', re.VERBOSE)

# a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+ # name part
@ # @ symbol
[a-zA-Z0-9_.+]+# domain name part
''', re.VERBOSE)

# get the text off the clipboard
text = pyperclip.paste()

# extract the email/phone from text in a list of strings
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# copy the extracted email/phone to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

# write result in a text file



