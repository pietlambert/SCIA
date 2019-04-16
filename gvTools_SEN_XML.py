import os
CURR_DIR = os.path.curdir
SEN_XML_DIR = os.path.join(os.path.curdir, "sen_xml")

import sen_xml._writer as writer
from sen_xml.SEN_Node import *
from sen_xml.SEN_Beam import *
from sen_xml.SEN_Support import *

OBJECTS = [SEN_Node, SEN_Beam, SEN_Support]


def GenerateName_using(prefix):
    """
    Name generator
        Usage:
            NodeName = GenerateName_using("N")
                next(NodeName) will first return 'N1'
                next(NodeName) will then return 'N2'
                ...
            BeamName = GenerateName_using("B")
                next(BeamName) will first return 'B1'
                next(BeamName) will then return 'B2'
                ...
    """
    num = 1
    while num < 1000000:
        yield (prefix + str(num))
        num +=1


# use this for debugging
if __name__ == "__main__":

    SEN_Node.Add("N1", 0.0, 0.0, 0.0)
    SEN_Node.Add("N2", 0.0, 0.0, 5.0)
    SEN_Node.Add("N3", 7.5, 0.0, 6.5)
    SEN_Node.Add("N4", 15.0, 0.0, 5.0)
    SEN_Node.Add("N5", 15.0, 0.0, 0.0)

    SEN_Beam.Add("B1", "N1", "N2", 1)
    SEN_Beam.Add("B2", "N2", "N3", 1)
    SEN_Beam.Add("B3", "N3", "N4", 1)
    SEN_Beam.Add("B4", "N4", "N5", 1)
    SEN_Beam.Add_Line("B5", "N1", "N5", 1)


    SEN_Beam.Add_Arc("B6", "N1", "N2", "N3", 1)
    SEN_Beam.Add_Parabola("B7", "N3", "N4", "N5", 1)

    SEN_Support.Add("Sn1", "N1", [1], [1], [1], [1], [1], [1])
    SEN_Support.Add_on_Beam("Sb1", "B6", [1], [0], [1], [2, 20000], [1], [1], 0, 1, 0.333)

    writer.WriteXML("test2.xml")
    writer.WriteXLS("abc.xlsx")
