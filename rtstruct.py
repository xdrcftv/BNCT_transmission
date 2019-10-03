import numpy as np
import xml.etree.ElementTree as EleTree
import os
import pydicom as dcm
import xml_parser

file_directory = 'C:/INFINITT/BNCT_TEMP'

whole_files = os.listdir(file_directory)
list(whole_files)
xml_file = os.path.join(file_directory, whole_files[0])
xml_doc = EleTree.parse(xml_file)

root = xml_doc.getroot()

struct_dir = root.findtext('RTStructure')
RT_struct = dcm.dcmread(struct_dir)
ROI_contour = RT_struct.ROIContourSequence

tumor_ROI = xml_parser.tumor_ROINo(root)

tumor1 = ROI_contour[3]
print(tumor1)
# for i in tumor_ROI:
#     print(ROI_contour[i-1])

