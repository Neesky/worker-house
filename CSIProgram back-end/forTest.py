import hashlib

h1 = hashlib.md5()
h1.update("00000000".encode(encoding='utf-8'))
print(h1.hexdigest())
