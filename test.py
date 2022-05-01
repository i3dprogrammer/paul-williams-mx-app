import actions, config

cf = actions.init(config.CLIENT_ID, config.API_KEY, config.HOST_DEV)

# Create a user, we can specify any metadata.
# actions.create_user(cf, "email@provider.com", "my-unique-id", '{\"first_name\": \"Ahmed\", \"last_name\": \"Magdy\"}')

# List users
actions.list_users(cf)