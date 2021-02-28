#!/usr/bin/python

import sys
import urllib
import json


def split(a, n):
    k, m = divmod(len(a), n)
    #    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))
    return (a[i * n + min(i, m):(i + 1) * n + min(i + 1, m)] for i in range(n))


geo_API_url = 'http://api.ipstack.com/'
geo_API_key = '4f90bf0da6f5f385c7d6513c18eeecf8'

#ip_addresses = '{' + sys.argv[1] + '}'
#print(sys.argv[1])
ip_addresses = sys.argv[1]
#ip_addresses = sys.argv[1].split('\n')
# ip_addresses = ip_addresses[:-1]
#print(type(ip_addresses))
# print(ip_addresses[-1])
# print('"{' + ip_addresses + '}"')
# print(ip_addresses.replace('\n', ''))
d = dict(x.split(':') for x in ip_addresses.split('\n'))
#print(d.items())
# k, v = d.items()
# print(k, v)
d1 = {k: int(v) for k, v in d.items()}
# print(d1)
# ds = {
#     k: v
#     for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)
# }
ips_sorted = sorted(d1.items(), key=lambda x: x[1], reverse=True)
num_ips = len(ips_sorted)

# d = eval('"{' + ip_addresses + '}"')
# exit
# for ip_set in split(ip_addresses, 50):
# ip_string = ','.join(ip_set)
# full_API_url = geo_API_url + ip_string + '?access_key=' + geo_API_key
# print(ip_string)
# print(full_API_url)

#    import urllib.request
#    with urllib.request.urlopen('http://python.org/') as response:
# html = response.read()
#     print(html)
# exit
