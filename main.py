# Dictionary for unit factors, all compared to inch
unit_factor = {
    'inch': 1,
    'feet': 12,
    'yard': 36,
    'mile': 63360
}
unit_names = list(unit_factor.keys())

# Get unit name for unit needing for conversion
while True:
    unit_from = str(input(f'What unit({', '.join(map(str, unit_names))}): '))
    if unit_from in unit_names:
        break
    else:
        print ('erm what the sigma?')

# Get amount of unit need to be converted
while True:
    amount = float(input("How many: "))
    if amount >= 0:
        break
    else:
        print('bruh...')

# Where the real conversion takes place 
print(f'Converting {amount} {unit_from} to other units:')
for unit_to, factor in unit_factor.items():
    converted = amount * (unit_factor[unit_from]/factor)
    print(f'{converted:.6f} {unit_to}')