import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

names_1_set = set(names_1)
names_2_set = set(names_2)
duplicates = {name_1 for name_1 in names_1_set if name_1 in names_2_set}

    # for name_2 in names_2:
    #     if name_1 == name_2:
            

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

