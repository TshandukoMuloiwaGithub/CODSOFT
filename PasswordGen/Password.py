#THis program should generate password for users
import random
def get_length():
    '''
    get users disired lenght of password
    return an integer
    '''
    try:
        return int(input('Enter the disired password length: '))
    
    except ValueError:
        print('Invalid length value\nNB: Please enter an integer value.')
        return get_length()



def complexity():
    '''
    THis functions return the users preferred password complexity
    '''
    complexity_details = '''choose password complexity:
    LOW - at least 6 characters
    FAIR - at least 8 characters including lower,upper-case letter and a number
    GOOD - at least 8 characters including at least 3 of the 4 types of characters:
          lower,upper-case letter,a number, a special character such as !@#$%^&*
    EXCELLENT - at least
    '''
    print(complexity_details)
    try:
        return input('Password complexity (eg. LOW): ').lower()
    
    except ValueError:
        print('Invalid complexity, choose from the given options')
        return complexity()
    
def adding_number(password_list,length):
    '''
    This function return a list of the password list given to it
    But with a number appended to it
    '''
    random_num = str(random.randint(0,9))
    pick_index = random.randint(0,length-1)

    password_list[pick_index] = random_num

    return password_list

def letters(length,pass_complexity):
    import string
    all_letters = string.ascii_letters
    password = ''
    random_letters = ''.join(random.choice(all_letters) for i in range(length))
    password_list = []

    #Splitting string password into a list for proper examination
    for x in random_letters:
        password_list.append(x)
    
    #k s  j F h J v F
    
    if pass_complexity == 'low' and length >= 6:
        #might have to return as soon as low complexity is generated
        return ''.join(password_list)
    
    elif pass_complexity == 'fair' and length >= 8:
        password_list = adding_number(password_list,length)
        return ''.join(password_list)
    elif pass_complexity == 'good' and length >= 8:
        password_list = adding_number(password_list,length)
        return password_list
    

    return random_letters

def start():
    '''
    This function call all the necssary function to genearate user password
    '''

    
    password_length = get_length()

    password_complexity = complexity()

    generated_string = letters(password_length,password_complexity)

    print(generated_string)
if __name__ == "__main__":
    start()
    
