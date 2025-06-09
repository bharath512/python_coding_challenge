import random

subnet_range_in = input("Enter first 2 octet for subnet as you wish to generate [Like: 192.168 ]: ")
subnet_range = subnet_range_in.split(".")

for i in range(1000):
    if len(subnet_range_in) <= 7:
        if int(subnet_range[0]) <=255 and int(subnet_range[1])<= 255:
            random_ip = f"{subnet_range_in}.{random.randrange(0, 255, 1)}.{random.randrange(0, 255, 1)}"
            print(f"{random_ip} is added to random_ip.txt file")
            with open('random_ip.txt', 'a') as file:
                file.write(f"{random_ip}\n")
        else:
            print("Entered value is not subnet, subnet ranges between [0-255].[0-255]")
            break
    else:
        print("Entered input has more than 6 number, which is not idle for first 2 Octet")
        break