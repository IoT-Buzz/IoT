from PIL import Image


def nth_bit_present(my_byte, n):
    return (my_byte & (1 << n)) != 0


def set_final_bit(my_byte, ends_in_one):
    new_byte = 0
    if ends_in_one:
        if(nth_bit_present(my_byte, 0)):
            # byte already ends in 1
            new_byte = my_byte
        else:
            new_byte = my_byte + 1
    else:
        if(nth_bit_present(my_byte, 0)):
            new_byte = my_byte - 1
        else:
            # byte already ends in 0
            new_byte = my_byte
    return new_byte


def encrypt(image_path, msg):

    # check if image is already a bitmap
    if image_path[-4:] != '.bmp':
        img = Image.open(image_path)
        image_path = image_path[:-4] + '.bmp'
        img.save(image_path)

    with open(image_path[:-4] + '.bmp', 'rb') as bmp_file:
        bmp = bmp_file.read()

    msg = bytearray(str(len(msg)) + '\n' + msg, 'utf-8')

    # color data begins at the byte at position 10
    start_offset = bmp[10]

    bmpa = bytearray(bmp)

    # convert the msg in bytes to bits
    bits = []
    for i in range(len(msg)):
        for j in range(7, -1, -1):
            bits.append(nth_bit_present(msg[i], j))

    data_array = bits

    # ensure the image is large enough to contain the text
    assert len(data_array) < len(bmpa) + start_offset

    for i in range(len(data_array)):
        bmpa[i + start_offset] = set_final_bit(bmpa[i + start_offset],
                                               data_array[i])

    with open(image_path.replace('.bmp', '_hidden.bmp'), 'wb') as out:
        out.write(bmpa)
    print('\nCover image with message saved with suffix _hidden\n')


msg = "Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography comes from Greek steganographia"
encrypt('polar bear.png', msg)
