from datetime import datetime
import actions, config, datetime

cf = actions.init(config.CLIENT_ID, config.API_KEY, config.HOST_DEV)

# Create a user, we can specify any metadata.
# actions.create_user(cf, "email@provider.com", "my-unique-id", '{\"first_name\": \"Ahmed\", \"last_name\": \"Magdy\"}')

# List users
# actions.list_users(cf)

# List Members
# actions.list_members(cf, "USR-f43da74d-e24f-4a36-a1cf-96fcef718c92")

# List transactions in last 24 hours.
# today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
# yesterday = (datetime.datetime.utcnow() - datetime.timedelta(1)).strftime("%Y-%m-%d")
# actions.list_user_transactions(cf, "USR-f43da74d-e24f-4a36-a1cf-96fcef718c92", from_date=yesterday, to_date=today)

# actions.list_accounts(cf, "USR-f43da74d-e24f-4a36-a1cf-96fcef718c92")

# actions.list_fav_institutes(cf)
# print("------------")
# actions.list_institute_required_creds(cf, "chase")

# actions.create_member(cf, "USR-f43da74d-e24f-4a36-a1cf-96fcef718c92", "chase", "my-unique-id-test", '\"credentials_last_refreshed_at\": \"2015-10-15\"')
# {'member': {'aggregated_at': None,
#             'connection_status': 'CREATED',
#             'guid': 'MBR-65c52665-33e5-4971-8d80-5c28010db001',
#             'id': 'my-unique-id-test',
#             'institution_code': 'chase',
#             'is_being_aggregated': True,
#             'is_managed_by_user': True,
#             'is_oauth': False,
#             'metadata': '"credentials_last_refreshed_at": "2015-10-15"',
#             'name': 'Chase Bank',
#             'successfully_aggregated_at': None,
#             'user_guid': 'USR-f43da74d-e24f-4a36-a1cf-96fcef718c92',
#             'user_id': 'williamp0044'}}

# actions.list_accounts(cf, 'USR-f43da74d-e24f-4a36-a1cf-96fcef718c92')
# print('-----------')
actions.list_members(cf, 'USR-f43da74d-e24f-4a36-a1cf-96fcef718c92')
print('------')
actions.delete_member(cf, 'USR-f43da74d-e24f-4a36-a1cf-96fcef718c92', 'MBR-65c52665-33e5-4971-8d80-5c28010db001')