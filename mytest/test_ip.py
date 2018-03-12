import ipaddress
import re

block = u'asdf/16'
address = re.match(r'\d+\.\d+\.\d+\.\d', block)
print address
if ipaddress.ip_address(address.group()).is_private:
  print re.match(r'\d+\.\d+\.\d+\.\d+/\d+', block)
else:
  print "error"