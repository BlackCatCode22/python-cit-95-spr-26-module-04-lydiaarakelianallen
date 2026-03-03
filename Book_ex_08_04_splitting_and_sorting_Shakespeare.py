# enter: romeo.txt
fname = input("Enter file name: ")
fh = open(fname)

lst = list()

for line in fh:
    line = line.rstrip()
    wds = line.split()

    for wd in wds:
        if wd not in lst:
            lst.append(wd)
lst.sort()
print(lst)