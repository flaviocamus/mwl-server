import subprocess

r="y"
context=["STUDY","WORKLIST"]
modality=['US','CT','MR']
host = 'r192-mwl-server.herokuapp.com'
port = 80
print("requiere Offis dicomtoolkit : https://dicom.offis.de/dcmtk.php.en ")

while r=="y":
    # hace el ciclo de programa
    print("Herrramiernta query")
    print("Contexto de query?")
    c=0
    for con in context:
        print( str(c)+ ": "+con)
        c=c+1
    ctx=input()
    print("Modalidad")
    c=0
    for mo in modality:
        print(str(c) + ": " + mo )
        c=c+1
    user_m=input()
    user_mod=''
    if user_m!="" and int(user_m) > -1:
        user_mod="="+modality[int(user_m)]



    print("generando query")
    callstr=["findscu.exe","+dc" ,"-S", "-aec", "ACME_STORE" ,"-aet", "ACME1", host,str(port) ,"-k", "QueryRetrieveLevel=WORKLIST" ,"-k", "StudyDate", '-k','PatientName',"-k", "AccessionNumber" ,"-k","StudyDate","-k",'AccessionNumber','-k','StudyID','-k','StudyDescription','-k','PatientID','-k','PatientBirthDate','-k','PatientSex','-k','Modality'+user_mod]
    print(callstr)
    subprocess.call(callstr)
    print("Continuar? y/n")
    r=input()
