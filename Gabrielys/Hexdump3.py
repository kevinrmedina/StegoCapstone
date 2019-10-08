#!/usr/bin/env python3

import mimetypes
import argparse
import math
import os
import sys
from hexForm import *

def dump(filepath, fileName, chunksize = 16, verbose = False, info = False, raw = False):
    if not os.path.exists(filepath): raise FileNotFoundError("file not found")
    if not os.path.isfile(filepath): raise IsADirectoryError("not a file")
 
    #avoid dd numbers
    chunksize += chunksize % 2
    separator = '' if raw else '|'
    line = 0
 
    #find the file type
    type = mimetypes.MimeTypes().guess_type(filepath)[0]
    size = os.path.getsize(filepath)
    result = "Name : {nm}\nExt  : {ex}\nSize : {sz} octet\nMime : {tp}\n".format(
        nm = os.path.splitext(filepath)[0],
        ex = os.path.splitext(filepath)[1][1:],
        sz = size,
        tp = type if not type == None else '',
    ) if info else ''
 
    if verbose and info: print(result)
 
    with open(filepath, "rb") as file:
        while True:
            chunk = file.read(chunksize)
            if len(chunk) == 0: break
 
            text = "{ln:0{zp}x} {sp} {hd} {tl}{pa}{sp} {tx}\n".format(
                sp = separator,
                #zero padding, calcul the max line and convert to str/hex and get the length
                zp = len(hex(math.ceil(size / chunksize))[2:]),
                ln = line,
                hd = ''.join("{:02X} ".format(c) for c in chunk[:int(chunksize / 2)]),
                tl = ''.join("{:02X} ".format(c) for c in chunk[int(chunksize / 2):]),
                pa = '   ' * (chunksize - len(chunk)),
                tx = ''.join([chr(c) if c in range(32, 127) else '.' for c in chunk]),
            )
 
            if verbose: print(text, end='')
            line += 1


    """
            #Uncomment this if you want use the function for ohter purpose than just
            #print the result, otherwise it's just take memory and slowdown the script.
           result += text
 
   return result
   """
 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file to dump.")
    parser.add_argument("name", help="file name.")
    parser.add_argument("-c", "--chunksize", nargs='?', type=int, default=16, help="choose chunk size, default is 16.")
    parser.add_argument("-i", "--info", action="store_true", help="show file name, type, size, ext.")
    parser.add_argument("-r", "--raw", action="store_true", help="remove the separtor character \'|\'.")
 
    #No output file options because bash can do this like this "hexdump.py hello.txt > hello_dumped.txt"
    #No verbose options because it's useless, if we dont print anythin we wont see the result
 
    args = parser.parse_args()
    
    if args.file: 
        sys.stdout = open(args.name, 'w')	
        dump(args.file, args.name, args.chunksize, True, args.info, args.raw)
        
    else: print(parser.usage)

