L1 = []
ch = 1
while ch == 1:
	print ("""Select one of the following options: 
	1: Push
	2: Pop
	3: Display
	4: Exit""")	
	choice = 0
	choice = int(input("What you want to do"))

	if choice == 1:
		L1.append (int(input ("Enter item in list-1")))
		print("Pushed element is", L1[-1])
	elif choice == 2:
		if L1 !=[]:		
			p = L1.pop()
			print ("Popped element is ", p)
		else:
			print("there is no element")
	elif choice == 3:
		print ("First list is: ", L1)
	else:
		exit()
	ch = int(input(" Do you want to continue, press 1"))
