#from requests.auth import HTTPBasicAuth
from python_graphql_client import GraphqlClient

#auth = HTTPBasicAuth('carlosok', 'carlos')
#print(auth)
client = GraphqlClient(endpoint="https://demo-back-lifeapp.herokuapp.com") 

token=""

query="""
query {
  loginUser(user: "carlosok", pass: "carlos"){
    token
  }
}
"""
data = client.execute(query=query)
print (data)
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
data = client.execute(query=query)
print(data)