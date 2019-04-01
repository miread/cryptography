def encrypt(contents, key):
    result = ""
    for n in range(1, key + 1):

        # First rail follows a simple distance formula
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

        # Middle rails are written twice per "cycle", alternating distances
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

        # Last rail is like the first, but offset
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
    dict = {}
    content_length = len(contents)
    cycle = 2 * key - 2
    num_of_cycles = int(content_length / cycle)
    remainder = content_length % cycle

    # Middle rails are twice as long
    for n in range(1, key + 1):
        if n == 1 or n == key:
            dict[n] = num_of_cycles
        if n > 1 and n < key:
            dict[n] = num_of_cycles * 2

    # A partial cycle must be counted, too
    for i in range(1, remainder + 1):
        if i <= key:
            dict[i] += 1
        if i > key:
            dict[2 * key - i] += 1

    # We will replace the count with the actual contents of each rail
    count = 0
    for n in range(1, key + 1):
        dict[n], count = contents[count:count + dict[n]], count + dict[n]

    # Reversed list form for efficient popping
    for n in range(1, key + 1):
        dict[n] = list(reversed(dict[n]))

    # Pop the rails one-by-one, in order
    output = ""
    count = 1
    path = "down"
    for i in range(0, content_length):
        output += dict[count].pop()
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
