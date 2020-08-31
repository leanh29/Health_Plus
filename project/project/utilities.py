from django.contrib.auth.models import Permission, Group


def get_user_permissions(user):
    if user.is_superuser:
        permissions = Permission.objects.all()
    else:
        permissions = user.user_permissions.all() | Permission.objects.filter(group__user=user)

    return [permission.codename for permission in permissions]

def get_user_group(user):
    if user.is_superuser:
        group = Group.objects.all()
    else:
        group = user.groups.all()

    return group


def is_permission_granted(user, permission):
    return permission in get_user_permissions(user)


def get_template_names(user, required_permission, expected_template_name):
    if is_permission_granted(user, required_permission):
        return [expected_template_name]
    else:
        return ['reject.html']


def get_template_name(user, required_permission, expected_template_name):
    return get_template_names(user, required_permission, expected_template_name)[0]
