
import xml.etree.ElementTree as ET
import numpy as np

baseDp = 300
dpOutputs = [300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600, 630, 660, 690, 720, 750, 780, 810, 840, 870, 900, 930, 960, 990, 1020, 1050, 1080]

def createXML(dp, ratio):
    tree = ET.ElementTree("tree")
    resources = ET.Element("resources")

    numbers = np.arange(1, 100.1, 0.1)
    for number in numbers:
        number = float('%.2f' % number)
        dimen = ET.SubElement(resources, "dimen")
        if number.is_integer():
            dimen.set('name', '_%dssp' % int(number))
        else:
            dimen.set('name', '_%.1fssp' % number)
        dimen.text = '%.2fsp' % (number * ratio)

    tree._setroot(resources)
    ET.indent(tree, space="\t", level=0)
    tree.write("res/values-sw%ddp/positive_ssps.xml" % dp, encoding = "UTF-8", xml_declaration = True)

for dp in dpOutputs:
    ratio = dp / baseDp
    createXML(dp=dp, ratio=ratio)