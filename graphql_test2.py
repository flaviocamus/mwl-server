from graphqlclient import GraphQLClient
import json
import os

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
print(json.loads(data))
out=open(basedir+"/lifeapi.json",'w')
out.write(json.dumps( json.loads(data),indent=6 ) )
out.close()