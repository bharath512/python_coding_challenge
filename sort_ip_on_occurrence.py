import re

with open('random_ip.txt', 'r') as file:
    ip_string = file.readlines()

lst = []
ip_pattern = (r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
for lines in ip_string:
    ip_search = re.findall(ip_pattern, lines)
    lst.extend(ip_search)

ip_count = {}
for ips in lst:
    ip_count[ips] = ip_count.get(ips, 0)+1
    sorted_ip_list = sorted(ip_count.items(), key=lambda item: (-item[1],item[0]))

for sorted_ip in sorted_ip_list:
    print(sorted_ip)