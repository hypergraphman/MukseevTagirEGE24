from ipaddress import ip_network

net = ip_network('212.192.32.96/255.255.255.224', False)
k = 0
for host in net.hosts():
    t = f'{int(host):b}'[-8:]
    if '000' not in t and '111' not in t:
        print(t)
print(k)