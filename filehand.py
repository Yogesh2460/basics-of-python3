pe "help", "copyright", "credits" or "license" for more information.
>>> fp=open("definefunctio.py","r")
>>> fp.seek(20)
20
>>> fp.readline()
'rint("hello")\n'
>>> fp.seek(30)
30
>>> fp.readline()
'o")\n'
>>> fp.seek(40)
40
>>> fp.readline()
'int("hajime mashite")\n'
>>> fp.tell()
62
