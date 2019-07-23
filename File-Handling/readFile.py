with open("test.txt", "r") as handle:
        data = handle.read().split()
        counter = 0
        for word in data:
            if word == "Ipsum":
                counter += 1
                
print(counter)