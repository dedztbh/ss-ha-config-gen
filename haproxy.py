import random
import ipaddress

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
num_server = 500

ips = []
for iprange in ranges:
    for ip in ipaddress.IPv4Network(iprange):
        ips.append(str(ip))

config = ''
for i, ip in enumerate(random.choices(ips, k=num_server)):
    config += '    server server' + str(i) + ' ' + ip + ':443 check inter 1000 rise 3 fall 1\n'

config = \
"""global
    log 127.0.0.1 local0 notice
    daemon
    nbproc 8

defaults
    log global
    mode tcp
    balance source
    timeout connect 3s
    timeout client 1m
    timeout server 1m

frontend main
    bind *:40498
    default_backend ss-server

backend ss-server
""" + config
with open('haproxy.cfg', 'w+') as f:
    f.write(config)
