length_factor = {
    'inch' : 1,
    'feet': 12,
    'yard': 36,
    'mile': 63360
}

volume_factors = {
    'teaspoon': 1,
    'tablespoon': 3,
    'fluid ounce': 6,
    'cup': 48,
    'pint': 96,
    'gallon': 768,
    'barrel': 32256
}

weight_factors = {
    'grain': 1,
    'pound': 7000,
    'stone': 98000,
    'ton': 14000000,
    'long ton': 15680000
}

def convert_unit(unit_type, amount, unit_from, unit_to):
    match unit_type:
        case 'length':
            factors = length_factor
        case 'volume':
            factors = volume_factors
        case 'weight':
            factors = weight_factors
            
    converted = amount * (factors[unit_from]/factors[unit_to])
    
    txt_result = f'{amount} {unit_from} is equal to {converted} {unit_to}'
    print(txt_result)
    return txt_result
    
def convert_all_unit(unit_type, amount, unit):
    match unit_type:
        case 'length':
            factors = length_factor
        case 'volume':
            factors = volume_factors
        case 'weight':
            factors = weight_factors
        # case _:
        #     raise ValueError("Invalid unit type")
            
    results = []
    for unit_to, factor in factors.items():
        if unit != unit_to:
            converted = amount * (factors[unit]/factor)
            results.append(f'{converted} {unit_to}')
        
    txt_result = '\n'.join(map(str, results))
    print(txt_result)
    return txt_result