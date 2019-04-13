#!/usr/bin/python
from sys import modules,exit
from random import randint
modules.clear()
del modules

print("Guess The Password")
__builtins__.dir = None
execfile = None

pass_length = randint(10,21)

try:
    inp = input("input : ")
except:
    print "something is wrong"
    exit()
password = ''.join([str(randint(0,9)) for i in range(pass_length)])
assert pass_length >=1
print("comparing {} and password".format(inp))

for i in range(pass_length):
    if(inp[i] != password[i]):
        print "wrong"
        exit()

flag=open('./flag.txt','r').read()

print(flag)
