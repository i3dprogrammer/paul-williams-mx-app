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

def delete_user(configuration, user_guid):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)

        try:
            api_instance.delete_user(user_guid)
            pprint(f"{user_guid} deleted succesfully")
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->delete_user: %s\n" % e)

def create_member(configuration, user_guid, institute_code, id, metadata):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        user_guid = user_guid
        request_body = MemberCreateRequestBody(  
            member = MemberCreateRequest(    
                background_aggregation_is_disabled = False,
                credentials = [
                    CredentialRequest(        
                        guid = "CRD-a7fc25d4-7631-44ed-bb32-3127a5b41a13",
                        value = "username"
                    ),
                    CredentialRequest(        
                        guid = "CRD-19fcbc11-d1bd-4a2a-b114-234c2508e6bb",
                        value = "password"
                    ),
                ],
                id = id,
                institution_code = institute_code,
                is_oauth = False,
                metadata = metadata,
                skip_aggregation = False
            ),
            referral_source = 'APP',
            ui_message_webview_url_scheme = 'mx'
        )

        try:
            api_response = api_instance.create_member(user_guid, request_body)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->create_member: %s\n" % e)

def delete_member(configuration, user_guid, member_guid):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)

        try:
            api_instance.delete_member(member_guid, user_guid)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->delete_member: %s\n" % e)

def list_users(configuration):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 100

        try:
            api_response = api_instance.list_users(page=page, records_per_page=records_per_page)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_users: %s\n" % e)

def list_fav_institutes(configuration):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 10

        try:
            api_response = api_instance.list_favorite_institutions(page=page, records_per_page=records_per_page)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_favorite_institutions: %s\n" % e)

def list_institutes(configuration, query):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 10
        supports_account_identification = True
        supports_account_statement = True
        supports_account_verification = True
        supports_transaction_history = True

        try:
            api_response = api_instance.list_institutions(name=query, page=page, records_per_page=records_per_page, supports_account_identification=supports_account_identification, supports_account_statement=supports_account_statement, supports_account_verification=supports_account_verification, supports_transaction_history=supports_transaction_history)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_institutions: %s\n" % e)

def list_institute_required_creds(configuration, institute_code):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 100

        try:
            api_response = api_instance.list_institution_credentials(institute_code, page=page, records_per_page=records_per_page)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_institution_credentials: %s\n" % e)

def list_user_transactions(configuration, user_guid, from_date=None, to_date=None):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 100
        
        try:
            api_response = api_instance.list_transactions(user_guid, from_date=from_date, page=page, records_per_page=records_per_page, to_date=to_date)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_transactions: %s\n" % e)

def list_members(configuration, user_guid):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 100

        try:
            api_response = api_instance.list_members(user_guid, page=page, records_per_page=records_per_page)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_members: %s\n" % e)

def list_accounts(configuration, user_guid):
    with mx_platform_python.ApiClient(configuration, 'Accept', 'application/vnd.mx.api.v1+json') as api_client:
        api_instance = mx_platform_api.MxPlatformApi(api_client)
        page = 1
        records_per_page = 100

        try:
            api_response = api_instance.list_user_accounts(user_guid, page=page, records_per_page=records_per_page)
            pprint(api_response)
        except mx_platform_python.ApiException as e:
            print("Exception when calling MxPlatformApi->list_members: %s\n" % e)