import secrets, string

def MY_PASSWORD():
    """
    A program that displays a secure random password 
    : return: None
    """
    try:
        # get the length of the user
        # desired password
        length_of_password = int(input('\nEnter the length of your desired password: '))
    except ValueError:
        print('Invalid Input!')
    else:
        # make a string that contains both upper and 
        # lower  case letters, digits and punctuations
        password_picks = string.ascii_letters + string.digits + string.punctuation
        # select a password based on the length entered
        # from the combination of both upper and lower case letters
        # digits and punctuations
        yourPassword = ''.join(secrets.choice(password_picks) for i in range(length_of_password))
        # make a list of the generated password
        password_list = list(yourPassword)
        # shuffle the password
        secrets.SystemRandom().shuffle(password_list)
        print('Password:',''.join(password_list))

MY_PASSWORD()