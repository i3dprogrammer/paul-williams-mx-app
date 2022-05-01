from distutils.command.config import config
import mx_platform_python
from mx_platform_python.api import mx_platform_api
from mx_platform_python.models import *
from pprint import pprint

def init(user, pw, host):
    return mx_platform_python.Configuration(username=user,password=pw,host=host)

def create_user(configuration, email, id, metadata, disabled = False):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        request_body = UserCreateRequestBody(  
            user = UserCreateRequest(    
                email = email,
                id = id,
                is_disabled = disabled,
                metadata = metadata
            )
        )

        try:
            api_response = api_instance.create_user(request_body)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->create_user: %s\n" % e)

def list_users(configuration):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 10

        try:
            api_response = api_instance.list_users(page=page, records_per_page=records_per_page)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_users: %s\n" % e)