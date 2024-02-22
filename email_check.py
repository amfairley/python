# import regular expression library
import re

email = input("What is your email? ".strip())
# Option 1
# r": start of a raw string, allows the \ escape character
# ^ : carrot denoting starts with [^@]+
# [^@]+: 1 or more characters that are not an @ symbol
# @: then an @ symbole
# [^@]+: 1 or more characters that are not an @ symbol
#\.edu$: ends with .edu the \ allows the . to not mean "any character"
if re.search(r"^[^@]+@[^@]+\.edu$", email):
# Option 2
# r" Start of raw string allowing escape character
# ^\w+ start with 1 or more any alphanumberic or _ character
# @ then an at symbol
# (\w+\.)? then 0 or 1 (?) uses of 1 or more alphanumeric or _ character followed by a dot
# The above allows for a sub domain
# ? is 0 or 1, * is 0 or more
#\.edu$ ends with .edu
# re.IGNORECASE ignores case sensitivity of input
# if re.search(r"^\w+@(\w+\.)?\w+\.edu$, email, re.IGNORECASE):
# regular expression that browsers currently use to check for an email address
#   ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+
#   @
#   (?:[a-zA-Z0-9-]{0, 61}[a-zA-Z0-9])?
#   (?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
    print("Valid")
else:
    print("Invalid")