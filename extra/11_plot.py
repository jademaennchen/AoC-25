from pyvis.network import Network

devices = {l[:3]: l[5:].strip().split() for l in open('input/11.txt').readlines()}
print(devices)

net = Network(directed=True, select_menu = True, filter_menu = True)
net.add_nodes(list(devices.keys()) + ['out'])
for device in devices:
    for next in devices[device]: net.add_edge(device, next)
net.toggle_physics(True)
net.show("AoC_25_11.html", notebook=False)
