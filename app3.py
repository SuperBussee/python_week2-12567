num_string = '12.25'
num_integer = 23

print('Data Type casting:', type(num_string))
#explicit type conversion
num_string = float(num_string)
print('Data Casting:', type(num_string))

num_sum = num_integer + num_string
print(f'Sum:num_sum', type(num_sum))