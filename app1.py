from keystoneauth1 import loading
from keystoneauth1 import session
from heatclient import client
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(auth_url='http://192.168.56.111:5000/v3/auth/tokens',
                                   username='demo',
                                   password='demo',
                                   project_id='cb4f2411086c4c89b84114420525ab2e')
sess = session.Session(auth=auth)
heat = client.Client('1', session=sess)
x=heat.stacks.list()
print(x)
#for var in x:
#    print(var)