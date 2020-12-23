import os

from pydicom import dcmread
from pydicom.dataset import Dataset, FileDataset, FileMetaDataset

instances = []
fdir = 'd:/DICOM/CPTAC-HNSCC/C3L-04844/02-24-2005-CT SOFT TISSUE NECK ENHANCEDNK-16104/601.000000-35 WET NECK AXIAL-60974'
for fpath in os.listdir(fdir):
    print(fpath)
    instances.append(dcmread(os.path.join(fdir, fpath)))


##  crear new metadata
file_meta = FileMetaDataset()
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
file_meta.MediaStorageSOPClassUID ='1.2.840.10008.5.1.4.1.1.4'
file_meta.MediaStorageSOPInstanceUID = "1.2.3"
file_meta.ImplementationClassUID = "1.2.3.4"


print (file_meta)
print (type(file_meta))