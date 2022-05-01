import mx_platform_python

def init(user, pw, host):
    return mx_platform_python.Configuration(username=user,password=pw,host=host)

def create_user(email, id, metadata, disabled = False):
    pass