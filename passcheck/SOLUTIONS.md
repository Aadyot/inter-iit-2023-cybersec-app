I decompiled the provided file using the FernFlower decompiler.

"lookup" is array of size 40

hash function does some weird stuff and gets a char between A and Z using 2 ints.

check function:
if input size * 2 is not of length 40 then WRONG

so input string length must be 20

i'th char of string must be equal to 
hash(lookup[2i], lookup[2i+1])

if this is true for all i, then CORRECT
else WRONG

so only 1 password is possible, which i can generate by adding a print statement to the decompiled file, and getting back 1 charachter at a time.

password:
KXRPQQGZWSQQWAKDFRMA
