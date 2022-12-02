
max_sum = 0
second_sum = 0
third_sum = 0

current_elf_sum = 0

elfUpdated = False

data_file = open('day1.txt', 'r')
raw_elf_data = data_file.readlines();

for i in range(len(raw_elf_data)):
    
    strippedCalorieCount = raw_elf_data[i].strip();

    if strippedCalorieCount == '' or i == len(raw_elf_data)-1:
        if i == len(raw_elf_data)-1:
            current_elf_sum += int(strippedCalorieCount)
        if current_elf_sum > max_sum:
            third_sum = second_sum
            second_sum = max_sum
            max_sum = current_elf_sum
        elif current_elf_sum > second_sum:
            third_sum = second_sum
            second_sum = current_elf_sum
        elif current_elf_sum > third_sum:
            third_sum = current_elf_sum
        current_elf_sum = 0
    else:
        current_elf_sum += int(strippedCalorieCount)
        

print(max_sum)
print(second_sum)
print(third_sum)

print(max_sum+second_sum+third_sum)
