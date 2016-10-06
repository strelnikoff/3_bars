import json
import os
import sys


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    return max(data, key=lambda x:x["Cells"].get("SeatsCount"))


def get_smallest_bar(data):
    return min(data, key=lambda x:x["Cells"].get("SeatsCount"))


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda x:calculate_distance(get_point(x), [longitude, latitude]))


def calculate_distance(point_one, point_two):
    return ((point_one[0]-point_two[0])**2 +
            (point_one[1]-point_two[1])**2)**(1/2)


def get_point(bar):
    return bar["Cells"].get("geoData").get("coordinates")


def get_param(argv):
    minimal = {"--minimal", "-m"}
    biggest = {"--biggest", "-b"}
    wathit = {"--help", "-h"}
    closest = {"--closest", "-c"}
    file_error = "Файл не найден, для справки используйте ключ -h\n"
    key_error = "Не опознанный ключ, для справки используйте ключ -h\n"
    manual = "Данный скрипт предназаначен для получения информации \
o барах в виде json документа \
\n--minimal, -m \t- возвращает json документ с наименьшим баром \
по колличеству мест\
\n\t bars.py -m bars_list.json\
\n--biggest, -b \t- возвращает json документ с наибольшим баром \
по колличеству мест\
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
