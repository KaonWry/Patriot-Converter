# Dictionary for unit factors, all compared to inch
unit_factor = {
    'inch': 1,
    'feet': 12,
    'yard': 36,
    'mile': 63360
}
unit_names = list(unit_factor.keys())

# Get unit name for unit needing for conversion
def get_conversion_unit():
    while True:
        unit = str(input(f'What unit({', '.join(map(str, unit_names))}): '))
        if unit in unit_names:
            return unit
        else:
            print ('erm what the sigma?')

# Get amount of unit need to be converted
def get_conversion_amount():
    while True:
        amount = float(input("How many: "))
        if amount >= 0:
            return amount
        else:
            print('bruh...')

# Where the real conversion takes place 
conversion_unit = get_conversion_unit()
conversion_ammount = get_conversion_amount()
def convert_unit(unit, amount):
    print(f'Converting {amount} {unit} to other units:')
    for unit_to, factor in unit_factor.items():
        converted = amount * (unit_factor[unit]/factor)
        print(f'{converted:.6f} {unit_to}')
        
convert_unit(conversion_unit, conversion_ammount)