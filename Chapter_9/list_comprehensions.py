input_strings = ['1', '5', '28', '131', '3']
output_inteers = []
for num in input_strings:
    output_inteers.append(int(num))

input_strings = ['1', '5', '28', '131', '3']
output_inteers = [int(num) for num in input_strings]

output_ints = [int(n) for n in input_strings if len(n) < 3]