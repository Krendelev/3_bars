import json
import argparse


def load_data(filepath):
    with open(filepath) as file_handler:
        return json.load(file_handler)['features']


def get_biggest_bar(bar_data):
    return max(
        bar_data,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_smallest_bar(bar_data):
    return min(
        bar_data,
        key=lambda x: x['properties']['Attributes']['SeatsCount']
    )


def get_distance(bar_data, longitude, latitude):
    longitude2, latitude2 = bar_data['geometry']['coordinates']
    return ((longitude2 - longitude) ** 2 + (latitude2 - latitude) ** 2) ** 0.5


def get_closest_bar(bar_data, longitude, latitude):
    return min(bar_data, key=lambda x: get_distance(x, longitude, latitude))


def print_bar(feature, bar):
    print(
        feature,
        '{0},'.format(bar['properties']['Attributes']['Name']),
        'мест: {0}'.format(bar['properties']['Attributes']['SeatsCount']),
        '\nАдрес: {0}'.format(bar['properties']['Attributes']['Address']),
    )
    return None


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('longitude', type=float, nargs='?')
    parser.add_argument('latitude', type=float, nargs='?')
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    try:
        bar_list = load_data(args.file)
    except FileNotFoundError:
        print('File not found')
    except json.decoder.JSONDecodeError:
        print('Please specify valid JSON file')
    else:
        print_bar(
            'Самый большой бар:',
            get_biggest_bar(bar_list)
        )
        print_bar(
            'Самый маленький бар:',
            get_smallest_bar(bar_list)
        )
    if args.longitude and args.latitude:
        print_bar(
            'Самый близкий бар:',
            get_closest_bar(bar_list, args.longitude, args.latitude)
        )
