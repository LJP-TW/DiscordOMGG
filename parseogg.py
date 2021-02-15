#!/usr/bin/env python3
import sys
import os

class OGG:
    def __init__(self, content):
        self.signature   = content[:4]
        self.version     = content[4:5]
        self.flags       = content[5:6]
        self.granulePos  = content[6:14]
        self.serialNum   = content[14:18]
        self.sequenceNum = content[18:22]
        self.checksum    = content[22:26]
        self.totalSeg    = int(content[26:27].hex(), 16)
        self.size        = 0

        for i in range(self.totalSeg):
            self.size += content[27 + i]

        self.data        = content[27 + self.totalSeg:27 + self.totalSeg + self.size]
        self.rawdata     = content[:27 + self.totalSeg + self.size]

    def show(self):
        print(f"Signature   = {self.signature}")
        print(f"version     = {self.version.hex()}")
        print(f"flags       = {self.flags.hex()}")
        print(f"granulePos  = {self.granulePos.hex()}")
        print(f"serialNum   = {self.serialNum.hex()}")
        print(f"sequenceNum = {self.sequenceNum.hex()}")
        print(f"checksum    = {self.checksum.hex()}")
        print(f"totalSeg    = {self.totalSeg}")
        print(f"size        = {self.size}")

def parseBytes2Oggs(content):
    oggs = []

    while True:
        ogg = OGG(content)

        content = content[27 + ogg.totalSeg + ogg.size:]

        if ogg.signature != b'OggS':
            break
        
        oggs.append(ogg)

        if len(content) == 0:
            break

    return oggs

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename, 'rb') as f:
        content = f.read()

    oggs = []

    while True:
        ogg = OGG(content)

        content = content[27 + ogg.totalSeg + ogg.size:]

        if ogg.signature != b'OggS':
            break
        
        oggs.append(ogg)

        if len(content) == 0:
            break

    # For debug
    print(len(oggs))
    for i in range(20):
        print(oggs[i].checksum.hex(), end=' ')
        print(oggs[i].sequenceNum.hex(), end=' ')
        print(oggs[i].serialNum.hex())


