# -*- coding: utf-8 -*-
from randgen_maptools import coord_to_1d_index
from randgen_generator_bsp import bsp_rect, tunnel


__author__ = 'Dan Alexander'
__email__ = 'lxndrdagreat@gmail.com'
__version__ = '0.1.0'

"""
Parameter Schema
"""
schema = {
    'width': {
        'type': 'integer',
        'coerce': int,
        'min': 25
    },
    'height': {
        'type': 'integer',
        'coerce': int,
        'min': 25
    },
    'min_size': {
        'type': 'integer',
        'coerce': int,
        'min': 3
    },
    'max_size': {
        'type': 'integer',
        'coerce': int,
        'min': 5
    }
}

schema_default = {
    'width': 50,
    'height': 50,
    'min_size': 5,
    'max_size': 12
}


def connect(node, tiles, map_width, min_cell_width, min_cell_height, rooms, wall=1, floor=0):
    """
    Traverses the BSP tree recursively, connecting leaves.
    """
    if node['top'] and node['bottom']:
        top = connect(node['top'], tiles, map_width, min_cell_width, min_cell_height, rooms)
        bottom = connect(node['bottom'], tiles, map_width, min_cell_width, min_cell_height, rooms)

        tunnel(top, bottom, tiles, map_width, floor)

        return top
    elif node['left'] and node['right']:
        left = connect(node['left'], tiles, map_width, min_cell_width, min_cell_height, rooms)
        right = connect(node['right'], tiles, map_width, min_cell_width, min_cell_height, rooms)

        tunnel(left, right, tiles, map_width, floor)

        return left
    else:
        border = 1
        x = node['x'] + border
        y = node['y'] + border
        w = node['width'] - border * 2
        h = node['height'] - border * 2

        for xx in range(x, x + w):
            for yy in range(y, y + h):
                index = coord_to_1d_index(xx, yy, map_width)
                tiles[index] = floor

        rooms.append((x, y, w, h))

        return x, y, w, h


def main(params):
    width = params['width']
    height = params['height']
    min_room_size = params['min_size']
    max_room_size = params['max_size']
    seed = params['seed']

    random.seed(seed)

    wall = 1
    floor = 0

    tiles = [wall] * (width * height)

    # leave outer border alone
    bsp = bsp_rect(1, 1, width - 2, height - 2, max_room_size, max_room_size)

    rooms = []
    connect(bsp, tiles, width, min_room_size, min_room_size, rooms, wall, floor)

    dungeon = {
        "width": width,
        "height": height,
        "tiles": tiles,
        'rooms': rooms
    }

    return dungeon
