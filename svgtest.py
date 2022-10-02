import sys
import xml.etree.ElementTree as ET
first_coordinate = True
tree = ET.parse(sys.argv[1])
root = tree.getroot()
for child in root:
    if "polyline" in child.tag or "polygon" in child.tag:
        print("Pen up")
        coords = child.attrib["points"].split(" ")[:-1]
        first_coordinate = True
        for coord in coords:
            xstring, ystring = (coord.split(","))
            x, y = float(xstring), float(ystring)
            print(f"Go to {x}, {y}")
            if(first_coordinate):
                print("Pen down")
                first_coordinate = False
        if "polygon" in child.tag:
            coord = coords[0]
            xstring, ystring = (coord.split(","))
            x, y = float(xstring), float(ystring)
            print(f"Go to {x}, {y}")
    if "rect" in child.tag:
        print("Pen up")
        x = float(child.attrib["x"])
        y = float(child.attrib["y"])
        width = float(child.attrib["width"])
        height = float(child.attrib["height"])
        print(f"Go to {x}, {y}")
        print("Pen down")
        print(f"Go to {x}, {y + height}")
        print(f"Go to {x + width}, {y + height}")
        print(f"Go to {x + width}, {y}")
        print(f"Go to {x}, {y}")
print("Pen up")
print("Go to 0, 0")