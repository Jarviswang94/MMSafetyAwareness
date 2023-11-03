import os
dir = 'dataset/unsafe'
#filenames=os.listdir(dir)
filenames=[os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser('dataset')) for f in fn]

for file in filenames:
	prompt = file.split('/')[-1]
	if prompt[0] == '.':
		continue



	

	#os.system("rename 's/\'//g' " + '/'.join(file.split('/')[:-1]) + '/*')
	#continue
	'''
	if ' ' in file:
		print(file)
	continue
	


	if "\'" in file:
		print(file)
	continue


	if prompt[0].islower():
		#print(file)
		#continue
		filenew = '/'.join(file.split('/')[:-1]) + '/' + prompt[0].upper() + prompt[1:]
		


		#print(file)
		#print(filenew)
		#print('\n\n')
		#continue
		
		#print(file)
		#print(filenew)
		#print('\n\n')
		#print('mv ' + file + ' ' + filenew)
		#continue

		try:
			os.system("mv " + file + " "  + filenew)
			#print('success')
		except:
			print(file)
			print(filenew)
			print('fail')
		#print(prompt)
	#print(file.split('/')[-1])
	'''
#print(filenames)
