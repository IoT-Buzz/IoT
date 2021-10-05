import secrets, string

def password_generator():
    """
    A program that generates a secure random password
    : return: None
    """
    try:
        # get the length of alphabets to be present in password
        length_of_alphabets = int(input('\nEnter the length of alphabets (upper and lower case inclusive): '))
        # get the length of digits to be present in password
        length_of_digits = int(input('Enter the length of digits: '))
        # get the length of special characters to be present in password
        length_of_special_characters = int(input('Enter the length of special characters: '))
    except ValueError:
        print('Invalid Input!')
    else:
        # get the total password length
        passwordLength = length_of_alphabets + length_of_digits + length_of_special_characters
        # generate a password for user based on the total password length
        securePassword = ''.join(secrets.choice(string.ascii_letters) for i in range(length_of_alphabets))
        securePassword += ''.join(secrets.choice(string.digits) for i in range(length_of_digits))
        securePassword += ''.join(secrets.choice(string.punctuation) for i in range(length_of_special_characters))
        # make a list with the password
        generated_password = list(securePassword)
        # shuffle generated password
        secrets.SystemRandom().shuffle(generated_password)
        print('Your password of length {} is {}'.format(passwordLength,''.join(generated_password)))

password_generator()