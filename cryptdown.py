#Esse script precisa ser encriptado para ser 100% eficaz

print("\033[35m")
import py_compile
py_compile.compile("anondown.py")

fileName = 'Python.png'
print(" ██████╗██████╗ ██╗   ██╗██████╗ ████████╗    ██████╗ ███████╗████████╗")
print("██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝   ██╔════╝ ██╔════╝╚══██╔══╝")
print("██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║█████╗██║  ███╗█████╗     ██║   ")
print("██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║╚════╝██║   ██║██╔══╝     ██║   ")
print("╚██████╗██║  ██║   ██║   ██║        ██║      ╚██████╔╝███████╗   ██║   ")
print(" ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝       ╚═════╝ ╚══════╝   ╚═╝   ")
                                                                       
print("\033[96m                         Coded By Hyd3 | Arquivo: " + fileName)
print(" ")
print(" ")
import requests
link = "https://pastebin.com/raw/GTcBzmhd"
f = requests.get(link)
respos = input('\033[35m[+]\033[96m Senha: ')
if respos == f.text:



# ALTERE AQUI AS INFORMAÇÕES!!!
#Url = link de download direto do arquivo
 url = 'https://www.python.org/static/img/python-logo.png'
 print("\033[35m[+]\033[96m Baixando Arquivo | " + fileName + "\033[91m")

 req = requests.get(url) 
 file = open(fileName, 'wb')
 for chunk in req.iter_content(100000):
    file.write(chunk)
 file.close()
 print("\033[35m[+]\033[96m Arquivo Baixado!!")
else:
 print("\033[35m[+]\033[91m Senha Errada")
                                                                                                                     
