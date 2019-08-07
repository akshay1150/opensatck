from heatclient.client import Client as Heat_Client
from keystoneclient.v3 import Client as Keystone_Client

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


def create_stack(stack_file_path, stack_name, parameters=None):
    template = open(stack_file_path)
    if parameters:
        stack = heatclient.stacks.create(stack_name=stack_name,
        template=template.read(), parameters=parameters)
    else:
        stack = heatclient.stacks.create(stack_name=stack_name,
        template=template.read())
        template.close()
    return stack

def delete_stack(stack_id):
    heatclient.stacks.delete(stack_id)

def list_stacks():
    return heatclient.stacks.list()

#create_stack('./volume.yml','volume')
#delete_stack('1e500188-1aa4-4690-8879-e11290ba03ff')
x=list_stacks()
print(type(x))
for var in x:
    print(var)
    break

