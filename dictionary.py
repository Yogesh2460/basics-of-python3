"""
str1=input("enter the strin")
str1=str1.split()
strword=[]
strcount=[]

count=0
for i in str1:
    if i in strword:
        index=strword[i]
        strcount[index]+=1
    else:
        strword.append(i)
        strcount.append(i)


    """
#done by yoges"
"""
str1=input("enter")
print(str1)

spl=str1.split(" ")
print(spl)

def freq(str1):
    str_list=str1.split(" ")
    unique=set(str_list)
    for words in unique:
        a=str_list.coount(words)
        return a

if __name__=="__main__":
    freq(str1)
    d1=dict.fromkeys(spl,a)
    print(d1)
"""
str=input()
print(str)
str=str.split()
str1=set(str)
print(str1)
count=[]
for ele in str1:#if we run for loopfor str then we'll get multiple values & we here done for str1 becz we want count unique word
    count.append(str.count(ele))

d=dict(zip(str1,count))
print(d)

"""o/p=>
"heelo rep heelo rep"
heelo rep heelo rep
set([' ', 'e', 'h', 'l', 'o', 'p', 'r'])
{' ': 3, 'e': 6, 'h': 2, 'l': 2, 'o': 2, 'p': 2, 'r': 2}
"""
