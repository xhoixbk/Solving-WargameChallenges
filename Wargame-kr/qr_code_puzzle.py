"""
This script decode the URL encoded string in Javascript of the challenge [Wargame.kr] QR CODE PUZZLE
Author: xhoix - email: xhoixbk@gmail.com, blog: khanglambk.blogspot.com
Python 3.5.2
"""
from urllib.parse import unquote

urlencoded = '.%2f%69%6d%67%2f%71%72%2e%70%6e%67'
print(unquote(urlencoded))


