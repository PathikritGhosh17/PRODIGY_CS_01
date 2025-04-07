ct="";pt="";char=''
opt=input("Enter the task to be done (E for encryption and D for decryption) :- ")
shift=int(input("Enter the shift: "))
if (opt=="E"):
    pt=input("Enter the Plain Text to be encrypted: ")
    length=len(pt)
    for i in range(0,length):
        char=pt[i]
        ct=ct+chr(ord(char)+shift)
    print("The Cipher Text to The Corresponding Plain Text: ",ct)
elif(opt=="D"):
    ct=input("Enter the Cipher Text to be decrypted: ")
    length=len(ct)
    for i in range(0,length):
        char=ct[i]
        pt=pt+chr(ord(char)-shift)
    print("The Plain Text to the Corresponding Cipher Text: ",pt)
else:
    print("Invalid Input")