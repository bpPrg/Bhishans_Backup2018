#!/usr/bin/env python3
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Dec 14, 2016
# Last update :
# Est time    :


def increase_filenumber(infile):
    """increase filenumber.

    e.g.
    tmp/f606w_gal1.fits ==>  tmp/f606w_gal101.fits
    tmp/f814w_gal1.fits ==>  tmp/f814w_gal101.fits

    """
    import os
    import glob
    import re
    oldfiles = glob.glob(infile)
    for oldfile in oldfiles:
        try:
            fname, ext = os.path.splitext(oldfile)
            head, tail = os.path.split(oldfile)
            base = os.path.basename(oldfile)
            mydir = os.path.dirname(oldfile)
            # regex = mydir + r'/(.+?gal)(\d+)(.fits)'
            # pre = re.search('(.+?)(\d+)(\.\w*)', oldfile).group(1)
            # num = re.search('(.+?)(\d+)(\.\w*)', oldfile).group(2)
            # post = re.search('(.+?)(\d+)(\.\w*)', oldfile).group(3)
            # new = pre + str(int(num) + 100) + post
            print(fname, ext, head, tail, base)

        except:
            pass


if __name__ == "__main__":
    infile = 'tmp/*.fits'
    increase_filenumber(infile)
