from RBAC.models.user import User
from RBAC.models.role import Role
from RBAC.entity.role import RoleEntity
from RBAC.entity.user import UserEntity

class UserEntity():
    def __init__(self):
        self.__users={}
        self.__populate_default_entity()
    
    def __populate_default_entity(self):
        all_roles = RoleEntity().get()
        self.__users["admin"] = [role for role in all_roles]
        self.__users["user1"] = [role for role in all_roles if role.name]

    def get(self):
        return self.__users