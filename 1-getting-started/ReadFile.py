import re

with open('record.txt', 'r') as file:
	li=file.readlines()
	lar=0
	name=''

	obj=re.compile(r'Name : (.*)  Marks : (.*)')
	for entry in li:
		grp=obj.search(entry)
		print(grp.group(1))
		print(grp.group(2))
		




#	for entry in li:
#		marks=re.findall('\d\d*',entry)     #(pattern, string)
#		if int(marks[0]) > lar:
#			lar=int(marks[0])
#			s=re.search('Name : ', entry)
#			e=re.search('Marks', entry)
#			name=entry[s.end():e.start()]


	#print(f'Heighest marks is {lar} secured by {name}')


#the heighest score was 40
#find -> \d\d    -> 40
#search -> '40'
#obj.group() -> 40
#obj.start()  -> starting index
#obj.end() -> ending index
#obj.span()  -> (start, end)


#for entry in li:
#	marks=int(entry[-3:-1])
#	if marks>lar:
#		lar=marks
#		name=entry[7:]
	
#print(name.split(' ')[0])
#print(lar)	
