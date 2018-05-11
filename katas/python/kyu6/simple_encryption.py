"""
http://www.codewars.com/kata/57814d79a56c88e3e0000786/train/python

For building the encrypted string:
Take every 2nd char from the string, then the other chars, that are not every 2nd char, and concat them as new String.
Do this n times!

Examples:

"This is a test!", 1 -> "hsi  etTi sats!"
"This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
Write two methods:

def encrypt(text, n)
def decrypt(encrypted_text, n)
For both methods:
If the input-string is null or empty return exactly this value!
If n is <= 0 then return the input text.
"""

from itertools import chain


def decrypt(encrypted_text, n):
    half_of_string = int(len(encrypted_text) / 2)

    for i in range(0, n):
        first_half, second_half = encrypted_text[:half_of_string], encrypted_text[half_of_string:]
        merged = list(zip(second_half, first_half))
        encrypted_text = ''.join(list(chain.from_iterable(merged)))
    return encrypted_text


def encrypt(text, n):
    for i in range(0, n):
        text = text[1::2] + text[::2]
    return text
