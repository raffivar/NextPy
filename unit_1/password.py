password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
print(password + " (original)")
print(''.join(list(map(lambda char: chr(ord(char) + 2) if char.isalpha() else char, password))))
