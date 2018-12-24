import os

list_of_states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']


for metric in ['tail_3mon', 'tail_6mon', 'tail_1yr', 'tail_3yr', 'mean', 'coeff_of_var', 'kl', 'zero', 'n_hearings', 'time_bw_hearings']:
	for state in list_of_states:
		file = open('GeoJSON_Files/gadm_districts_'+metric+'.geojson', 'r')
		all_lines = file.readlines()
		write_file = all_lines[:4]
		for i in range(len(all_lines)):
			if (state in all_lines[i]):
				write_file = write_file[:] + [all_lines[i]]
		write_file[len(write_file) - 1] = write_file[len(write_file) - 1][:-2] + write_file[len(write_file) - 1][-1:]
		write_file = write_file[:] + all_lines[-2:]

		state = state.replace(' ', '_')
		state = state.lower()

		with open('states_pages/'+state+'/GeoJSON_Files/'+state+'_districts_'+metric+'.geojson', 'w') as f:
			f.writelines(write_file)
	print metric + ' done.'