import math
import gvTools_SEN_XML as gvXML

def createNodeList(delta_Z, delta_Theta, Internal_Radius, External_Radius, Nr_of_steps):
    # returns a list of node definitions;
    # each node is a list of [NodeName, X, Y, Z]
    nL = []
    Z = 0.0
    theta = 0.0
    NodeName = gvXML.GenerateName_using("N")

    for stp in range(Nr_of_steps):
        Z = stp * delta_Z
        theta = stp * delta_Theta

        nL.append([next(NodeName), Internal_Radius * math.cos(theta), Internal_Radius * math.sin(theta), Z])
        nL.append([next(NodeName), External_Radius * math.cos(theta), External_Radius * math.sin(theta), Z])
    return nL

def createBeamList(nodeList):
    # returns a list of beam definitions;
    # each beam is a list of [BeamName, start NodeName, end NodeName]
    bL = []
    BeamName = gvXML.GenerateName_using("B")

    #create the horizontal steps
    for i in range(0, len(nodeList), 2):
        bL.append([next(BeamName), nodeList[i][0], nodeList[i+1][0]])

    #create the two spirals
    for i in range(0, len(nodeList) - 2, 2):
        bL.append([next(BeamName), nodeList[i][0], nodeList[i+2][0]])
        bL.append([next(BeamName), nodeList[i+1][0], nodeList[i+3][0]])
    return bL



def main():
    nodeList = createNodeList(delta_Z = 0.18, delta_Theta = math.radians(15.0), Internal_Radius = 0.6, External_Radius = 2.6, Nr_of_steps = 48)

    for node in nodeList:
        # SEN_Node.Add (NodeName, X, Y, Z)
        gvXML.SEN_Node.Add(node[0], node[1], node[2], node[3])

    beamList = createBeamList(nodeList)
    for beam in beamList:
        # SEN_Beam.Add_Line (BeamName, start NodeName, end NodeName, CSS number)
        gvXML.SEN_Beam.Add_Line(beam[0], beam[1], beam[2], 1)

    gvXML.writer.WriteXML("SpiralStair.xml")

if __name__ == "__main__":
    main()
