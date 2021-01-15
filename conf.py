import json 

def new_configuration():
    print("creando nueva configuracion")
    conf={}
    conf["ip"]=""
    conf["AEtitle"]="r192mwl"
    conf["port"]=11112
    conf["sitename"]="r192mwldemo"
    cf=open("conf.json","w")
    json.dump(conf,cf,indent=6)


def read_configuration():
    print("read configuration file")
    with open("conf.json","r") as cf:
        data=cf.read()
        return json.loads(data)



if __name__ == '__main__':
    print("Crear archivo de configuracion?")
    response=input()
    if response in ['y','Y','s','S']:
        new_configuration()
        print("archivo creado")
    else:
        print(read_configuration() )

        

