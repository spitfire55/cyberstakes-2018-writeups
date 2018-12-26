# Pythoooooooooon

## Reverse Engineering - 50 Points

#### Description

There is a 'protected' flag available at at challenge.acictf.com:7506.
We were able to recover the source code of the protection, which you can
download at ooo.py. Can you recover the flag?

#### Hints

- Can you identify the critical operations to 'protect' the flag?
- Can you determine the order of the functions?
- Can you write an equivalent (but readable) version of the script?

### Solution 

This challenge is a nice introduction to code obfuscation challenges that are
fairly popular in CTF competitions. We are given a Python file and a remote
port to interact with. I first connect to the listener w/ netcat and get the
following base64-encoded flag: `OTsxAxtMSkAbHRlJSR0ZSk0ZHUsZTR4eSksZHh1NGwU=`.
This "protected" flag is the output of the provided [ooo.py](ooo.py) script,
which encoded the actual flag.

The first thing I do is try to understand which of the function calls happen in 
which order. I realize quickly that each function call occurs in descending 
length order, which is the opposite order that the functions are organized 
above the main `ooooooo` function.

Next, I need to figure out what each function is doing. If we look at `ooo`, an 
XOR operator and the use of list comprehension suggests that the nested function
calls XOR each byte of the flag with a one-byte key. Since we are trying to
decode the encoded flag, we should just need to XOR the encoded bytes again with
the correct key bytes in reverse order to get the original decoded flag. If we
then look at the other functions, most of them have the same body, but a
different integer multiplier applied to the `'o'` character to produce a sequence
of `'o'` in varying length. Finally, if we look at the `oooooooo` function, which
is called in every function that contains the integer multiplier, it simply
returns the length of the parameter, which is the sequence of `'o'`s. Without
knowing exactly how the code works, I have enough information to guess that the
encoded flag can be decoded by iteratively XORing the flag with the single-byte
XOR keys, which can be extracted from the functions defined above the `ooo`
function.

My solve script can be found at [ooo_solve.py](ooo_solve.py). I manually
extracted the integer values from functions into a list, and then iterate over
that list in reverse order, iteratively XORing the base64-decoded flag with the
integer value. This produces the flag!
