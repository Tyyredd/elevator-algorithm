import random

def script_1():
    start = random.randint(0, 10)
    finish = random.randint(0, 10)
    while start == finish:
        finish = random.randint(0, 10)

    return start, finish

def script_2():
    if random.random() < 0.7:
        start = random.randint(4, 10)
        finish = 0
        return start, finish
    return script_1()

def script_3():
    if random.random() < 0.7:
        start = 0
        finish = random.randint(1, 10)
        return start, finish
    return script_1()

# Stays on the floor
def scenario_1(data):
    floors = 0
    prev_stop = data[0][0]
    for start, stop in data:
        offset = abs(start - prev_stop)
        floors += abs(start - stop) + offset
        prev_stop = stop
    return floors

# Returns to the bottom
def scenario_2(data):
    floors = 0
    for start, stop in data:
        floors += start + abs(start - stop) + stop
    return floors

# Returns to 5th floor if elevator ends on the 10th floor
def scenario_3(data):
    floors = 0
    prev_stop = data[0][0]
    default_floor = lambda f: 5 if f == 10 else f
    for start, stop in data:
        start_offset = abs(start - prev_stop)
        stop_offset = abs(stop - default_floor(stop))
        floors += start_offset + abs(start - stop) + stop_offset

        prev_stop = default_floor(stop)
    return floors


def main():
    COUNT = 1000
    DIST = 2.8 / 1000
    data_1 = [script_1() for _ in range(COUNT)]
    data_2 = [script_2() for _ in range(COUNT)]
    data_3 = [script_3() for _ in range(COUNT)]
    data = [data_1, data_2, data_3]

    print('Scenario 1')
    set_1 = [scenario_1(d) * DIST for d in data]
    print(f'1: {"{:.2f}".format(set_1[0])}km')
    print(f'2: {"{:.2f}".format(set_1[1])}km')
    print(f'3: {"{:.2f}".format(set_1[2])}km')
    print(f'Avg: {"{:.2f}".format( sum(set_1)/3)}km')

    print('Scenario 2')
    set_2 = [scenario_2(d) * DIST for d in data]
    print(f'1: {"{:.2f}".format(set_2[0])}km')
    print(f'2: {"{:.2f}".format(set_2[1])}km')
    print(f'3: {"{:.2f}".format(set_2[2])}km')
    print(f'Avg: {"{:.2f}".format( sum(set_2)/3)}km')

    print('Scenario 3')
    set_3 = [scenario_3(d) * DIST for d in data]
    print(f'1: {"{:.2f}".format(set_3[0])}km')
    print(f'2: {"{:.2f}".format(set_3[1])}km')
    print(f'3: {"{:.2f}".format(set_3[2])}km')
    print(f'Avg: {"{:.2f}".format( sum(set_3)/3)}km')

if __name__ == "__main__":
    main()
