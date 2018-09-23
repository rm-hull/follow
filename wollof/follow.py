#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import itertools
import select
import subprocess
import sys
import threading
from datetime import datetime

from colored import attr, bg, fg
from wollof.color_palette import MUTED, PASTEL

reset = attr('reset')
error_marker = bg('red') + fg('white')
finished_marker = bg('white') + fg('black')


def _output(color, prefix, line, include_timestamp=True, line_color=''):
    if include_timestamp:
        timestamp = datetime.now().strftime('%H:%M:%S.%f')
        sys.stdout.write(
            f'{color}{prefix} | {timestamp} | {reset}{line_color}{line.rstrip()}{reset}\n')
    else:
        sys.stdout.write(f'{color}{prefix} | {reset}{line.rstrip()}{reset}\n')


def _watch_stream(color, prefix, fp, line_color=''):
    while True:
        data = fp.readline().decode('utf-8')
        if data:
            _output(color, prefix, data, line_color=line_color)
        else:
            break


def _with_keyboard_interrupts_suppressed(func):
    def __wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            pass

    return __wrapper


def _follow_command(color, command, max_width):
    prefix = command[0:max_width].ljust(max_width)
    process = subprocess.Popen(command.split(
        ' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout_watcher = threading.Thread(
        target=_watch_stream,
        args=(color, prefix, process.stdout))

    stderr_watcher = threading.Thread(
        target=_watch_stream,
        args=(color, prefix, process.stderr),
        kwargs=dict(line_color=error_marker))

    stdout_watcher.start()
    stderr_watcher.start()

    stdout_watcher.join()
    stderr_watcher.join()

    process.wait()
    _output(color, prefix,
            f'*** Process terminated with exit code: {process.returncode} ***', line_color=finished_marker)


def process(argv):
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('commands', metavar='CMD', type=str, nargs='+',
                        help='commands to run concurrently (use single quotes for passing arguments')

    args = parser.parse_args(argv)

    max_width = len(max(args.commands, key=len))
    follow_cmd = _with_keyboard_interrupts_suppressed(_follow_command)
    threads = [threading.Thread(target=follow_cmd, args=(color_name, command, max_width))
               for color_name, command in zip(itertools.cycle(PASTEL), args.commands)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    process(['./random_output.py 4',
             './random_output.py 6', './random_output.py 6',
             './random_output.py 6', './random_output.py 6', './random_output.py 6',
             './random_output.py 6', './random_output.py 6'])
