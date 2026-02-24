# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    value = float(line[19:])
    count = count + 1
    total = total + value
print("Average spam confidence:", total / count)