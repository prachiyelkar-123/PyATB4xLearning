# try :
#     # Try this code , if error
# except:
#     # Excute me if try has some error



import math
try:
    math.exp(1000) #OverflowError: math range error
except Exception as e:
    print(e)
    print("Please try to use the lower exp value")