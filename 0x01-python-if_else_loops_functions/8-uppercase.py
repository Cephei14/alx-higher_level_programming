def uppercase(str):
    Upstr = ""
    for c in str:
        if 'a' <= c <= 'z':
            Nc = chr(ord(c) - 32)
            Upstr += Nc
        else:
            Upstr += c
    print(Upstr)
