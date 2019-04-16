class SEN_Node:
    """SEN_Node supports the following methods:
    1) Add(NodeName, X, Y, Z)
        Add a node, using the (X,Y,Z) coordinates
            Parameters:
            - NodeName: (string) 'N1', 'N2'
            - X: (float) 10.0 m
            - Y: (float) 12.5 m
            - Z: (float) 10.0 m

    """
    data = []
    @classmethod
    def Add(cls, NodeName, X, Y, Z):
        cls.data.append([NodeName, X, Y, Z])
    @classmethod
    def ReturnXMLs(cls):
        if (len(cls.data)==0):
            return [False, "", ""]

        import sen_xml._sen_xml_helper as gv
        tags = gv.FillTags("SEN_Node.xml", "version_01")
        # xml.def
        tdef = tags.get("XMLDEF")
        # xml
        t_container = tags.get("CONTAINER")
        t_table = tags.get("TABLE")
        t_obj = tags.get("OBJ")

        to = "".join([t_obj.format(*d) for d in cls.data])
        tt = t_table.format(to)
        tc = t_container.replace("{0}", tt)
        return [True, tc, tdef]

if __name__ == "__main__":
    pass