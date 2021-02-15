#!/usr/bin/env python3
import sys
import parseogg

def PlayOnce(filename1, filename2):
    with open(filename1, 'rb') as f:
        content1 = f.read()

    with open(filename2, 'rb') as f:
        content2 = f.read()

    oggs1 = parseogg.parseBytes2Oggs(content1)
    oggs2 = parseogg.parseBytes2Oggs(content2)

    with open('PlayOnce.ogg', 'wb') as f:
        for ogg in oggs1:
            f.write(ogg.rawdata)

        f.write(oggs2[0].rawdata)

        rawdata = oggs2[1].rawdata[:14] + oggs1[0].rawdata[14:18] + oggs2[1].rawdata[18:]
        f.write(rawdata)

        for ogg in oggs2[2:]:
            f.write(ogg.rawdata)

def PlayTwice(filename1, filename2):
    with open(filename1, 'rb') as f:
        content1 = f.read()

    with open(filename2, 'rb') as f:
        content2 = f.read()

    oggs1 = parseogg.parseBytes2Oggs(content1)
    oggs2 = parseogg.parseBytes2Oggs(content2)

    with open('PlayTwice.ogg', 'wb') as f:
        for ogg in oggs1:
            f.write(ogg.rawdata)

        f.write(oggs2[0].rawdata)

        f.write(oggs1[len(oggs1)-1].rawdata)

        for ogg in oggs2[1:]:
            f.write(ogg.rawdata)

if __name__ == "__main__":
    mode = sys.argv[1]
    filename1 = sys.argv[2]
    filename2 = sys.argv[3]

    if mode == 'once':
        PlayOnce(filename1, filename2)
    elif mode == 'twice':
        PlayTwice(filename1, filename2)
