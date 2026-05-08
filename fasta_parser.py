# FASTA Parser Practice
# Future project for biological sequence parsing

filename = "sample.fasta"

with open(filename, "r") as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()

    if line == "":
        continue
    
    if line.startswith(">"):
        print(f"Header: {line}")
    
    else:
        length = len(line)

        g_count = line.count("G")
        c_count = line.count("C")

        gc_content = (g_count + c_count) / length * 100

        if gc_content >= 60:
            status = "GC-rich"
        elif gc_content >= 40:
            status = "Normal"
        else:
            status = "AT-rich"

        print(f"Sequence: {line}")
        print(f"Length: {length}")
        print(f"GC Content: {gc_content:.2f}%")
        print(f"Status: {status}")

        print("-" * 30)

        

