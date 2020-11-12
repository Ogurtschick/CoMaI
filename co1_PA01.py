def roots(a,b,c,d,e,f):
	l = [a*d,b*d+a*e,a*f+b*e+c*d,b*f+c*e,c*f] #c4 bis c0
	pos = True #speichert, ob der letze Wert pos war. Fängt mit True an, da 1*x^5
	vzw = 0 #zählt die Vorzeichenwechsel
	for i in range(5):		
		#print(i,"Das jetztige Listenelement ist ",l[i]," vzw: ",vzw, "pos: ",pos)
		#Wenn l[i-1]>0 und l[i]<0 oder l[i-1]<0 und l[i]>0 gibt es einen VZW
		if (pos==True and l[i] < 0) or (pos==False and l[i] > 0):			
			vzw += 1
			pos = not pos
			#print("WECHSEL vzw: ",vzw, "pos: ",pos)
	if (vzw%2)==0:
		return 'Das Polynom hat eine gerade Anzahl von positiven reellen Wurzeln.'
	elif (vzw%2)==1:
		return 'Das Polynom hat eine ungerade Anzahl von positiven reellen Wurzeln.'