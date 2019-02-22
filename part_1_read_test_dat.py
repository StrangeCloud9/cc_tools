import cc_dat_utils

#Part 1
input_dat_file = "data/pfgd_test.dat"

#Use cc_dat_utils.make_cc_data_from_dat() to load the file specified by input_dat_file
data = cc_dat_utils.make_cc_data_from_dat(input_dat_file)
#print the resulting data
print (type(data))
print (data)

#save content
save_file_name = "data/pfgd_test.txt"
save_file = open(save_file_name, "w")
save_file.write(str(data))
save_file.close()