def encrypt(contents, key):

    result = ""

    for n in range(1, key + 1):

        if n == 1:
            distance = 2 * key - 3
            count = 0
            for letter in contents:
                if count == 0:
                    result += letter
                if count == distance:
                    count = 0
                else:
                    count += 1

        if n > 1 and n < key:
            distance_down = (2 * key) - (2 * n) - 1
            distance_up = 2 * n - 3
            count = 1 - n
            path = "down"
            for letter in contents:
                if count < 0:
                    pass
                elif count == 0:
                    result += letter
                elif path == "down" and count == distance_down:
                    count = -1
                    path = "up"
                elif path == "up" and count == distance_up:
                    count = -1
                    path = "down"
                count += 1

        if n == key:
            distance = 2 * key - 3
            count = 1 - key
            for letter in contents:
                if count == 0:
                    result += letter
                if count == distance:
                    count = 0
                else:
                    count += 1

    return result


def decrypt(contents, key):
    dict = {}  # Holds length of each rail, then the rail itself
    content_length = len(contents)
    cycle = 2 * key - 2
    num_of_cycles = int(content_length / cycle)
    remainder = content_length % cycle

    # Stores the number of complete cycles for each rail
    for n in range(1, key + 1):
        if n == 1 or n == key:
            dict[n] = num_of_cycles
            #print("Rail " + str(n) + " has " + str(dict[n]) + " complete cycles")
        if n > 1 and n < key:
            dict[n] = num_of_cycles * 2
            #print("Rail " + str(n) + " has " + str(dict[n]) + " complete cycles")

    # Adds partial cycle
    for i in range(1, remainder + 1):
        if i <= key:
            dict[i] += 1
            #print("Rail " + str(i) + " has " + str(dict[i]) + " cycles total")
        if i > key:
            dict[2 * key - i] += 1
            #print("Rail " + str(i) + " has " + str(dict[i]) + " cycles total")

    # Replaces the rail length with the rail contents
    count = 0
    for n in range(1, key + 1):
        dict[n], count = contents[count:count + dict[n]], count + dict[n]
        #print("Rail " + str(n) + ": " + dict[n] + ", count: " + str(count))

    for n in range(1, key + 1):
        dict[n] = list(reversed(dict[n]))
        #print("Rail " + str(n) + " reversed: ", dict[n])

    output = ""
    count = 1
    path = "down"
    for i in range(0, content_length):
        #print(dict[count])
        output += dict[count].pop()
        #print(output)
        if path == "down":
            if count == key:
                path = "up"
                count -= 1
            else:
                count += 1
        elif path == "up":
            if count == 1:
                path = "down"
                count += 1
            else:
                count -= 1

    return output


print(decrypt("WECRLTEERDSOEEFEAOCAIVDEN", 3))
