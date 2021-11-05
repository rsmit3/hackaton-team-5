import json

def parse(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    lines = [line.strip().split(' ') for line in lines]

    frame = []
    S_index = []
    for line_index, line in enumerate(lines):
        line_array = []
        for i in range(0, len(line), 2):
            k, v = line[i].strip(':'), line[i+1]

            if k == 'S':
                S_index.append(line_index)
                continue

            line_array.append(float(v))

        frame.append(line_array)

    json_out = {}
    for i in range(len(S_index) - 1):
        rotation = frame[S_index[i]:S_index[i + 1]]
        json_out[i] = rotation

    return json_out


if __name__ == '__main__':
    data = parse('data/LidarData2.txt')

    with open('data/LidarData.json', 'w') as f:
        f.write(json.dumps(data, indent=2))