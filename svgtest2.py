import sys
from svgpathtools import svg2paths
paths, attributes = svg2paths(sys.argv[1])
for k, v in enumerate(attributes):
    print(v['d'])  # print d-string of k-th path in SVG