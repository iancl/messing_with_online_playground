# Messing with online python playgrounds

NOTE: ONLINE PYTHON PLAYGROUNDS PROBABLY RUN ON DOCKER CONTAINERS OR SANDBOXES OR process lacks root privileges SO
      NO REAL HARM CAN BE DONE WITH THIS

## Situation:

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


## Solution:

1. Create an algorithm that _during_runtime_ joins an array of chars and split them by using a designated char to signal that the current word is complete:
   i.e: ['o', 's', '.', 's', 'y', 's', 't', 'e', 'm'] should be turned into
   strings "os" and "system" during runtime
   
 2. use the setattr() build in function to extract the 'system' method from
    the os module during runtime
