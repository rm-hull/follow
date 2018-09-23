#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colored import attr, bg, fg
from wollof.clut import rgb2short

def __ansi_colors(*rgb_colors):
    return [fg(rgb2short(color)) for color in rgb_colors]


MUTED = __ansi_colors(
    '#A54242',
    '#8C9440',
    '#DE935F',
    '#5F819D',
    '#85678F',
    '#5E8D87',
    '#707880',
)

PASTEL = __ansi_colors(
    '#CC6666',
    '#B5BD68',
    '#F0C674',
    '#81A2BE',
    '#B294BB',
    '#8ABEB7',
    '#C5C8C6',
)