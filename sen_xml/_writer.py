import os
#import sen_xml._sen_xml_helper as gv
#from gvTools_SEN_XML import CURR_DIR
#from gvTools_SEN_XML import CURR_FNAME
#from gvTools_SEN_XML import SEN_XML_DIR

def GetFullFileName(fname, ext):
    #check if ext is present, else add it
    p, f = os.path.split(fname)   # p= the path, f= the file name
    if f:
        parts = f.split(".")
        if parts[-1].upper() != ext.upper():
            f = f + "." + ext
    if not p:
        from gvTools_SEN_XML import CURR_DIR
        p = CURR_DIR
    return os.path.join(p, f)


def WriteXML(fname):
    #from gvTools_SEN_XML import CURR_DIR
    import sen_xml._sen_xml_helper as gv
    tags = gv.FillTags("SEN_XML.xml", "version_01")

    from gvTools_SEN_XML import OBJECTS
    x = "".join([obj.ReturnXMLs()[1] for obj in OBJECTS if obj.ReturnXMLs()[0]])
    d = "".join([obj.ReturnXMLs()[2] for obj in OBJECTS if obj.ReturnXMLs()[0]])

    xml_fname = GetFullFileName(fname, "xml")
    xmldef_fname = GetFullFileName(xml_fname, "def")

    txml = tags.get("XML").format(fname + ".def", x)
    tdef = tags.get("XMLDEF").format(d)

    with open(xml_fname, encoding="utf_16", mode="w",) as f:
        f.write(txml)
    with open(xmldef_fname, encoding="utf_16", mode="w",) as f:
        f.write(tdef)


def WriteXLS(fname):
    #http://aef.pdinfo.scia.cz/
    import xlsxwriter
    xls_fname = GetFullFileName(fname, "xlsx")
    wb = xlsxwriter.Workbook(xls_fname)

    header_fmt = wb.add_format()
    header_fmt.set_font_name("Segoe UI")
    header_fmt.set_font_size(9)
    header_fmt.set_bold()
    cell_fmt = wb.add_format()
    cell_fmt.set_font_name("Segoe UI")
    cell_fmt.set_font_size(9)


    from gvTools_SEN_XML import OBJECTS
    for obj in OBJECTS:
        if obj.__name__=="SEN_Node" and len(obj.data)>0:
            ws = wb.add_worksheet("StructuralPointConnection")
            ws.set_column(0, 5, None, cell_fmt)
            ws.set_row(0, cell_format=header_fmt)
            row = 0
            header = ["Name", "Coordinate X [m]", "Coordinate Y [m]", "Coordinate Z [m]"]
            ws.write_row(row, 0, header)
            for NodeName, X, Y, Z in obj.data:
                row += 1
                ws.write_row(row, 0, [NodeName, X, Y, Z])
        if obj.__name__=="SEN_Beam" and (len(obj.data_Line)>0 or len(obj.data_Arc)>0 or len(obj.data_Parabola)>0):
            ws = wb.add_worksheet("StructuralCurveMember")
            ws.set_column(0, 25, None, cell_fmt)
            ws.set_row(0, cell_format=header_fmt)
            row = 0
            header = ["Name", "Type", "Begin node", "End node", "Cross section", "Layer", "LCS", "Coordinate X [m]", "Coordinate Y [m]", "Coordinate Z [m]", "LCS Rotation [deg]", "System line", "Eccentricity ey [mm]", "Eccentricity ez [mm]", "Geometrical shape", "Length [m]", "Nodes", "Segments", "Behaviour in analysis", "Colour", "ID"]
            ws.write_row(row, 0, header)
            for BeamName, Node1, Node2, CSSnr in obj.data_Line:
                row += 1
                ws.write_row(row, 0, [BeamName, "General", Node1, Node2, "CS"+str(CSSnr),"Layer1", "Standard", 0.0, 0.0, 0.0, 0.0, "Centre", 0.0, 0.0, "Line", 0.0, "; ".join([Node1, Node2]), "Line", "Standard","", ""])
            for BeamName, Node1, Node2, Node3, CSSnr in obj.data_Arc:
                row += 1
                ws.write_row(row, 0,[BeamName, "General", Node1, Node3, "CS"+str(CSSnr),"Layer1", "Standard", 0.0, 0.0, 0.0, 0.0, "Centre", 0.0, 0.0, "Line", 0.0, "; ".join([Node1, Node2, Node3]), "Circular Arc", "Standard","", ""])
            for BeamName, Node1, Node2, Node3, CSSnr in obj.data_Parabola:
                row += 1
                ws.write_row(row, 0,[BeamName, "General", Node1, Node3, "CS"+str(CSSnr),"Layer1", "Standard", 0.0, 0.0, 0.0, 0.0, "Centre", 0.0, 0.0, "Line", 0.0, "; ".join([Node1, Node2, Node3]), "Parabolic Arc", "Standard","", ""])
        if obj.__name__=="SEN_Support" and (len(obj.data_inNode)>0):
            pass
        if obj.__name__=="SEN_Support" and (len(obj.data_inBeam)>0):
            pass


    wb.close()


if __name__ == "__main__":
    pass

