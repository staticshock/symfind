#!/usr/bin/python

from __future__ import print_function
import re
from subprocess import check_output

__version__ = '0.1.0'


def parse_output(args, pattern):
    return re.findall(pattern, check_output(args))


def get_undef_syms(obj):
    return parse_output(["nm", "-u", obj], r"\bU (.*)")


def get_lib_deps(obj):
    return parse_output(["ldd", obj], r"=> (.+) ")


class memoize(dict):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        return self[args]

    def __missing__(self, key):
        result = self[key] = self.func(*key)
        return result


@memoize
def get_def_syms(obj):
    # This is better than nm -D for matching versioned symbols,
    # e.g. something@@GLIBC_2.0
    return parse_output(["readelf", "--dyn-syms", obj], r" (\S+)\n")


FOUND_MSG = "{idt}Found symbol: \033[36m{sym}\033[0m in \033[34m{lib}\033[0m"
NOT_FOUND_MSG = "{idt}Did not find symbol: \033[31m{sym}\033[0m"


def symfind(targets):
    indent = "" if len(targets) < 2 else "\t"

    for target in targets:
        if len(targets) > 1:
            print("{tgt}:".format(tgt=target))
        for symbol in get_undef_syms(target):
            for library in get_lib_deps(target):
                if symbol in get_def_syms(library):
                    print(FOUND_MSG.format(
                        idt=indent, sym=symbol, lib=library))
                    break
            else:
                print(NOT_FOUND_MSG.format(idt=indent, sym=symbol))


def parse_args():
    from optparse import OptionParser
    parser = OptionParser(
        usage="%prog [options] lib1 [lib2 ...]",
        version="%prog v" + __version__)
    return parser.parse_args()


def main():
    from glob import glob
    options, args = parse_args()
    targets = [target for arg in args for target in glob(arg)]
    symfind(targets)


if __name__ == '__main__':
    main()
