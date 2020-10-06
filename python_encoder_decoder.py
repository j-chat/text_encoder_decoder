"""
This script is to be executed in an IDE such as Spyder, PyCharm, etc. for Python 3
It encodes and decodes text using Python codecs. 

ARGUMENTS:
  text: text to encode or decode
  method: an option to pick encode or decode for the text
  encoding_type: the type of encoding. For standard types see:
  https://docs.python.org/3/library/codecs.html#standard-encodings 
  
 OUTPUTS:
  encoded_text: the encoded text
  decoded_text: the decoded text
"""

#import package(s)
import codecs

#ask user for inputs
text = input("text please: ")
method = input("choose encode or decode: ")
encoding_type = input("choose an encoding type like base64, bz2, hex, quopri, uu, zip : ")

#transform text to bytes
str_to_bytes = text.encode()

#conditional statement 
if method == 'encode':
    #encode the text
    encoded_text_in_bytes = codecs.encode(str_to_bytes,encoding_type, 'strict')
    #convert text from bytes to string
    encoded_text = encoded_text_in_bytes.decode()
    print('\nEncoded text: ' + encoded_text)
elif method == 'decode':
    #decode the text
    decoded_text_in_bytes = codecs.decode(str_to_bytes,encoding_type, 'strict')
    #convert text from bytes to string
    decoded_text = decoded_text_in_bytes.decode()
    print('\nDecoded text: ' + decoded_text)
else:
    print('invalid input')
