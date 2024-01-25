def copy_file(source, destination):
    "Copy an entire file to another"
    src = open('src.txt', 'r')
    dst = open('dst.txt', 'w')

    while 1:
        chunk = src.read(50)
        if(chunk == ""):
            break
        dst.write(chunk)
    
    src.close()
    dst.close()
    return