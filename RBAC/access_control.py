from RBAC.entity.role import RoleEntity
from RBAC.entity.user import UserEntity
from RBAC.models.action_types import ActionTypes
from RBAC.models.user import User
from RBAC.models.resources import Resources
from RBAC.exceptions import InvalidInput,InvalidUser

class AccessControl():
    def __init__(self):
        self.__users = UserEntity().get()

    def authenticate(self, user: str, action_types: ActionTypes, resource: Resources):
        self.validate_input(user, action_types, resource)
        user_roles = self.__users[user]
        actions_for_resource = [role.name for role in user_roles if role.resource ==
                                resource and role.action_type == action_types]
        access_status = True if actions_for_resource else False
        return access_status

    def validate_input(self, user: str, action_types: ActionTypes, resource: Resources):
        if not user or not action_types or not resource:
            raise InvalidInput
        if user not in self.__users:
            raise InvalidUser
        if action_types not in ActionTypes:
            raise InvalidActionType
        if resource not in Resources:
            raise InvalidResource
