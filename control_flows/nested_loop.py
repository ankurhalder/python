import time
start_time = time.time()

# outer loop
for i in range(100):
    # inner loop
    for j in range(10000):
        print(0, end=" ")
    print()

print("--- %s seconds ---" % (time.time() - start_time))