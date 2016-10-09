import json, os, argparse


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, mode='r', encoding='utf-8') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(args):
    data = load_data(args.file)
    return max(data, key=lambda x:x["Cells"].get("SeatsCount"))


def get_smallest_bar(args):
    data = load_data(args.file)
    return min(data, key=lambda x:x["Cells"].get("SeatsCount"))


def get_closest_bar(args):
    data = load_data(args.file)
    return min(data, key=lambda x:calculate_distance(get_point(x), [args.longitude, args.latitude]))


def calculate_distance(point_one, point_two):
    return ((point_one[0]-point_two[0])**2 +
            (point_one[1]-point_two[1])**2)**(1/2)


def get_point(bar):
    return bar["Cells"].get("geoData").get("coordinates")


def parse_args():
    parser = argparse.ArgumentParser(description='Bar json utility')
    subparsers = parser.add_subparsers()
    parser.add_argument('file', type = str, help = 'Json file with bars')

    parser_biggest = subparsers.add_parser('biggest', help = 'Rerurn biggest bar')
    parser_biggest.set_defaults(func = get_biggest_bar)

    parser_smallest = subparsers.add_parser('smallest', help = 'Rerurn smallest bar')
    parser_smallest.set_defaults(func = get_smallest_bar) 

    parser_closest = subparsers.add_parser('closest', help = 'Rerurn closest bar')
    parser_closest.add_argument('longitude', type = float, help = 'you longitude')
    parser_closest.add_argument('latitude', type = float, help = 'you latitude')
    parser_closest.set_defaults(func = get_closest_bar)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.func(args))
