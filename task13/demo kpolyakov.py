from ipaddress import ip_network

net = ip_network('117.32.0.0/255.224.0.0', False)
k = 0
for ad in net.hosts():
    if len(set(str(ad).split('.'))) == 3:
        k += 1
print(k)