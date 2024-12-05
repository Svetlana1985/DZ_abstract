# Задача №1
def requires_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if check_permissions(permission):
                return func(*args, **kwargs)
            else:
                return f"Error: Permission '{permission}' required."
        return wrapper
    return decorator

def check_permissions(permission):

    user_permissions = {'admin':True, 'user':False}
    return user_permissions.get(permission, False)

@requires_permission('admin')
def delete_user(user_id):
    return f'User {user_id} deleted'

print(delete_user(123))
print(delete_user(456))

@requires_permission('user')
def edit_profile(user_id):
    return f'Profile {user_id} edited'

print(edit_profile(789))

# Задача №2
def to_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return wrapper

@to_string
def get_number():
    return 42

@to_string
def get_text():
    return 'Hello,World!'

print(get_number())
print(get_text())





