import random
# import ipaddress
import sys
from os.path import exists
# import geoip2.database

# ranges = \
# """173.245.48.0/20
# 103.21.244.0/22
# 103.22.200.0/22
# 103.31.4.0/22
# 141.101.64.0/18
# 108.162.192.0/18
# 190.93.240.0/20
# 188.114.96.0/20
# 197.234.240.0/22
# 198.41.128.0/17
# 162.158.0.0/15
# 104.16.0.0/13
# 104.24.0.0/14
# 172.64.0.0/13
# 131.0.72.0/22""".split()
# ranges = ['172.64.0.0/13']
# _, num_server = sys.argv
# num_server = int(num_server)

# if not exists('ips.txt'):
#     with open('ips.txt', 'w') as f:
#         for iprange in ranges:
#             for ip in ipaddress.IPv4Network(iprange):
#                 f.write(str(ip) + '\n')

# with open('ips.txt', 'r') as f:
#     ips = f.readlines()
#     ips = [ip.strip() for ip in ips]

# ips = random.choices(ips, k=200000)
#
# with geoip2.database.Reader('./GeoLite2-Country.mmdb') as reader:
#     def f(ip):
#         try:
#             code = reader.country(ip).country.iso_code
#             if code == 'HK' or code == 'CN' or code == 'MO':
#                 print(code)
#                 return True
#             return False
#         except:
#             return False
#     ips = list(filter(f, ips))
#
# print(f'len(ips)={len(ips)}')

with open("result.csv", encoding='utf-8') as f:
    ips = [row.split(',')[0] for row in f.readlines()[1:]]

# ips = random.choices(ips, k=min(num_server, len(ips)))

config = ''
for i, ip in enumerate(ips):
    config += '    server server' + \
        str(i) + ' ' + ip.strip() + ':443 check observe layer4\n'

config = \
    """global
    log 127.0.0.1 local0 notice

defaults
    log global
    mode tcp
    balance roundrobin
    timeout connect 5s
    timeout client 5s
    timeout server 5s
    option redispatch
    option dontlognull
    retries 3
    maxconn 20480

frontend main
    bind *:40498
    default_backend ss-server

backend ss-server
""" + config
with open('haproxy.cfg', 'w+') as f:
    f.write(config)
