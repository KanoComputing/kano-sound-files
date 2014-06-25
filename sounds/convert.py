#!/usr/bin/env python

import os

for root, dirs, filenames in os.walk('.'):
    for filename in filenames:
        path = os.path.join(root, filename)
        basename, ext = os.path.splitext(path)
        ext = ext[1:]

        if ext not in ['mp3', 'wav']:
            continue

        if basename.endswith('_new'):
            continue

        print path, basename, ext

        sox_cmd = "sox {} -b 16 {}_new.wav remix -".format(path, basename)
        os.system(sox_cmd)
        os.remove(path)
        os.rename('{}_new.wav'.format(basename), '{}.wav'.format(basename))
