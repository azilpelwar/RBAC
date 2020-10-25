from RBAC.models.user import User
from RBAC.models.role import Role
from RBAC.entity.role import RoleEntity


class UserEntity():
    def __init__(self):
        self.__users = {}
        self.__populate_default_entity()

    def __populate_default_entity(self):
        all_roles = RoleEntity().get()
        self.__users["admin"] = [role for role in all_roles]
        self.__users["user"] = [
            role for role in all_roles if int(role.name[-1]) in [1, 3, 4]]
        
    def get(self):
        return self.__users
