import re
m = re.search(r'^([A-Z0-9]{2})(\d{1,4})$', 'NH105', re.I)
if m is None:
    print('Not match')
else:
    print(f'Airline: {m.group(1)}')
    print(f'Flight : {m.group(2)}')