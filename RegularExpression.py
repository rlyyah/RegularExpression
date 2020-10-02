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


# Roman Numerals

'''
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''

# Checking for Thousands

pattern = '^M?M?M?$'
result = re.search(pattern, 'M')
print(result)
result = re.search(pattern, 'MM')
print(result)
result = re.search(pattern, 'MMM')
print(result)
result = re.search(pattern, 'MMMM')
print(result)
result = re.search(pattern, '')
print(result)

# Checking for Hundreds
print()

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
result = re.search(pattern, 'MCM')
print(result)
result = re.search(pattern, 'MD')
print(result)
result = re.search(pattern, 'MMMCCC')
print(result)
result = re.search(pattern, 'MMMCCC')
print(result)
result = re.search(pattern, 'MCMC')
print(result)
result = re.search(pattern, '')
print(result)

# Using {n,m} Syntax
print()

pattern = "^M{0,3}$"
result = re.search(pattern, 'M')
print(result)
result = re.search(pattern, 'MM')
print(result)
result = re.search(pattern, 'MMM')
print(result)
result = re.search(pattern, 'MMMM')
print(result)
result = re.search(pattern, '')
print(result)

# Checking for Tens and Ones
print()

pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
result = re.search(pattern, 'MCMXL')
print(result)
result = re.search(pattern, 'MCML')
print(result)
result = re.search(pattern, 'MCMLX')
print(result)
result = re.search(pattern, 'MCMLXXX')
print(result)
result = re.search(pattern, 'MMLXXXX')
print(result)
