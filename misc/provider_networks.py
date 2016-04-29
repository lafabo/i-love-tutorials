#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://habrahabr.ru/post/127822/

import re, cymruwhois
from sys import argv, stdin
from iptools import IpRange, IpRangeList


private_nets = IpRangeList("10/8", "172.16/12", "192.168/16")
ip_re = re.compile(r'^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])')

def iprangelistappend(match, rangelist):
  rangelist.ips += (IpRange(match.prefix),)
  return (match.prefix, match.owner)


def main(input):
  ips = sorted(set(ip_re.match(line).group(0) for line in input if ip_re.match(line)))
  ips = filter(lambda ip: ip not in private_nets, ips)
  public_nets = IpRangeList()
  whois = cymruwhois.Client()
  nets = (iprangelistappend(whois.lookup(ip), public_nets) for ip in ips if ip not in public_nets)
  for prefix, owner in nets:
    print prefix, owner


if __name__ == "__main__":
  if len(argv) == 1:
    main(stdin)
  else:
    main(open(argv[2]))