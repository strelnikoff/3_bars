import json
import os
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    temp_big = []
    for bar in data:
        if not temp_big or get_SeatsCount(temp_big[0]) \
                < bar["Cells"].get("SeatsCount"):
            temp_big.clear()
            temp_big.append(bar)
        elif temp_big and get_SeatsCount(temp_big[0]) \
                == bar["Cells"].get("SeatsCount"):
            temp_big.append(bar)
    return temp_big


def get_smallest_bar(data):
    temp_small = []
    for bar in data:
        if not temp_small or get_SeatsCount(temp_small[0]) > \
                bar["Cells"].get("SeatsCount"):
            temp_small.clear()
            temp_small.append(bar)
        elif temp_small and get_SeatsCount(temp_small[0]) \
                == bar["Cells"].get("SeatsCount"):
            temp_small.append(bar)
    return temp_small


def get_closest_bar(data, longitude, latitude):
    temp_closest = None
    temp_distance = None
    for bar in data:
        if temp_closest is None or temp_distance > \
                calculate_distance(get_point(bar), [longitude, latitude]):
            temp_closest = bar
            temp_distance = calculate_distance(get_point(temp_closest), \
                [longitude, latitude])
    return temp_closest


def calculate_distance(point_one, point_two):
    return ((point_one[0]-point_two[0])**2 +
            (point_one[1]-point_two[1])**2)**(1/2)


def get_point(bar):
    return bar["Cells"].get("geoData").get("coordinates")


def get_SeatsCount(bar):
    return bar.get("Cells").get("SeatsCount")


def get_param(argv):
    minimal = {"--minimal", "-m"}
    biggest = {"--biggest", "-b"}
    wathit = {"--help", "-h"}
    closest = {"--closest", "-c"}
    file_error = "Файл не найден, для справки используйте ключ -h\n"
    key_error = "Не опознанный ключ, для справки используйте ключ -h\n"
    manual = "Данный скрипт предназаначен для получения информации \
o барах в виде json документа \
\n--minimal, -m \t- возвращает json документ со списком \
наименьших баров по колличеству мест\
\n\t bars.py -m bars_list.json\
\n--biggest, -b \t- возвращает json документ со списком \
наибольших баров по колличеству мест\
\n\t bars.py -b bars_list.json\
\n--closest, -c \t- возвращает json документ с ближайшим баром \
относительно координат заданных в виде float числа\
\n\t bars.py -c 50.706200 51.300010 bars_list.json\
\n--help, -h \t- показывает эту справку\
\n\t bats.py -h\n"

    if len(argv) == 3 and argv[1] in minimal:
        data = load_data(argv[2])
        if data is not None:
            return get_smallest_bar(data).__str__()
        else:
            return file_error
    elif len(argv) == 3 and argv[1] in biggest:
        data = load_data(argv[2])
        if data is not None:
            return get_biggest_bar(data).__str__()
        else:
            return file_error
    elif len(argv) == 5 and argv[1] in closest:
        data = load_data(argv[4])
        if data is not None:
            x = float(argv[2])
            y = float(argv[3])
            if x is not None and y is not None:
                return get_closest_bar(data, x, y).__str__()
            else:
                return key_error
        else:
            return file_error
    elif len(argv) == 2 and argv[1] in wathit:
        return manual
    else:
        return key_error + manual


if __name__ == '__main__':
    print(get_param(sys.argv))
