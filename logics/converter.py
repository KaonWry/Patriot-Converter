unit_factors = {
    'length': {
        'inch' : 1,
        'feet': 12,
        'yard': 36,
        'mile': 63360,
        'banana': 6, 
        'football field': 360*12,  
        'basketball court': 1128, 
        'Washington Monument': 6660,  
        'dollar bill': 6.14,  
        'semi truck': 840,  
        'bald eagle': 79.2,  
        'Empire State Building': 17448,  
        'M4 carbine': 33,  
        'Grand Canyon': 63360
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
        'bathtub': 61440,
        'teardrop': 0.25,
        'olympic swimming pool': 5068800000,
        'water drop': 0.001
        },
    
    'weight': {
        'grain': 1,
        'pound': 7000,
        'stone': 98000,
        'ton': 14000000,
        'long ton': 15680000,
        'paperclip': 15.4,  
        'penny': 38.5, 
        'dollar bill': 15.4,  
        'semi truck': 907184, 
        'football': 6538, 
        'big mac': 448, 
        'banana': 154,  
        'house cat': 150000, 
        'elephant': 181437600
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