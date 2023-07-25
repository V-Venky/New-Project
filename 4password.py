q, w, e, r = 0, 0, 0, 0
m = input("Enter your password: ")
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_#%^&*()[\]{}|;:></?"
digits="0123456789"
if (len(m) >= 8):
	for i in m:
		if (i in smallalphabets): 
			q+=1		
		elif (i in capitalalphabets):  
			w+=1	 
		elif (i in digits): 
			e+=1	
		elif(i in specialchar): 
			r+=1 
if (q>=1 and w>=1 and e>=1 and r>=1 and q+w+e+r==len(m)):
	print("Valid Password")
	print("small alphabets are",q)
	print("capital alphabets are",w)
	print("digits are",e)
	print("special characters are",r)
else:
	print("Invalid Password")
