import os

from pydicom import dcmread
from pydicom.dataset import Dataset

from pynetdicom import AE, evt
from pynetdicom.sop_class import PatientRootQueryRetrieveInformationModelFind,StudyRootQueryRetrieveInformationModelFind,VerificationSOPClass

#from  mwldb import readdb 
import datetime 
import requests
import json
import sys 
import mariadb

#Sfrom flask import Flask
#from subprocess import call
#configuration 
from conf  import read_configuration

from lifeapi import load_mwl,mwl_dbquery
CONF=read_configuration()
print(CONF)

#echo
def handle_echo(event):
    """Handle a C-ECHO request event."""
    print("C-ECHO received")
    ei=event.assoc
    #print(type(ei))
    for elem in ei:
        print(elem)
    return 0x0000


# Implement the handler for evt.EVT_C_FIND
def handle_find(event):
    print("cfind fired")
    print(str(event.assoc.requestor.ae_title))
    #    """Handle a C-FIND request event."""
    ds = event.identifier
    #print("Query:")
    for elem in ds:
        print(elem)

    if 'QueryRetrieveLevel' not in ds:
        #print("fail!")
        # Failure
        yield 0xC000, None
        return
    #===================================================================================
    #print(instances)
    if ds.QueryRetrieveLevel == 'PATIENT':
        #@TODO yields no info  0xA900 - Identifier does not match SOP class
        if 'PatientName' in ds:
            if ds.PatientName not in ['*', '', '?']:
                matching = [
                    inst for inst in instances if inst.PatientName == ds.PatientName
                ]
    #====================================================================================
    #@TODO yields no info  0xA900 - Identifier does not match SOP class
    if ds.QueryRetrieveLevel == 'STUDY':
        #print("context=Study")
        identifier = Dataset()
        identifier.PatientName ='DUMMY'
        identifier.QueryRetrieveLevel = ds.QueryRetrieveLevel
        yield (0xFF00, identifier)
    #====================================================================================
    if ds.QueryRetrieveLevel == 'WORKLIST':
        # TODO 
        # Procesador del query
        # generar un dataset menor cuando se procesan el query, recorriendo ese dataset y generaldo la salida
        # usar los datos de entrada
        # generar diccionario de busqueda
        q={}
        q['modality']=str(ds.Modality)
        DB=mwl_dbquery(q)
        print("db len:" + str(len(DB)))
        
        for st in DB:
            print("._")
            # Check if C-CANCEL has been received
            if event.is_cancelled:
                yield (0xFE00, None)
                return
            # ver match de modalidad
            #print(st['mod'])
            now = datetime.datetime.now()
            #--conditionals
            
            if st['modality'] == ds.Modality and st['sch_study_date']==now.strftime("%Y%m%d"):
                print("._ _")
                print(st)
                #print("biuld...")
                #print(str(st['fecha']))
                identifier = Dataset()
                identifier.QueryRetrieveLevel = ds.QueryRetrieveLevel
                #PAtient group
                identifier.PatientName =str(st['patient_name'])
                identifier.PatientSex=str(st['patient_sex'])
                #identifier.PatientBirthDate='00000000'
                #identifier.PatientBirthDate=str(st['patient_birth_date'])
                identifier.PatientID=str(st['patient_id'])
                #Study Level group
                #identifier.StudyDescription=str(st['procedure'])
                #identifier.StudyDate=str(st['sch_study_date'])
                identifier.AccessionNumber =str(st['accession_number'])
                #identifier.Modality =str(st['modality'])
                # revisar identifier
                print('._ _ _')
                for elem in identifier:
                    print(elem)
                yield (0xFF00, identifier)
        yield(0x0000,NULL)
        print("end of assciation")

#Program
#DB=load_mwl()
#print(str(len(DB))+" studios en db")
#print(DB[0])

#print("iniciar web interface")
#call(["python.exe",'webinterface.py'])


#agregar handle para C-echo
handlers = [(evt.EVT_C_FIND, handle_find),(evt.EVT_C_ECHO, handle_echo)]

# Initialise the Application Entity and specify the listen port
ae = AE()

# Add the supported presentation context
ae.add_supported_context(PatientRootQueryRetrieveInformationModelFind)
ae.add_supported_context(StudyRootQueryRetrieveInformationModelFind)
ae.add_supported_context(VerificationSOPClass)

# Start listening for incoming association requests
#get heroku port:S
#
# 
# 
# dicom_port = int(os.environ.get("PORT", CONF["port"] ))

print("starting server "+ CONF['AEtitle']+" on port:"+str(CONF['port']))
ae.start_server((CONF["ip"], CONF['port']), evt_handlers=handlers,ae_title=CONF['AEtitle'])

#init web interface
#app = Flask(__name__)
#if __name__ == '__main__':
#	#app.run(debug=True)
#	app.run(host="0.0.0.0", debug=True, port=11113)