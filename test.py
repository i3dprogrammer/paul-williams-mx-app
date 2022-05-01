import actions, config

cf = actions.init(config.CLIENT_ID, config.API_KEY, config.HOST_DEV)

actions.create_user(cf, "email@provider.com", "my-unique-id", '{\"first_name\": \"Ahmed\", \"last_name\": \"Magdy\"}')