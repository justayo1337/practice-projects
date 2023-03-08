from Crypto.Util.number import *

ciphtext = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

num = bytes_to_long(ciphtext)

for i in range(256):
    nums = [chr(a ^ i) for a in ciphtext]
    
    if "crypto" in "".join(nums):
        print("".join(nums))