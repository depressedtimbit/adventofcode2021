fileobj=open("list.txt")
input_list=[]
for line in fileobj:
    input_list.append(line.strip())

gamma_binary = str("")
epsilon_binary = str("")

def cal_digit(seek, test):
    common = 0
    for item in input_list:
        digit = int(item[seek])
        if digit == test:
           common += 1
        else:
           common -= 1
    return common

for item in range(len(input_list[0])):
    digit = cal_digit(item, 1)
    if digit > 1:
        gamma_binary += str(1)
    else:
        gamma_binary += str(0)

for item in range(len(input_list[0])):
    digit = cal_digit(item, 0)
    if digit > 1:
        epsilon_binary += str(1)
    else:
        epsilon_binary += str(0)

print(int(gamma_binary, 2))

print(int(epsilon_binary, 2))
consumption = int(gamma_binary, 2) * int(epsilon_binary, 2)
print(consumption)