f=open('unsort.txt','r')
f1=open('sort.txt','w')
for i in f.readlines():
    l=(list(map(int,i.split())))
    l.sort()
    for p in l:
        f1.write(str(p)+' ')
    f1.write('\n')
f.close()
f1.close()

    
    