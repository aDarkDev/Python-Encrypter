import marshal , base64 , py_compile , gzip , zlib
tag = "\n# By ConfusedCharacter \n#Don't try decode it because your time is gold."

def marshaling(text):
    compiled = compile(text,"","exec")
    marshaled = marshal.dumps(compiled)
    savingfile("import marshal;exec(marshal.loads("+repr(marshaled)+"))"+tag)

def hexing(text):
    level1 = text[:round(len(text)/2)]
    level2 = text[round(len(text)/2):]
    if type(level1) != bytes:
        level1 = level1.encode()

    if type(level2) != bytes:
        level2 = level2.encode()

    khkh = level1.hex()
    khkh2 = level2.hex()
    savingfile('exec(bytes.fromhex("'+khkh+'").decode()+bytes.fromhex("'+khkh2+'").decode())'+tag)

def base64ing(text):
    level1 = text[:round(len(text)/2)]
    level2 = text[round(len(text)/2):]

    if type(level1) != bytes:
        level1 = level1.encode()

    if type(level2) != bytes:
        level2 = level2.encode()

    khkh = base64.b64encode(level1).decode()
    khkh2 = base64.b85encode(level2).decode()
    savingfile("import base64;exec(base64.b64decode('"+khkh+"'.encode()).decode()+base64.b85decode('"+khkh2+"'.encode()).decode())"+tag)

def PYCompile(filename):
    py_compile.compile(filename,"your_file.py")


def gzipzlib(text):
    level1 = text[:round(len(text)/2)]
    level2 = text[round(len(text)/2):]

    if type(level1) != bytes:
        level1 = bytes(level1, 'utf-8')

    if type(level2) != bytes:
        level2 = bytes(level2, 'utf-8')

    khkh = gzip.compress(level1)
    khkh2 = zlib.compress(level2)
    savingfile('import gzip;import zlib;exec(gzip.decompress('+repr(khkh)+').decode(\'utf-8\')+zlib.decompress('+repr(khkh2)+').decode(\'utf-8\'))'+tag)

def openingfile():
    try:
        return open("your_file.py",encoding="utf-8").read()
    except:
        return open("your_file.py",'rb').read()

def savingfile(text):
    try:
        open('your_file.py','w+',encoding="utf-8").write(text)
    except:
        open('your_file.py','wb').write(text)