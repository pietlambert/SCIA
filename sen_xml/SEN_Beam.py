# import sen_xml._sen_xml_helper as gv
class SEN_Beam:
    """SEN_Beam supports the following methods:
    1)  Add (BeamName, Node1, Node2, CSS number)
    2)  Add_Line (BeamName, Node1, Node2, CSS number)
            Add a beam of type Line.
                Parameters:
                    - BeamName: (string) 'B6'
                    - Node1: start node (string) N12
                    - Node2: end node(string) N4
                    - CSS number: (int) 1
    3)  Add_Arc (BeamName, Node1, Node2, Node3, CSS number)
    4)  Add_Parabola (BeamName, Node1, Node2, Node3, CSS number)
            Add a beam of type Arc or Parabola.
                Parameters:
                    - BeamName: (string) 'B6'
                    - Node1: start node (string) N12
                    - Node2: internal node (string) N4
                    - Node3: end node (string) N7
                    - CSS number: (int) 1

    """
    data_Line, data_Arc, data_Parabola = [], [], []
    @classmethod
    def Add(cls, BeamName, Node1, Node2, CSSnr):
        cls.data_Line.append([BeamName, Node1, Node2, CSSnr])
    @classmethod
    def Add_Line(cls, BeamName, Node1, Node2, CSSnr):
        cls.data_Line.append([BeamName, Node1, Node2, CSSnr])
    @classmethod
    def Add_Arc(cls, BeamName, Node1, Node2, Node3, CSSnr):
        cls.data_Arc.append([BeamName, Node1, Node2, Node3, CSSnr])
    @classmethod
    def Add_Parabola(cls, BeamName, Node1, Node2, Node3, CSSnr):
        cls.data_Parabola.append([BeamName, Node1, Node2, Node3, CSSnr])
    @classmethod
    def ReturnXMLs(cls):
        if (len(cls.data_Line)==0 and len(cls.data_Arc)==0 and len(cls.data_Parabola==0)):
            return [False, "", ""]

        import sen_xml._sen_xml_helper as gv
        tags = gv.FillTags("SEN_Beam.xml", "version_01")
        # xml.def
        tdef = tags.get("XMLDEF")
        # xml
        t_container = tags.get("CONTAINER")
        t_table = tags.get("TABLE")
        t_obj_line = tags.get("OBJ_LINE")
        t_obj_arc = tags.get("OBJ_ARC")
        t_obj_parabola = tags.get("OBJ_PARABOLA")

        to_L = "".join([t_obj_line.format(*d) for d in cls.data_Line])
        to_A = "".join([t_obj_arc.format(*d) for d in cls.data_Arc])
        to_P = "".join([t_obj_parabola.format(*d) for d in cls.data_Parabola])
        to = "".join([to_L, to_A, to_P])

        tt = t_table.format(to)
        tc = t_container.replace("{0}", tt)
        return [True, tc, tdef]

if __name__ == "__main__":
    pass