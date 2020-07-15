"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c

def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_c = (temperature_c * (9/5)) + 32
    return temperature_c

## CREATE THE ADDITIONAL FUNCTIONS BELOW

def convert_c_to_k(temperature_c):
    temperature_k = temperature_c + 273.15
    return temperature_k

def convert_f_to_k (temperature_f):
    temperature_k = ((temperature_f - 32) * (5/9)) + 273.15
    return temperature_k

def convert_k_to_c (temperature_k):
    temperature_c = temperature_k - 273.15
    return temperature_c

def convert_k_to_f (temperature_k):
    temperature_f = ((temperature_k - 273.15) * (9/5)) + 32
    return temperature_f

## LEVEL UP

def convert_f_to_all(temperature_f):
    temp_c = convert_c_to_f(temperature_f)
    temp_k = convert_f_to_k(temperature_f)
    print(f'{temperature_f} degrees F is:')
    print(f'{temp_c} degrees C')
    print(f'{temp_k} degrees K')
        
def convert_f_to_all_level_up(temp_f):
    import pandas as pd
    temp_dict = {'C': convert_f_to_c(temp_f), 'K': convert_f_to_k(temp_f)}
    return pd.DataFrame(temp_dict, index=[f'{temp_f} F =']).round(2)