import random
import json
import ipaddress
import copy

ranges = \
    """173.245.48.0/20
    103.21.244.0/22
    103.22.200.0/22
    103.31.4.0/22
    141.101.64.0/18
    108.162.192.0/18
    190.93.240.0/20
    188.114.96.0/20
    197.234.240.0/22
    198.41.128.0/17
    162.158.0.0/15
    104.16.0.0/12
    172.64.0.0/13
    131.0.72.0/22""".split()
# ranges = ['104.16.0.0/12']
num_server = 500
full_config = {
    "strategy": "com.shadowsocks.strategy.ha",
    "index": -1,
    "portableMode": True
}

ips = []
for iprange in ranges:
    for ip in ipaddress.IPv4Network(iprange):
        ips.append(str(ip))

with open('template.json', 'r') as f:
    template = json.load(f)


def mk_new_server(ip):
    template0 = copy.copy(template)
    template0['server'] = ip
    return template0


configs = list(map(mk_new_server, random.choices(ips, k=num_server)))
full_config['configs'] = configs

with open('gui-config.json', 'w+') as f:
    f.write(json.dumps(full_config, indent=4))
