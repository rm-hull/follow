# WOLLOF

A command line utility to start some programs running simultaneously so that
their output is interleaved on the console with each programs output prefixed
by a colour and timestamp.

![SVG](https://rawgithub.com/rm-hull/follow/master/example.svg)

## Setup

Install from pypi with:

    sudo -H pip install -U wollof

## TODO
* Add -r switch which if passed, it instead converts existing timestamps in the 
  input to relative times, such as "15m5s ago".
* Add -f FILE argument which will read commands from the supplied file
* Add xargs style handling to run a single command with different arguments
* Silence traceback info when interrupting with Ctrl-C 
* Build python package ✅
* Install as executable in `<location>/bin` ✅
* Selectable colour palette - muted/pastel colors 
* Documentation
* Publish to PyPi

## License

### The MIT License (MIT)
Copyright (c) 2018 Richard Hull

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.