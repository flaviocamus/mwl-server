from graphqlclient import GraphQLClient
import json
import os
from datetime import date
from time import sleep
#import sqlite3
import mariadb

def db_insert(dat):
    print("quering mariadb")
    basedir=os.path.dirname(__file__)
    ###cn = sqlite3.connect(basedir+'/mwl00.db')
    ###cur=cn.cursor()
    try:
        conn = mariadb.connect(
            user="mwlserver",
            password="mwlserver",
            host="localhost",
            port=3306,
            database="mwlserver"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return -1
    cur = conn.cursor()
    print ("Opened database successfully");
    """{'accession_number': '9228939329061016', 'study_id': '', 'sch_study_date': '20210104', 'sch_study_time': '181500', 'study_descripction': 'NA', 
    'procedure': '', 'modality': 'US', 'patient_name': 'UNKNOWN', 'patient_id': '16029256-3', 'patient_sex': 'O', 'patient_birth_date': '0000000', 
    'patient_comments': 'cx'}
    """
    """ CREATE TABLE "studies" (
            "id_study"	INTEGER,
            "StudyID"	TEXT,
            "accession_number"	TEXT,
            "study_date"	TEXT,
            "study_description"	TEXT,
            "modality"	TEXT,
            "patient_name"	TEXT,
            "patient_sex"	TEXT,
            "patient_birth_date"	TEXT,
            "patient_id"	TEXT,
            "state"	INTEGER DEFAULT 1,
            PRIMARY KEY("id_study" AUTOINCREMENT)
        )
    """
    sql="insert  ignore into  studies(study_id,study_date,accession_number,modality,studies.procedure,patient_id,patient_name,patient_birth_date,patient_sex,ref_physician ,state)  values  ( ? , ? , ? , ? , ? , ? , ? , ? ,? , ? , ? )"
    cur.execute( sql , (dat['study_id'],dat['sch_study_date'],dat['accession_number'],dat['modality'],dat['procedure'],dat['patient_id'],dat['patient_name'],dat['patient_birth_date'],dat['patient_sex'],dat['ref_physician'],1) )
    #print(cur.lastrowid)
    #TODO log error de study_id repetidos
    #TODO agregar columna de creacion y de cambio
    
    
    conn.commit()
    conn.close()


def load_mwl():

    today = date.today()
    # dd/mm/YY
    HOY = today.strftime("%Y%m%d")


    basedir=os.path.dirname(__file__)
    client = GraphQLClient('https://demo-back-lifeapp.herokuapp.com')

    result = client.execute("""
    query {
    loginUser(user: "carlosok", pass: "carlos"){
        token
    }
    }
    """)

    print(type(result))
    data=json.loads(result)
    token = data['data']['loginUser']['token']

    client.inject_token(token)
    query="""
    query {
    getEvents{
        _id
        tenantID
        centersID
        isImported
        internal_number
        accession_number
        uuid
        altern_uuid
        external_uuid
        patient_type
        date
        date_string
        time
        time_string
        personID
        patient_doc_id
        referring_professionalID
        appointment_types
        status
        payment_status
        resource_types
        active
        professionalsID
        specialitiesID
        proceduresID
        appointment_reason
        reception_comment
        log {
        date
        time
        action_type
        detail
        prev_data
        new_data
        user
        }
        created_at
        created_by
    }
    }
    """

    data = client.execute(query)
    print("saving lifeapi.json")
    #print(json.loads(data))
    out=open(basedir+"/lifeapi.json",'w')
    out.write(json.dumps( json.loads(data),indent=6 ) )
    out.close()
    print ("Iterando:")
    j=json.loads(data)
    wl=[]
    for exam in j['data']['getEvents']:
        ex={}
        ex['accession_number']=exam['accession_number']
        ex['study_id']=exam['_id']
        datep=exam['date_string'] #"04-01-2021"
        ex['sch_study_date']=datep[6:10]+datep[3:5]+datep[0:2]
        # se deberia agregar al listado solo si la fecha coincide con el dia actual, no?
        # time_string	"10:15"
        ts=exam['time_string']
        ex['sch_study_time']=ts[0:2]+ts[3:5]+'00'
        ex['study_descripction']='NA'
        ex['procedure']=''
        ex['modality']='US'
        #ex=
        #Patient Data
        #usar tablka?
        ex['patient_name']='UNKNOWN'
        ex['patient_id']=exam['patient_doc_id']
        ex['patient_sex']='O'
        ex['patient_birth_date']='0000000'
        ex['patient_comments']=exam['appointment_reason'] #0010,4000
        ex['ref_physician']=''

        if ex['sch_study_date'] == HOY:
            wl.append(ex)
        #DB op 
        db_insert(ex)
    return wl

def mwl_dbquery(q):
    print(".. mwl db query ..")
    print(q)
    # --  ejecuta una query contra la base de datos, con los parametros de dict q
    basedir=os.path.dirname(__file__)
    try:
        conn = mariadb.connect(
            user="mwlserver",
            password="mwlserver",
            host="127.0.0.1",
            port=3306,
            database="mwlserver"
        )
        print("fine!")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return -1
    cur = conn.cursor()
    thisday=date.today().strftime("%Y-%m-%d")
    print("query fecha: "+thisday)
    print("query mod: ["+ q['modality']+']')
    #sql="select * from studies where study_date='?'  and modality='?'"
    #cur.execute(sql,(thisday,q['modality']))
    #TODO revisar por que los parametros ? no funcionan pero si el estric concatenado!
    # deberia poder aceptar el fomato de las lineas superirores
    sql="select * from studies where study_date='"+thisday+ "' and modality='"+q['modality']+"' "
    print(sql)
    cur.execute(sql )
    DB=[]
    #print("results "+str(len(cur)))
    for r in cur:
        print("...")
        row={}
        row['study_id']=r[0]
        row['accession_number']=r[2]
        row['modality']=str(r[3])
        row['sch_study_date']=r[1].strftime("%Y%m%d")
        row['procedure']=r[4]
        row['patient_id']=r[5]
        row['patient_name']=str(r[6])
        row['patient_birth_date']=r[7]
        row['patient_sex']=r[8]
        row['ref_physician']=r[9]


        DB.append(row)
    return DB



if __name__ == '__main__':
    while 1:
        load_mwl()
        sleep(15)