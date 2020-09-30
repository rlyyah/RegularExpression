'''
Regular expressions are a powerful and (mostly) standardized way of 
searching, replacing, and parsing text with complex patterns of characters.
'''

'''
"$" - at the end od the string
'''

import re


# Street Adresses

street_adress = '100 NORTH BROAD ROAD'
street_adress = street_adress.replace('ROAD', 'RD.')

print(street_adress)

street_adress = '100 NORTH BROAD ROAD'
street_adress = re.sub('ROAD$', 'RD.', street_adress)
print(street_adress)

