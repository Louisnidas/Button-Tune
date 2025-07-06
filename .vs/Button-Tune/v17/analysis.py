import matplotlib.pyplot as plt

# initialise 
filename = "data.csv"
data = [[]]
line = []

# pull data from file
with open(filename) as f:
    for x in f:
        start = 0
        while (start < len-4)
            pos = x.index(",", start)
            data.append(line[start:pos])
            start = pos + 1
data_length = len(data)

print(data)