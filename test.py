import actions, config

cf = actions.init(config.CLIENT_ID, config.API_KEY, config.HOST_DEV)

# Create a user, we can specify any metadata.
# actions.create_user(cf, "email@provider.com", "my-unique-id", '{\"first_name\": \"Ahmed\", \"last_name\": \"Magdy\"}')

# List users
# actions.list_users(cf)

# List Members
actions.list_members(cf, "USR-f43da74d-e24f-4a36-a1cf-96fcef718c92")

# List transactions
actions.list_user_transactions(cf, "USR-f43da74d-e24f-4a36-a1cf-96fcef718c92")