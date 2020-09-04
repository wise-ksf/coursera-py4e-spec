# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# problem stem:
# name = input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
# handle = open(name)

# solution
d = dict()
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
for line in handle:
  if line == '\n':
    continue
  linelist = line.split()
  if linelist[0] == 'From':
    d[linelist[1]] = d.get(linelist[1], 0) + 1
largestkey = None
largestvalue = 0
for key, value in d.items():
  if value > largestvalue:
    largestkey = key
    largestvalue = value
print(largestkey, largestvalue)

