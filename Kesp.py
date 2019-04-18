import math
import gvTools_SEN_XML as gvXML

class Model:

    def __init__(self, name'model'):
        self.name = name


class Kesp:

    def __init__(self, name='moot', parts=7, width=2.8, origin=(0, 0, 0)):
        self.name = name
        self.parts = parts
        self.width = width
        self.origin = origin

        self.build()

    def build(self):
        self.nL = []
        self.bL = []

        NodeName = gvXML.GenerateName_using('N')
        BeamName = gvXML.GenerateName_using('B')

        # each node is a list of [NodeName, X, Y, Z]
        for part in range(self.parts + 1):
            self.nL.append([next(NodeName), self.width * part,
                       self.origin[1], self.origin[2]])

        # each beam is a list of [BeamName, start NodeName, end NodeName]
        for n1, n2 in zip(self.nL[:-1], self.nL[1:]):
            self.bL.append([next(BeamName), n1[0], n2[0]])

    def write(self):
        # write in a file
        for node in self.nL:
            gvXML.SEN_Node.Add(*node)

        for beam in self.bL:
            gvXML.SEN_Beam.Add_Line(*beam, 1)


def main():

    moot1 = Kesp(name='Moot 1', parts=17, width=1.4)

    moot1.write()

    gvXML.writer.WriteXML("Kesp.xml")


if __name__ == "__main__":
    main()
