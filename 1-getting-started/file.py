file=open('record.txt', 'w')

def enter_record():
	name=input('Enter name: ')
	marks=input('Enter marks: ')
	file.write('Name : {}   Marks : {}\n'.format(name, marks))

ch=''	
while(ch!='q'):
	enter_record()
	ch=input('Want to enter more record? ')
	
file.close()

