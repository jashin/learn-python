import gnupg

dev_public = ''
with open('dev_public.key', 'r') as f:
  dev_public = f.read()

dev_private = ''
with open('dev_private.key', 'r') as f:
  dev_private = f.read()

prod_public = ''
with open('prod_public.key', 'r') as f:
  prod_public = f.read()

# print dev_public

gpg = gnupg.GPG(gnupghome='/Users/steven/Development/Files/atlas/gpghome', gpgbinary='/usr/local/Cellar/gnupg@1.4/1.4.22/bin/gpg1')

import_result = gpg.import_keys(dev_private)

# print import_result.results

data = ''

with open('test14.txt', 'r') as f:
  data = f.read()

# print data

decrypted_data = gpg.decrypt(data)

print str(decrypted_data)

import_result = gpg.import_keys(dev_public)

# print import_result.results

# encrypted_ascii_data = gpg.encrypt(str(decrypted_data), 'nobody@everbridge.com')
encrypted_ascii_data = gpg.encrypt('stageus3r', 'nobody@everbridge.com', always_trust=True)

print encrypted_ascii_data.ok
print encrypted_ascii_data.status
print str(encrypted_ascii_data)