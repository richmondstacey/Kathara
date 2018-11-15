import os
import re
import sys
from utils import log 
from utils import istextfile

def win2linux(filename):
    c = None
    istext = False
    with open(filename) as f:
        istext = istextfile(f)
        if not istext:
            return
        else c = f.read()
        if len(c) <= 0:
            return
    try: #python3 
        open(filename, 'wb').write(re.sub(r'\r', '', c).encode())
    except: #python2
        open(filename, 'wb').write(re.sub(r'\r', '', c))


def win2linux_all_files_in_dir(some_dir):
    for dname, dirs, files in os.walk(some_dir):
        for fname in files:
            fpath = os.path.join(dname, fname)
            try: 
                win2linux(fpath)
            except Exception as e: # not a text file, probably
                log('Exception on ' + fpath)
                log(str(e))