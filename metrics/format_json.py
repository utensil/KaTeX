#!/usr/bin/env python

import sys
import json

props = ['depth', 'height', 'italic', 'skew']

if len(sys.argv) > 1:
    if sys.argv[1] == '--width':
        props.append('width')

data = json.load(sys.stdin)
sep = "module.exports = {\n"
for font in sorted(data):
    sys.stdout.write(sep + json.dumps(font))
    sep = ": {\n  "
    for glyph in sorted(data[font], key=int):
        sys.stdout.write(sep + json.dumps(glyph) + ": ")
        
        values = [value if value != 0.0 else 0 for value in 
                  [data[font][glyph][key] for key in props]]
            
        sys.stdout.write(json.dumps(values))
        sep = ",\n  "
    sep = "\n},\n"
sys.stdout.write("\n}};\n")
