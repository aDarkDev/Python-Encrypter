import os
from Core import funcs ,config
import time , sys
from tkinter import Tk     
from tkinter.filedialog import askopenfilename

Tk().withdraw()
os.system("cls")
K1 = '\033[36m'+"-"*24+'\033[0m'
K2 = '\033[36m|\033[0m'
K3 = "\033[91mHEX\033[0m"
K4 = "\033[91mBase64\033[0m"
K5 = "\033[91mGZIPZLIB\033[0m"
K6 = "\033[91mPYC\033[0m"
K7 = "\033[91mMARSHAL\033[0m"
K8 = "\033[35mCount : \033[0m"
K9 = lambda s:"\033[33m"+str(s)+"\033[0m"
K10 = "\033[1;36;40m"+"Python Encryptor  "+"\033[0m"

print(f"""
{K1}
{K2}  {K10} {K2}
{K1}
{K2}  {K4}  {K2} {K8}{K9(config.BASE64)} {K2} 
{K1}
{K2}   {K3}    {K2} {K8}{K9(config.HEX)} {K2} 
{K1}                                                     
{K2} {K5} {K2} {K8}{K9(config.GZIPZLIB)} {K2} 
{K1}                                                     
{K2}   {K6}    {K2} {K8}{K9(config.PYCOMPILE)} {K2} 
{K1}
{K2}  {K7} {K2} {K8}{K9(config.MARSHAL)} {K2} 
{K1}""")

time.sleep(0.2)

for x in list('[+] Enter File Name: '):
    sys.stdout.write(x)
    sys.stdout.flush()
    time.sleep(0.02)

print("",end="")

time.sleep(0.1)
filename = askopenfilename()
print(filename)

try:
    data_file_ = open(filename,encoding="utf-8").read()
except:
    data_file_ = open(filename,'rb').read()

try:
    open('your_file.py','w+',encoding="utf-8").write(data_file_)
except:
    open('your_file.py','wb').write(data_file_)

while config.HEX != 0 or config.BASE64 != 0 or config.GZIPZLIB != 0 or config.MARSHAL != 0:
    if config.MARSHAL != 0:
        text = funcs.marshaling(funcs.openingfile())
        config.MARSHAL -= 1
    
    if config.HEX != 0:
        funcs.hexing(funcs.openingfile())
        config.HEX -= 1

    if config.GZIPZLIB != 0:
        funcs.gzipzlib(funcs.openingfile())
        config.GZIPZLIB -= 1


    if config.BASE64 != 0:
        funcs.base64ing(funcs.openingfile())
        config.BASE64 -= 1

while config.PYCOMPILE != 0:
    if config.PYCOMPILE != 0:
        text = funcs.PYCompile("your_file.py")
        config.PYCOMPILE -= 1


input("[ \033[92mEncryption Success\033[0m ] \n[+] New File Saved in \"your_file.py.\"")