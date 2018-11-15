import time,os
from _socket import *
#COLORS============#
blue = '\033[94m'  #
green = '\033[32m' #
red = '\033[91m'   #
w = '\033[0m'      #
#==================#
os.system("cls")
time.sleep(1)
print(blue+"\n[*]"+red+":"+green+"Checking Internet Connection...........")
REMOTE_SERVER = "www.google.com"
def is_connected():
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
if is_connected() == True:
    print(blue+"\n[+]"+red+":"+green+"[ Connected ]")
    time.sleep(2)
    os.system("cls")
elif is_connected() == False:
    print(red+"\n[!]"+green+"Your Not Connected To The Internet !!")
    print(blue+"[*]"+red+":"+green+"Please Connect To The Internet And Try Again :)")
    time.sleep(4)
    exit()
l = open("l.txt","r")
lo = l.read()
print(red+lo+"\n")
print(green+"============="+red+"Deeb will love you :)"+green+"============="+"\n")
print(blue+"[---]\t by:>"+red+" WAleed Deeb\t"+blue+"[---]")
print(blue+"[---]\t Version:>"+red+" 1.5\t        "+blue+"[---]\n")
print(blue+"\n\n[*]"+red+green+"1-Analyst Date\n"+blue+"\n\n[*]"+red+green+"2-Attake wesite\n"+blue+"\n\n[*]"+red+green+"4-Scan router\n")
q =input(blue+"\n\n[*]"+red+":"+green+"waht Do you want"+w+":"+blue+"~"+w+"# "+red)
if q == "1":
    import analysdate

elif q=="2":
    import atrakewebsite

elif q=="3":
    import scannetwork