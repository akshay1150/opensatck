from heatclient.client import Client as Heat_Client
from keystoneclient.v3 import Client as Keystone_Client
from flask import Flask
from flask import request
import base64
import yaml
import json

def get_keystone_creds():
    creds = {}
    creds['username'] = 'demo'
    creds['password'] = 'demo'
    creds['auth_url'] = 'http://192.168.56.111:5000/v3'
    creds['tenant_name'] = 'demo'
    return creds

creds = get_keystone_creds()
ks_client = Keystone_Client(**creds)
heat_endpoint = ks_client.service_catalog.url_for(service_type='orchestration', endpoint_type='publicURL')
heatclient = Heat_Client('1', heat_endpoint, token=ks_client.auth_token)

app = Flask(__name__)

@app.route("/create_stack",methods=['POST'])
def create_stack():
    #stack_file_path=request.args['stack_file-path']
    stack_file_path='./template.yml'
    stack_name=request.args['stack_name']
#     template=base64.decodestring(request.args['description'])
#     yaml_file=yaml.load(template)
#     example = {
#             "template" : yaml_file
#     }
    #parameters=None
    template = open(stack_file_path)
    # if parameters:
    #     stack = heatclient.stacks.create(stack_name=stack_name,
    #     template=template.read(), parameters=parameters)
    # else:
    #print(template.read())
    stack = heatclient.stacks.create(stack_name=stack_name,template=template.read())
    template.close()
#    return stack
    #return stack
#     print(type(example))
    return stack
@app.route("/delete_stack")
def delete_stack():
    stack_id=request.args['stack_id']
    heatclient.stacks.delete(stack_id)
    return "deletetion started"

@app.route("/list_stacks")
def list_stacks():
    x=heatclient.stacks.list()
    for var in x:
        return var

#create_stack('./volume.yml','volume')
#delete_stack('1e500188-1aa4-4690-8879-e11290ba03ff')

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=2100,debug='True')



