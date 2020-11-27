# import lithops

# config = {'lithops' : {'storage_bucket' : 'bucket-gerard-eu-gb'},

#           'ibm_cf':  {'endpoint': 'https://eu-gb.functions.cloud.ibm.com',
#                       'namespace': 'cloudbutton@uvigo.es_dev',
#                       'api_key': 'c8a9e3ec-51c9-413b-ac23-e10c3ccb71e1:k3GoGB7GRgyNFYI3ob97GAuKt8ORPYJ9eWjCfIygD0d2xeR9aowjaQlvgm7HhlPm'},

#           'ibm_cos': {'endpoint': 'https://s3.eu-gb.cloud-object-storage.appdomain.cloud',
#                       'private_endpoint': 'https://s3.private.eu-gb.cloud-object-storage.appdomain.cloud',
#                       'api_key': '0GRleyXkQsvdhokMlmI0Ve-p7WxAhnKCJz9F-M7bu9qe'}}

# def hello_world(name):
#     return 'Hello {}!'.format(name)

# if __name__ == '__main__':
#     fexec = lithops.function_executor(config=config)
#     fexec.call_async(hello, 'World')
#     print(fexec.get_result())

import lithops

config = {'lithops' : {'storage_bucket' : 'BUCKET_NAME'},

          'ibm_cf':  {'endpoint': 'HOST',
                      'namespace': 'NAMESPACE',
                      'api_key': 'API_KEY'},

          'ibm_cos': {'endpoint': 'ENDPOINT',
                      'private_endpoint': 'PRIVATE_ENDPOINT',
                      'api_key': 'API_KEY'}}

def hello_world(name):
    return 'Hello {}!'.format(name)

if __name__ == '__main__':
    fexec = lithops.function_executor(config=config)
    fexec.call_async(hello, 'World')
    print(fexec.get_result())