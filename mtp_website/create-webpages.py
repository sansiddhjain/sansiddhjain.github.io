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
		main_file = open('bf_adv.html', 'r')
		lines = main_file.readlines()
		
		for i in range(119, len(lines)):
			line = lines[i]
			line = line.replace('asset', type2+'_'+type1)
			line = line.replace('Asset Ownership', full_form_dict[type2]+' '+type1.title())
			if type1 == 'change':
				line = line.replace('rudimentary', 'decline')
				line = line.replace('intermediate', 'no change')
				line = line.replace('advanced', 'increase')
			lines[i] = line

		with open(type1+'/'+type2+'.html', 'w') as f:
			f.writelines(lines)
		print(type1+'/'+type2+'.html'+' done.')
	
