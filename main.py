"""
This is the main script of exercise which works as follows:
1. It takes user inputs:
    a. for code pattern of form "SSTS" [Note: code alphabets limit is set to 20]
    b. list of integers [integers from 1-20 allowed for sake of simplicity]
2. Then it apply subjected formating to print string pattern as mentioned in exercise

"""
from package.apply_format import apply_format
from package.user_input import get_code, get_integers
from package.retrieve_message import get_message_of_all_strings

if __name__ == '__main__':

    code_input = get_code() #Take user input
    integers_input = get_integers() #Ask integers input
    formatted_list = apply_format(code_input, integers_input) #Apply formating
    #print_all_strings(formatted_list) #print_result
    message_to_print = get_message_of_all_strings(formatted_list)
    print('\n'.join(message_to_print)) # print actual message
