# read file line by line

with open("records/standing-desk_logs.hex") as f:
    lines = f.readlines()
    print(lines)

for line in lines:
    line = line.strip()
    packages = line.split(":")
    line_binary = ""
    for package in packages:
        # hex string to bits
        hex_ = int(package, 16)
        print(bin(hex_)[2:])
        bits = bin(int(package, 16))[2:].zfill(8)
        print(bits)
        line_binary += bits
    print(line_binary)

    if "00000001000000" in line_binary:
        print(line_binary)
        print(line_binary[-8:])
        print(int(line_binary[-8:], 2))