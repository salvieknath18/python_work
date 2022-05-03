import json
import os

if os.path.exists(os.path.abspath('bookingdata.json')):
    booking_data = json.load(open('bookingdata.json'))
else:
    booking_data = {
        'ACSL':
            {'available': [l+str(n) for l in "ABCDE" for n in range(1, 4)],
             'booked': []},
        'NACSL':
            {'available': [l+str(n) for l in "ABCDE" for n in range(1, 4)],
             'booked': []},
        'ACSE':
            {'available': [str(i) for i in range(1, 26)],
             'booked': []},
        'NACSE':
            {'available': [str(i) for i in range(1, 26)],
             'booked': []},
    }
    # json.dump(booking_data, open('bookingdata.json','w'))
print(booking_data)

print("************Welcome to ticket booking system****************")
print("Please choose option from following: ")
print("""
    1. AC-Sleeper
    2. NonAC-Sleeper
    3. AC-Seater
    4. NonAC-Seater
""")
binp = int(input())
map = {1: 'ACSL', 2: 'NACSL', 3: 'ACSE', 4: 'NACSE'}
avail = booking_data[map[binp]]['available']
print(f"The available seats are : {avail}")
print("choose one of the seat from above")
sinp = input()
booking_data[map[binp]]['booked'].append(avail.pop(avail.index(sinp)))
json.dump(booking_data, open('bookingdata.json','w'), indent=4)

