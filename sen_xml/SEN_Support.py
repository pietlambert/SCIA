#import sen_xml._sen_xml_helper as gv
class SEN_Support:
    """SEN_Support supports the following methods:
    1) Add (SupportName, NodeName, X, Y, Z, Rx, Ry, Rz)
        Add a support in a node.
            Parameters:
                - SupportName: (string)
                - NodeName: (string)
                - X:  (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 N/m
                - Y:  (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 N/m
                - Z:  (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 N/m
                - Rx: (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 Nm/rad
                - Ry: (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 Nm/rad
                - Rz: (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 Nm/rad
    2) Add_on_Beam (SupportName, BeamName, X, Y, Z, Rx, Ry, Rz, GcsLcs, AbsRel, pos)
        Add a nodal support on a beam.
            Parameters:
                - SupportName: (string)
                - NodeName: (string)
                - X:  (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 N/m
                - Y:  (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 N/m
                - Z:  (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 N/m
                - Rx: (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 Nm/rad
                - Ry: (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 Nm/rad
                - Rz: (list) [1]=Fixed, [0]=Free; [2, 12345]=Flexible with Rigidity=12345 Nm/rad
                - GcsLcs: (int)  0=GCS, 1=LCS
                - AbsRel: (int)  0=Abs, 1=Rel
                - Pos: (float)  absolute (in m) or relative ([0..1]) position on the beam

    """
    data_inNode, data_inBeam = [], []
    @classmethod
    def Add(cls, SupportName, NodeName, X, Y, Z, Rx, Ry, Rz):
        cls.data_inNode.append([SupportName, NodeName, X, Y, Z, Rx, Ry, Rz])
    @classmethod
    def Add_on_Beam(cls, SupportName, BeamName, X, Y, Z, Rx, Ry, Rz, GcsLcs, AbsRel, pos):
        cls.data_inBeam.append([SupportName, BeamName, X, Y, Z, Rx, Ry, Rz, GcsLcs, AbsRel, pos])
    @classmethod
    def ReturnXMLs(cls):
        if len(cls.data_inNode)==0 and len(cls.data_inBeam)==0:
            return [False, "", ""]

        import sen_xml._sen_xml_helper as gv
        tags = gv.FillTags("SEN_Support.xml", "version_01")

        t_Rigid = tags.get("OBJ_Rigid")
        t_Free = tags.get("OBJ_Free")
        t_Flexible = tags.get("OBJ_Flexible")

        tdef, tc = "", ""
        if len(cls.data_inNode)>0:
            #xml.def
            tdef = "".join([tdef, tags.get("XMLDEF_in_Node")])
            #xml
            t_container = tags.get("CONTAINER_inNODE")
            t_table = tags.get("TABLE_inNODE")
            t_obj_inNODE = tags.get("OBJ_inNODE")
            to = ""
            for d in cls.data_inNode:
                tx = []
                for i in range(6):
                    if d[i+2][0] == 0:
                        tx.append(t_Free.format(3 + 2*i))
                    if d[i+2][0] == 1:
                        tx.append(t_Rigid.format(3 + 2*i))
                    if d[i+2][0] == 2:
                        tx.append(t_Flexible.format(3 + 2*i, 4 + 2*i, d[i+2][1]))
                to = "".join([to, t_obj_inNODE.replace("{0}", d[0]).replace("{1}", d[1]).replace("{2}", "".join(tx))])
            tt = t_table.format(to)
            tc = "".join([tc, t_container.replace("{0}", tt)])

        if len(cls.data_inBeam)>0:
            #xml.def
            tdef = "".join([tdef, tags.get("XMLDEF_in_Beam")])
            #xml
            t_container = tags.get("CONTAINER_inBEAM")
            t_table = tags.get("TABLE_inBEAM")
            t_obj_inBEAM = tags.get("OBJ_inBEAM")
            to = ""
            for d in cls.data_inBeam:
                tx = []
                for i in range(6):
                    if d[i+2][0] == 0:
                        tx.append(t_Free.format(5 + 2*i))
                    if d[i+2][0] == 1:
                        tx.append(t_Rigid.format(5 + 2*i))
                    if d[i+2][0] == 2:
                        tx.append(t_Flexible.format(5 + 2*i, 6 + 2*i, d[i+2][1]))
                to = "".join([to, t_obj_inBEAM.replace("{0}", d[0]).replace("{1}", d[1]).replace("{2}", "".join(tx)).replace("{3}", str(d[8])).replace("{4}", str(d[9])).replace("{5}", str(d[10]))])
            tt = t_table.format(to)
            tc = "".join([tc, t_container.replace("{0}", tt)])

        return [True, tc, tdef]

