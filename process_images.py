#!/usr/bin/env python3

import os, sys
from PIL import Image
import json

with open(sys.argv[1], 'r') as f:
    params = json.load(f)

# print(params)

outpath = params["output_path"]
inpath = params["input_path"]
out_format = params["out_format"]

if not os.path.exists(outpath):
    try:
        os.mkdir(outpath)
        print("Output dir created: ", outpath)
    except OSError:
        print("Cannot create output dir")

for infile in os.listdir(inpath):
    f, e = os.path.splitext(os.path.basename(infile))
    outfile = outpath + f + "_compressed." + out_format
    infile = inpath + infile
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.resize((params["size"][0], params["size"][1])).convert("RGB").save(outfile, out_format, optimize=True)
                print("Compressed", outfile)
        except OSError as e:
            print(e)