# termcolor package
import sys
from termcolor import colored, cprint

print('helloo world!')

text = colored('hello, world!', 'red', attrs=['reverse', 'blink'])

print (text)

text1 = colored('hello, world!', 'red', attrs=[ 'blink'])

print (text1)


