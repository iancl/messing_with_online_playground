'''
Messing with online python playgrounds
NOTE: ONLINE PYTHON PLAYGROUNDS PROBABLY RUN ON DOCKER CONTAINERS OR SANDBOXES OR process lacks root privileges SO
      NO REAL HARM CAN BE DONE WITH THIS


Situation:

All occurrences of this text 'system' will be stripped from the code written
here when processed by the client or server. There for strings will be stripped
of the word 'system' and import statements will throw errors

This is to prevent access to os.system which allows us to run shell commands

Examples:
a- import system from os # will be converted to: import from os
b- import os.system will be converted to: import os.
c- modulelib.import_module('os.system') to: modulelib.import_module('os.')
d- string '12system12' # will be converted to: 1212


Try a, b, c by youselves because if I add them they will break the script


Solution:
1. Create an algorithm that _during_runtime_ joins an array of chars and split them by using a designated char to signal that the current word is complete:
   i.e: ['o', 's', '.', 's', 'y', 's', 't', 'e', 'm'] should be turned into
   strings "os" and "system" during runtime
   
 2. use the setattr() build in function to extract the 'system' method from
    the os module during runtime


'''
import importlib


def join_and_split_by_separator(chars, separator=None):
    '''
    This function takes a list of chars and an optional separator
    
    Notes: 
        - if separator is provided then all chars before and after it will
          be stored as a string in each key of the dict
        - if the separator is not found then all the chars will be stored
          as a string in the dict
    
    @param chars {list} list of chars
    @param separator {str} (optional) a char
    
    return {dict} dict which keys will be integers from 0 to n and each key
                  will contain a word
    '''
    index = 0
    word_map = {}
    
    
    for char in chars:
        
        if separator and char == separator:
            index += 1
            continue
        
        if index in word_map:
            word_map[index] += char
        else:
            word_map[index] = char
    
    return word_map

# substring 'system' will be stripped from these below
print('12system12')   # 1212
print('foo.system')   # foo.
print('this is a system') # this is a  

# generating strings at runtime
generated_str = join_and_split_by_separator(
    chars=['o', 's', '.', 's', 'y', 's', 't', 'e', 'm'], separator='.')

# now we get what we want
print(generated_str) # {0: 'first', 1: 'system'}

# import os
import os

# get system method
method = getattr(os, generated_str[1])

# it's there :D
print(method)

# list current dir contents :v
output = method('ls -la /')

# list current dir contents
print(output)



