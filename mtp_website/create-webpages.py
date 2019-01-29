full_form_dict = {
	'bf' : 'Bathroom Facility',
	'chh' : 'Condition of Household',
	'fc' : 'Fuel for Cooking',
	'emp' : 'Employment',
	'f_emp' : 'Female Employment',
	'msl' : 'Main Source of Light',
	'msw' : 'Main Source of Water',
	'asset' : 'Asset Ownership'
}

for type1 in ['2001', '2011', 'change']:
	for type2 in ['bf', 'chh', 'fc', 'emp', 'f_emp', 'msl', 'msw']:
		main_file = open('trilabel-broadcasting.html', 'r')
		lines = main_file.readlines()
		
		for i in range(119, len(lines)):
			line = lines[i]
			line = line.replace('asset', type2+'_'+type1)
			line = line.replace('Asset Ownership', full_form_dict[type2]+' '+type1.title())
			if type1 == 'change':
				line = line.replace('rudimentary', 'decline')
				line = line.replace('Rudimentary', 'Decline')
				line = line.replace('intermediate', 'no change')
				line = line.replace('Intermediate', 'No Change')
				line = line.replace('advanced', 'increase')
				line = line.replace('Advanced', 'Increase')
			lines[i] = line

		with open(type1+'/'+type2+'.html', 'w') as f:
			f.writelines(lines)
		print(type1+'/'+type2+'.html'+' done.')
	
for type1 in ['spatial']:
	for type2 in ['bf', 'chh', 'fc', 'emp', 'msl', 'msw']:
		if type2 != 'emp':
			type3_list = ['adv', 'rud', 'int']
		else:
			type3_list = ['un', 'al', 'nal']
		for type3 in type3_list:
			main_file = open('spatial-broadcasting.html', 'r')
			lines = main_file.readlines()
			
			for i in range(169, len(lines)):
				line = lines[i]
				line = line.replace('emp_al_spatial', type2+'_'+type3+'_'+type1)
				line = line.replace('EMP_AL', type2.upper()+'_'+type3.upper())
				lines[i] = line
			with open(type1+'/'+type2+'_'+type3+'.html', 'w') as f:
				f.writelines(lines)
			print(type1+'/'+type2+'_'+type3+'.html'+' done.')
		
