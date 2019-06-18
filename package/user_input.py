#This method get user specified code of form 'ssts'
"""
This script takes user input of code and list of integers
"""
def get_code():
    """input user-specified string of format s and t"""
    
    code = input("Enter the Code containing S and T: ").replace(' ', '')
    #Input acceptable only if it's of form 'sst' and length > 1 and < 20
    while not ({'s', 't'} <= set(code)) or len(code) <= 1 or len(code) > 20:
        try:
            code = input("Enter the Code containing S and T [20 alphabets allowed]: ").replace(' ', '')
        except:
            print("Please enter a valid string conatining only S and T")
    return code.upper()

#This method checks if all input integers are positive integers and less than or equal to 20
def if_numbers_within_bounds(result):
    """check if all integers are positive and within allowed limit i.e. 20"""
    for number in result:
        if number < 1 or number > 20:
            return False
    return True

#This method get integers input
def get_integers():
    """input all integers"""
    while True:
        try:
            integers = input("Enter number of integers [allowed range: 1-20] for Formating: ")
            result = [int(number) for number in integers.split()]
        except:
            print("Whoops! Enter only positive integers")
            continue
        else:
            #If no exception then break out out of loop here
            #Also check if number of integers are > 1
            if len(result) >= 1 and if_numbers_within_bounds(result):
                break
    return result
