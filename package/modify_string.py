"""
This script modifies the string into desirable formatting
"""
def modify_string(string, integer):
    """manipulates string to achieve desirable formatting"""
    string_size = len(string)
    if string_size > 20:
        #Don't perform operation if string length is greater than 20
        return ''
    else:
        #Else perform formatting
        #capitalize string if in lowercase
        if string.islower():
            string = string.upper()
        length_difference = abs(integer - string_size)

        if string_size < integer:
            new_string = string + 'S' * length_difference
        elif string_size > integer:
            new_string = string[:integer]
        else:
            new_string = string
        return new_string
