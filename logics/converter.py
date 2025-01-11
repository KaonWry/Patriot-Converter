unit_factors = {
    'length': {
        'inch' : 1,
        'feet': 12,
        'yard': 36,
        'mile': 63360,
        'banana': 6, 
        'football field': 360*12,  
        'basketball court': 94*12, 
        'Washington Monument': 6660,  
        'dollar bill': 6.14,  
        'semi truck': 75*12,  
        'bald eagle': 79,  
        'Empire State Building': 1454*12,  
        'M4 carbine': 33,  
        'Grand Canyon': 6000*12
        },
    
    'volume': {
        'teaspoon': 1,
        'tablespoon': 3,
        'fluid ounce': 6,
        'cup': 48,
        'pint': 96,
        'gallon': 768,
        'barrel': 32256,
        'shot': 9,
        'bathtub': 80*768,
        'olympic swimming pool': 660430*768,
        'water drop': 0.001
        },
    
    'weight': {
        'grain': 1,
        'pound': 7000,
        'stone': 98000,
        'ton': 14000000,
        'long ton': 15430000,
        'paperclip': 15.4,  
        'penny': 24, 
        'dollar bill': 15.4,  
        'semi truck': 280000000, 
        'football': 15*7000, 
        'big mac': 3395, 
        'banana': 1559,  
        'house cat': 63000, 
        'elephant': 92594000
        },
}

def get_units(unit_type):
    return list(unit_factors[unit_type].keys())

def format_number(number):
    if number == int(number):
        return str(int(number))
    return f'{number:.10f}'.rstrip('0').rstrip('.')

def convert_unit(unit_type, amount, unit_from, unit_to):
    factors = unit_factors[unit_type]
    converted = amount * (factors[unit_from]/factors[unit_to])
    
    txt_result = f'{format_number(amount)} {unit_from} is equal to {format_number(converted)} {unit_to}'
    print(txt_result)
    return txt_result
    
def convert_all_unit(unit_type, amount, unit):
    factors = unit_factors[unit_type]
    results = []
    for unit_to, factor in factors.items():
        if unit != unit_to:
            converted = amount * (factors[unit]/factor)
            results.append(f'{format_number(converted)} {unit_to}')
        
    txt_result = '\n'.join(map(str, results))
    print(txt_result)
    return txt_result