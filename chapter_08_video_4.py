han=open('mbox-short.txt')

for line in han:
    line=line.rstrip()
    wds=line.split()
    #compound guardian statement
    if len(wds)<3 or wds[0] != 'From':
        continue
    # prints the day of the week
    print(wds[2])