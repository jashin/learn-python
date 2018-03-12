import gnupg

dev_public = ''
with open('dev_public.key', 'r') as f:
  dev_public = f.read()

# prod_public = ''
# with open('prod_public.key', 'r') as f:
#   prod_public = f.read()

# print dev_public

gpg = gnupg.GPG(gnupghome='/Users/steven/Development/Files/atlas/gpghome_encryption', gpgbinary='/usr/local/Cellar/gnupg@1.4/1.4.22/bin/gpg1')

import_result = gpg.import_keys(dev_public)

# print import_result.results

public_keys = gpg.list_keys()

# print public_keys

# encrypted_ascii_data = gpg.encrypt(str(decrypted_data), 'nobody@everbridge.com')
encrypted_ascii_data = gpg.encrypt('stageus3r', 'nobody@everbridge.com', always_trust=True)

print encrypted_ascii_data.ok
print encrypted_ascii_data.status
print str(encrypted_ascii_data)