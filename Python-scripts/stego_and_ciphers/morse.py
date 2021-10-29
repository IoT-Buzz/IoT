MORSE_CODE_DICT = {

    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}

REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encrypt(message):
    morse = ""
    for char in message.upper():
        morse += "".join(MORSE_CODE_DICT[char])+" "
    return morse


def decrypt(message):
    message_ = ""
    for char in message.split():
        message_ += " ".join(REVERSE_DICT[char])
    return message_


print(encrypt("harsh"))
print(decrypt(".... .- .-. ... ...."))
