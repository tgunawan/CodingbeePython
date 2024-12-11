#-------- Library--------
import os
import numpy as np


#--------- variable------
nama='Tedi Gunawan'
buah=['apel','pisang','anggur']
list=[]


#-------- Function ------


#-------- Main Program ----
for char in nama:
    print(char)
    list.append(char)

print(list)

for i in range(len(buah)):
    print(f'{i+1} . {buah[i]}')

for i,fruit in enumerate(buah):
    print(f'{i+1} . {fruit}')

#end