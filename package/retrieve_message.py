"""
This script print all strings with applied mapping of soft and tough
"""
def get_message_single_string(string):
    """this function is used to print desired output"""

     #Allow string length only from 1-20
    if len(string) < 1 or len(string) > 20:
        return ''
    else:
        code = {"S":"soft", "T":"tough"}
        #change string to upper case if its in lower TestCase
        if string.islower():
            string = string.upper()
        message = ""
        for letter in string:
            if letter == "S":
                message += code['S'] + ' '
                #print(code['S'])
            elif letter == "T":
                #print(code['T'])
                message += code['T'] + ' '
        #print(message)
        return message

def get_message_of_all_strings(string_list):
    """print all strings in a list"""
    message_to_print = []
    for string in string_list:
        message_single_string = get_message_single_string(string)
        message_to_print.append(message_single_string)
    return message_to_print
