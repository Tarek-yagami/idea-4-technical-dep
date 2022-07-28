import json

from delete import delete_firewall_rule

def purge():
    jsonfile=open('chall.json','r')
    jsondata=jsonfile.read()
    pythonlist=json.loads(jsondata)
    for i in pythonlist :
        the_merge="-".join("allow",i.get("category"),i.get("name"))
        projectid="project id"
        delete_firewall_rule(project_id=projectid,firewall_rule_name=the_merge)
        
    return 



