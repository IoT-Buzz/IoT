# Steganography and Ciphers
## Stegangraphy
### Intro
* Steganography is the subtle art of hiding any form of media into any other form of media. This can include texts, images, videos and audio files too.

* The essence of steganography is, once hidden, the 3rd party can't even tell if a particular media is stego file or no unlike encryption where entire face of media is changed.

### Algorithm
* There are various algorithms to implement steganography, but here I have just implement the most commonly used used one (LSB-Least Significant Bit) algorithm which hides text strings into images.

### Scripts
* There are 2 files named as `hide_text.py` and `extract_text.py` which perform functions as the name suggests. 
* `hide_text.py` has a function `encrypt(img,msg)` which takes 2 parameters as input: cover image and message string to hide.
* Once, both these parameters are passed, it will hide the text in the image and generate the new image which will be saved with name "_hidden" appended at the end.
* `extract_text.py` will extract the message from the given image. It has a function `decrypt(img)` which takes only image as parameter.
* Just the stego image has to be passed to this function and it will return the hidden message.

Note: ensure that cover image is large as compared to input string or else this algorithm will fail.
## Cipher
* Out of many many ciphers available out there, I have chosen morse code. Basically coz it's really cool and I had always been fascinated by it.
* The file `morse.py` has 2 functions namely `encrypt(msg)` and `decrypt(msg)`. They also do as the name suggests.
* Call the `encrypt` function with a single string parameter to get morse coded output.
* Similarly, call the `decrypt` function with morse code string input to get the decoded message! 

Happy coding decoding!