#!/usr/bin/env python
# -*- coding: utf-8 -*-

#via www.openbookproject.net

from bitmap  import Bitmap
from hashlib import md5


def make_hashes(word) :
    hex32 = md5(word).hexdigest()
    hashes = []
    for i in range(0,30,5) :
        hashes.append(int(hex32[i:i+5],16))
    return hashes


def load_bitmap(file) :
    words = open(file).readlines()
    words = map(lambda x: x.strip(), words)
    bmap  = Bitmap(2**20)
    for word in words :
        hashes = make_hashes(word)
        for hash in hashes :
            bmap.setBit(hash)
    return bmap


def check_word(bmap, word) :
    hashes = make_hashes(word)
    for hash in hashes :
        if not bmap.getBit(hash): return False
    return True

if __name__ == '__main__':