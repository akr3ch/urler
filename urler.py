#!/usr/bin/python3

# simple python script for encoding and decoding from CLI
# coder: akr3ch
# github: akr3ch

from urllib.parse import unquote,quote
import sys
import base64


# color codes
red = "\x1b[31m"
green = "\x1b[32m"
yellow = "\x1b[33m"
blue = "\x1b[34m"
stop = "\x1b[0m"


def __encode():
    while True:
        try:
            value = input(f'{red}[url-encode]»» {stop}')
            print(quote(value))
        except:
            exit(0)

def __decode():
    while True:
        try:
            value = input(f'{red}[url-decode]»» {stop}')
            print(unquote(value))
        except:
            exit(0)

def base64__decode():
    while True:
         try:
             value = input(f'{red}[b64-decode]»» {stop}')
             data = base64.b64decode(unquote(value))
             print(data.decode("utf-8"))
         except:
             exit(0)

def base64__encode():
    while True:
         try:
             value = input(f'{red}[b64-encode]»» {stop}')
             data = base64.b64encode(bytes(value,"utf-8"))
             print(data.decode("utf-8"))
         except:
             exit(0)


menu = f"""
{blue}┌───────────┬───────────────────────────────┐
{blue}│{red}  Command {blue} │         {green}Information{stop}           {blue}│
{blue}│───────────┼───────────────────────────────│
{blue}│{red} urler -ud {blue}│   {green}url decode every input{stop}      {blue}│
{blue}│───────────┼───────────────────────────────│
{blue}│{red} urler -ue {blue}│   {green}url encode every input{stop}      {blue}│
{blue}│───────────┼───────────────────────────────│
{blue}│{red} urler -be{blue} │   {green}b64 encode every input{stop}      {blue}│
{blue}│───────────┼───────────────────────────────│
{blue}│{red} urler -bd{blue} │   {green}b64 decode every input{stop}      {blue}│
{blue}└───────────┴───────────────────────────────┘
"""
if (len(sys.argv) != 2):
    print(menu)


elif (sys.argv[1] == '-ud'):
    __decode()
elif (sys.argv[1] == '-ue'):
    __encode()
elif (sys.argv[1] == '-bd'):
    base64__decode()
elif (sys.argv[1] == '-be'):
    base64__encode()
else:
    print(menu)
