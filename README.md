# ss-ha-config-gen
Shadowsocks High-Availability multi-IP config file generation scripts for CDN

These scripts generate a shadowsocks config file that include servers with IPs randomly selected from specified ipranges and set to high availablity mode. This comes in handy when you are using CDN like Cloudflare.


-----------------------------------
## win.py

For shadowsocks-windows. Before run, include a "template.json" in the same folder as the template ss server config. It should have the same format as the shadowsocks-windows server config except you don't need the "server" field.

Customize at the begining of file:
- ranges: ip ranges to use
- num_server: number of servers created
- full_config: other configuration that windows ss client can read

-----------------------------------
## haproxy.py

For haproxy (Linux and macos). 

Customize at the begining of file:
- ranges: ip ranges to use
- num_server: number of servers created