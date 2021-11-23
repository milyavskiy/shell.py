#!/usr/bin/env python3

# https://docs.python.org/3/library/os.html
# https://danishpraka.sh/2018/09/27/shell-in-python.html
# https://brennan.io/2015/01/16/write-a-shell-in-c/

import os

def execute(argv):
    args = argv.split(" ")
    pid = os.fork()
    if (pid == 0):   # Child
        try:
            os.execvp(args[0], args)
        except Exception as err:
            print(err, argv)
            os._exit(err.args[0])
    else:   # Parent
        os.waitpid(pid, 0)

def cd(path):
    try:
        os.chdir(os.path.abspath(path))
    except Exception as err:
        print(err)

def main():
    while True:
        try:
            inp = input("$ ").strip()
            if inp == "cd" or inp[:3] == "cd ":
                cd(inp[3:])
            elif inp == "exit":
                break
            elif inp:
                execute(inp)
        except EOFError:   # Catch Ctrl-D
            print()
            break

if '__main__' == __name__:
    main()
