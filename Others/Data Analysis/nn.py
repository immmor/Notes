data = {}
with open('brianTXTFiles.txt') as f:
    for line in f:
        parts = line.split('\\')
        group = parts[6]
        folder = parts[7]
        room = parts[9]
        if group not in data:
            data[group] = {folder: {}}
        if room not in data[group][folder]:
            data[group][folder][room] = []
        data[group][folder][room].append(line)

print(data)