import os
from gvTools_SEN_XML import SEN_XML_DIR

def FillTags(fname, version):
    tags = {}
    bFillDict = False
    fpath = os.path.join(SEN_XML_DIR, fname)
    if os.path.exists(fpath):
        with open(fpath, encoding="utf_16", mode="r",) as f:
            #search version tag
            line = f.readline()
            while line:
                if line.find("TAG:")==0:
                    Tag = line.rstrip().split(":")[1]
                    if Tag == version:
                        bFillDict = True
                        break
                line = f.readline()

            if bFillDict:
                #search next tag after the version tag
                line = f.readline()
                while line:
                    if line.find("TAG:")==0:
                        Tag = line.rstrip().split(":")[1]
                        if Tag == "END":
                            bFillDict = False
                        break
                    line = f.readline()

            if bFillDict:
                #fill dict until the end tag
                tagStr = ""
                line = f.readline()
                while line:
                    if line.find("TAG:")==0:
                        #add to dict
                        tags[Tag] = tagStr
                        #new tag name
                        Tag = line.rstrip().split(":")[1]
                        tagStr = ""
                        if Tag == "END":
                            bFillDict = False
                            break
                    else:
                        tagStr += line
                    line = f.readline()
    return tags


if __name__ == "__main__":
    pass