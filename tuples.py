tp=(4,)
>>> dir(tp)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> tnew=(range(10))
>>> tnew
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> tne=1,2,3,4
>>> tne
(1, 2, 3, 4)
>>> a,b,c,d=tne
>>> a
1
>>> b
2
>>> c
3
>>> d# tne helps assign d to 4(method assignment)
4
new=(1,2,3,4,5,5,3,2)
>>> tnew.index(2,5)
7
>>> tnew.index(5,5)
5

>>> ad=yogeshl@batman
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'yogeshl' is not defined
>>> ad='yogeshl@batman'
>>> bd=as.split(@)
  File "<stdin>", line 1
    bd=as.split(@)
        ^
SyntaxError: invalid syntax
>>> bd=ad.split(@)
  File "<stdin>", line 1
    bd=ad.split(@)
                ^
SyntaxError: invalid syntax
>>> bd=ad.split('@')
>>> b,d=ad.split('@')
>>> b
'yogeshl'
>>> d
'batman'
>>> q,r=divmod(24,4)
>>> q
6
>>> r
0
>>> def fun(a,b)
  File "<stdin>", line 1
    def fun(a,b)
               ^
SyntaxError: invalid syntax
>>> def fun(a,b):
...    q=a/b
...    r=a%b
...    return q,r
... 
>>> a=24
>>> b=4
>>> fun(a,b)
(6.0, 0)
>>> q,r=divmod(24,0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> a=1,2,3,4
>>> b=a,b,c,d
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> b=(a,b,c,d)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
>>> b=('a,b,c,d')
>>> type(b)
<class 'str'>
>>> b='a','b','c','d'
>>> t=zip(a,b)
>>> t
<zip object at 0x7f6bb62d0748>
>>> t(zip(a,b))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'zip' object is not callable
>>> t=zip(a,b)
>>> tuple(t)
((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

>>> [(x,x**2) for x in range(1,6)]
[(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]#this i comprehension

