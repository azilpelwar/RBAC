from RBAC.models.role import Role
from RBAC.models.user import User
from RBAC.models.action_types import ActionTypes
from RBAC.models.resources import Resources


class RoleEntity():
    def __init__(self):
        self.__roles = []
        self.__populate_default_entity()

    def __populate_default_entity(self):
        counter = 1
        for resource in Resources:
            for action_type in ActionTypes:
                self.__roles.append(Role(name="role{}".format(
                    counter), resource=resource, action_type=action_type))
                counter += 1

    def get(self):
        return self.__roles
