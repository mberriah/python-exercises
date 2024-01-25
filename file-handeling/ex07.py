def filter(source, destination):
    "Recopy a file by eliminating the remarks lines."
    "Copy an entire file to another"
    src = open('src.txt', 'r')
    dst = open('dst.txt', 'w')

    while 1:
        chunk = src.read(50)
        if(chunk == ""):
            break
        if(chunk[0] != '#'):
            dst.write(chunk)
    
    src.close()
    dst.close()
    return