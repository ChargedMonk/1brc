def calculate():
    _min = 100
    _max = -100
    result = {}
    with open("measurements.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        station_val = line.split(';')
        val = float(station_val[1])
        curr_min, curr_sum, curr_max, curr_count = result.get(station_val[0], (_min, 0, _max, 0))
        result[station_val[0]] = (min(val, curr_min), curr_sum + val, max(curr_max, val), curr_count + 1)

    print("{", end="")
    for k, v in result.items():
        print(f'{k}={round(v[0], 1)}/{round(v[1]/v[3], 1)}/{round(v[2], 1)}', end=', ')


calculate()
