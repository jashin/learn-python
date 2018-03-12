
path = "/Users/steven/Downloads/nys/"

inFilename = path + "Contacts-2.csv"
outFilename = path + "Contacts-2_with_email.csv"
i = 0

with open(outFilename, 'w') as fout:
  with open(inFilename, 'r') as fin:
    for line in fin:
      if i == 0:
        line = line[0:len(line) - 2] + ",Email Address 1"  # remove \r\n at the end
      else:
        line = line[0:len(line) - 2] + ",Email_" + str(i) + "@backpostfix.everbridge.net"
      i += 1
      fout.write(line + '\n')

  fout.close()