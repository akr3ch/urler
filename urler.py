#!/usr/bin/python3

# simple python script for url encode and decode
# coder: akr3ch
# github: akr3ch

from urllib.parse import unquote,quote
import sys

def encode():
    while True:
        try:
            value = input('->')
            print(quote(value))
        except(KeyboardInterrupt):
            exit(0)

def decode():
    while True:
        try:
            value = input('->')
            print(unquote(value))
        except(KeyboardInterrupt):
            exit(0)

if (len(sys.argv) != 2):
    print(f'Usage:\n{sys.argv[0]} -d    -> url decode every input\n{sys.argv[0]} -e    -> url encode every input')
elif (sys.argv[1] == '-d'):
    decode()
elif (sys.argv[1] == '-e'):
    encode()
else:
    print(f'Usage:\n{sys.argv[0]} -d    -> url decode every input\n{sys.argv[0]} -e    -> url encode every value')
