import re, pyperclip as pc

#getting copied data in our program
text=pc.paste()

#making regex objects for different properties
name=re.compile(r'^([A-Z][a-z]+)( [A-Z]+\.)?( [A-Z][a-z]+)?', re.MULTILINE)     
phone=re.compile(r'(\+\d{2} )?(\d{10})')
email=re.compile(r'''
		[a-z0-9.-_]+
		@
		[a-z0-9]+
		\.[a-zA-Z]{2,4}''',
		re.VERBOSE | re.IGNORECASE)

#finding appropriate feilds
name_match=name.findall(text)
phone_match=phone.findall(text)
email_match=email.findall(text)
	
def write_to_file():
	with open('records.txt', 'w') as file:
		i=0
		while(i!=len(name_match)):
			#if we don't have these values we will assign it to NA
			mid_name='NA' if name_match[i][1]=='' else name_match[i][1]
			las_name='NA' if name_match[i][2]=='' else name_match[i][2]
			con_code='NA' if phone_match[i][0]=='' else phone_match[i][0]
			#writing it to file
			file.write('Record {}:\n\tFirst Name: {}\n\tMiddle name: {}\n\tLast Name: {}'.format(i+1, name_match[i][0], mid_name, las_name))
			file.write('\n\tCountry Code: {}\n\tPhone number: {}\n'.format(con_code, phone_match[i][1]))
			file.write('\tEmail id: {}\n'.format(email_match[i]))
			i+=1
		print('Successfully created a new records file')

if len(name_match)!=0:
	write_to_file()
	

#print('Names: ', name_match)
#print('Phone no: ', phone_match)
#print('Email: ',email_match)
