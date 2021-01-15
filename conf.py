import json 

def new_configuration():
    print("creando nueva configuracion")
    conf={}
    conf["ip"]=""
    conf["AEtitle"]="r192mwl"
    conf["port"]=11112
    conf["sitename"]="r192mwldemo"
    json.dump(conf,"conf.json")


def read_configuration():
    print("read configuration file")


def save_configuration(data):
    print("saving conf_file");


if __name__ == '__main__':


