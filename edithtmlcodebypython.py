Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 19:28:18) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> o=input("enter your name")
import codecs
with codecs.open(r"C:\Users\DIVYA JOSHI\Desktop\main.html","rt")as file:
    a=list()
    for g in file:
        a.append(g)
#print(a)

with codecs.open(r"C:\Users\DIVYA JOSHI\Desktop\main.html","rt")as file1:
    i=0
    m=''
    h=open(r"C:\Users\DIVYA JOSHI\Desktop\blank.txt","w")
    for g in file1:
        if i==8:
            for j in g:
                if j==" ":
                    m+="\n"+str(j)+"\n"
                elif j=="<":
                    m+="\n"+str(j)+"\n"
                elif j==":":
                    m+="\n"+str(j)+"\n"
                elif j=='"':
                    m+="\n"+str(j)+"\n"
                elif j==">":
                    m+="\n"+str(j)+"\n"
                elif j=="=":
                    m+="\n"+str(j)+"\n"
                else:
                    m+=str(j)
                    
        i+=1
    h.write(m)
    h.close()
with codecs.open(r"C:\Users\DIVYA JOSHI\Desktop\blank.txt","rt")as fi:
    hj=list()
    for v in fi:
       hj.append(v)
hj[40]=o
k=''
for d in hj:
    for s in d:
        if s=="\n":
            continue
        else:
            k+=s

a[8]=k
w=open(r"C:\Users\DIVYA JOSHI\Desktop\copy.txt","w")
for z in a:
    w.write(z)
w.close()

jk1=open(r"C:\Users\DIVYA JOSHI\Desktop\main.html","w")
ww=open(r"C:\Users\DIVYA JOSHI\Desktop\copy.txt","r")
gb=ww.read()
jk1.truncate()
jk1.write(gb)
ww.close()
jk1.close()


    
    


