'''
Regular expressions are a powerful and (mostly) standardized way of 
searching, replacing, and parsing text with complex patterns of characters.
PROTIP:
I recommend always using raw strings when dealing with regular expressions
'''

'''
"...$" - at the end od the string
"^..." - at the beginning of the string
"\b..." - a word boundary must occur here
r"..." - makes string "RAW" so nothing in this string should be escaped
'''

import re


# Street Adresses

street_adress = '100 NORTH BROAD ROAD'
street_adress = street_adress.replace('ROAD', 'RD.')

print(street_adress)

street_adress = '100 NORTH BROAD ROAD'
street_adress = re.sub('ROAD$', 'RD.', street_adress)
print(street_adress)

street_adresses = ['100 BROAD','100 BROAD ROAD APT. 3']
fixed_street_adresses = []
for name in street_adresses:
    fixed_street_adresses.append(re.sub(r'\bROAD\b', 'RD.', name))

print(fixed_street_adresses)




