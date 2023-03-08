
orig = "label"

new = "".join([chr(ord(x) ^ 13) for x in orig])

print(new)