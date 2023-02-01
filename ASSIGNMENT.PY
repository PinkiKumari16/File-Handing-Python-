#    1. Write a Python program to read an entire text file.
# p=open('assig.txt','r')
# read=p.read()
# print(read)
# p.close()

# ******************************************************************************
#  2. Write a Python program to read the first n lines of a file.
# a=open('assig.txt','r')
# b=a.readline()
# print(b)
# a.close()

# ************************************************************************
# 3. Write a Python program to append text to a file and display the text.
# o=open('assig.txt','a')
# o.write('\n'+'i am good pinki and i am quick learner')
# o.close()

# **************************************************************************
# 4. Write a Python program to read the last n lines of a file.
# n=int(input("enter line's no."))
# a=open('assig.txt','r')
# p=a.readlines()
# while n!=0:
#     print(p[-n])
#     n-=1

# *******************************************************************************
# 5. Write a Python program to read a file line by line and store it into a list.

# p=open('assig.txt','r')
# # l=[]
# for i in p:
#     a=p.readline()
#     print(a)
#     l.append(str(a).replace('\n',''))
# print(l)
# p.close()

# **********************************************************************
# 6. Write a Python program to read a file line by line and store it into a string variable.
# p=open('assig.txt','r')
# l=''
# for a in p:
#     print(a)
#     l+=(str(a).replace('\n',''))
# print()
# print('this is a string : -','\n')
# print(l)
# p.close()

# *********************************************************************
# 7. Write a program to store a matrix into a nested list. (Matrix in a text file) 
# a=open('ret.txt','r')
# l=a.readlines()
# n_l=[]
# for i in l:
#     n_l.append(list(map(int,(i.replace('\n','').split())))        
# print(n_l)

# **************************************************************************
# 8. Write a python program to find the longest words in a text file.
# p=open('max-file.txt','r')
# l=p.readlines()
# max1=0
# m=0
# for i in l:
#     i=i.split()
#     for j in i:
#         if len(j)>max1:
#             max1=len(j)
#             m=j
# print('The max lenght is :-',max1,(m))

# ****************************************************************************
# 9. Write a Python program to count the number of lines in a text file.
# p=open('assig.txt','r')
# a=p.readlines()
# print(len(a))
# p.close()

# o=open('max-file.txt','r')
# c=0
# for i in o:
#     print(i)
#     c+=1
# print(c)
# o.close()
# ************************************************************************
# 10. Write a Python program to count the frequency of words in a file.
# o=open('max-file.txt','r')
# c=0
# d={}
# for i in o:
#     i=i.split()
#     for j in i:
#       d.setdefault(j,0)
#       d[j]+=1
# print(d)
# o.close()
    
# ************************************************************************
# 11. Write a python program to store the names and birthdays of your friends in a text file .
# d={'pinki':'26-7-2002','Aarti':'10-12-2002','Khushboo':'10-4-2001','Honey':'13-3-2002','preeti':'21-8-2002','sheetal':'10-8-2004'}
# a=open('max-file.txt','a')
# for k,v in d.items():
#     a.write(k+': ')
#     a.write(str(v)+'\n')
# a.close()
    
# **********************************************************************
# 12. Write a Python program to write a list to a file.
# p=open('list.txt','w')
# l=['1.Pinki','2.Rinki','3.Kiran','4.Ansh','5.Abhi']
# for i in l:
#     p.write(i+'\n')
# p.close()

# ******************************************************************
# 13. Write a Python program to copy the contents of a file to another file .
# a=open('abc.csv','a')
# b=open('ret.txt','r')
# for i in b:
#     a.write(i+'\n')
# a.close()
# b.close()

# *******************************************************************
# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
# a=open('ret.txt','a')
# b=open('list.txt','r')
# c=open('max-file.txt','r')
# p=b.readlines()
# q=c.readlines()
# for i in range(len(p)):
#     r=p[i]+q[i]
#     a.write(r.replace('\n','')+'\n')
# a.close()
# b.close()
# c.close()

# *****************************************************************************
# 15. Write a Python program to read a random line from a file.
# import random
# a=open('assig.txt','r')
# files=a.read().splitlines()
# print(random.choice(files))
# a.close()

# ************************************************************************
# 16. Write a Python program to assess if a file is closed or not.
# p=open('assig.txt','r')
# print(p.closed)
# p.close()
# print(p.closed)

# ******************************************************************
# 17. Write a Python program to remove newline characters from a file.
# o=open('list.txt','r')
# a=o.readlines()
# i=0
# for j in a:
#     a[i]=j.rstrip('\n')
#     i+=1
# print(a)
# o.close()

# *****************************************************************************
# 18. Write a Python program that takes a text file as input and returns the number of words of a given text file.
# o=open(input("Enter file name : "),'r')
# c=0
# for i in o:
#     l=i.split()
#     c+=len(l)
# print(c)
# o.close()

# *******************************************************************************
# 19. Write a Python program to extract characters from various text files 
#      and put them into a list.


# *****************************************************************************
# 20. Write a Python program to generate 26 text files named 
#     A.txt, B.txt, and so on up to Z.txt.
# i=65
# while i<=90:
#     open(chr(i)+'.txt','w')
#     i+=1
    
#    ***********   TO REMOVE FILES   **********************
# import os
# i=65
# while i<=90:
#     os.remove(chr(i)+'.txt')
#     i+=1

# *******************************************************************
# 21. Write a Python program to create a file where all letters of the English 
# alphabet are listed by specified number of letters on each line.
# p=open('alpha.txt','w')
# i=1
# while i<=26:
#     p.write(str(i)+" => "+chr(i+64)+'\n')
#     i+=1
# p.close()

# *********************************************************************************
