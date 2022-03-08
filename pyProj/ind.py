#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def cmn(n, m):
    if m == n or m == 0:
        return 1
    if m != 1:
        return cmn(n - 1, m) + cmn(n - 1, m - 1)
    else:
        return n


if __name__ == '__main__':
    print(cmn(9, 4))
