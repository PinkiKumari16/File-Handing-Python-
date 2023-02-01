# USE OF FILE HANDLING 
# f=open('file name',modes)
#        ( abc.txt  , r)
# * modes
# 1. r = read only
# 2. w = write-read
# 3. a = read-append

# ** f.readlines() : use only one line read     * its gives answer in list
# ** f.read()  : use all paragraph in one time  * its gives answer in string
# ** f.close()


# f=open('file.txt','r')
# p=f.read()
# print(p)
# print(type(p))

# f=open('ret.txt','r')
# l=[]
# for line in f.readlines():
#     l.append(list(map(int,line.split())))
# print(l)


# f=open('text.txt','w') ** agar text nam ki file nhi hogi to automatic ban jayga.
# f.write('Hello pink.\n 1 2 3')
# f.close()

#f=open('text.txt','a')
# f.write('pinki') 
# f.close()

# k=open('file.txt','a')
# k.write('preeti')
# print(k)

# import os
# os.remove('text.txt')

