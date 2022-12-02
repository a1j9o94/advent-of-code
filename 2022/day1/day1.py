
max_sum = 0
current_elf_sum = 0

data_file = open('day1.txt', 'r')
raw_elf_data = data_file.readlines();

for foodCalorieCount in raw_elf_data:
    
    strippedCalorieCount = foodCalorieCount.strip();
    
    if strippedCalorieCount == '':
        current_elf_sum = 0
    else:
        current_elf_sum += int(strippedCalorieCount)
        if current_elf_sum > max_sum:
            max_sum = current_elf_sum

print(max_sum)
