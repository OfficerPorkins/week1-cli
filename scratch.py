with open("demo.txt", "w") as f:
    f.write("buy milk\n")
    f.write("call mom\n")

with open ("demo.txt", "r") as f:
    for line in f:
        print(line)
        