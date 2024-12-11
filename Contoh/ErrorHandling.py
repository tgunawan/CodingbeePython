#------------library-----------
import os,math
import function
#------------Variables-----------
number=0
#------------Functions-----------

#------------Main----------------
os.system('cls')
try:
    number=int(input("number: "))
    bagi=int(input("bagi: "))
    if number==1:
        raise ZeroDivisionError
    hasil=number/bagi
    print(hasil)

# '''except ValueError:

#     print("Error Huruf")

# except ZeroDivisionError:

#     print("Error 0")'''

# except Exception as e:
#     print('Error',e)

except ZeroDivisionError:
    print("Error 0")


else:
    print('Benar')
finally:
    print('pasti jalan')
#------------End Main------------