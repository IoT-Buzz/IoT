from PIL import Image


def nth_bit_present(my_byte, n):

    return (my_byte & (1 << n)) != 0


def bits_to_byte(bits):
    # convert 8 bits into 1 byte
    assert len(bits) == 8
    new_byte = 0
    for i in range(8):
        if bits[i]:
            new_byte |= 1 << 7 - i
        else:
            new_byte |= 0 << 7 - i
    return new_byte


def decrypt(image_path):
    with open(image_path, 'rb') as bmp_file:
        bmp = bmp_file.read()

    start_offset = bmp[10]

    # deconstruct each byte and get its final bit
    bits = []
    for i in range(start_offset, len(bmp)):
        bits.append(nth_bit_present(bmp[i], 0))

    # combine our bit array into bytes
    out_bytes = []
    for i in range(0, len(bits), 8):
        if(len(bits) - i > 8):
            out_bytes.append(bits_to_byte(bits[i: i + 8]))

    # convert bytes to characters
    out = []
    for b in out_bytes:
        out.append(chr(b))

    output = ''.join(out)

    # strip out the first line containing the length of the message
    idx = output.find('\n')
    msg_len = int(output[:idx])
    msg = output[idx + 1: idx + msg_len + 1]

    print('Hidden message:')
    print(msg, '\n')

    return msg
