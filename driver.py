from RBAC.entity.user import UserEntity
from RBAC.entity.role import RoleEntity
from RBAC.access_control import AccessControl
from RBAC.models.resources import Resources as resources
from RBAC.models.action_types import ActionTypes as actionTypes
from RBAC.exceptions import InvalidActionType, InvalidResource, InvalidRole, InvalidUser
import sys
import traceback



class Driver():
    def __init__(self):
        self.__all_users = UserEntity().get()

    def select_user(self):
        selected_user = None
        print("Select a user from following list:")
        for index, user in enumerate(self.__all_users.keys()):
            print(f'{index+1} {user}')

        selected_no = int(input(":"))

        for index, user in enumerate(self.__all_users.keys()):
            if index+1 == selected_no:
                selected_user = user

        if selected_user==None:
            raise InvalidUser
        return selected_user

    def select_resource(self):
        selected_resource = None
        print("Select a resource:")
        for index, resource in enumerate(resources):
            print(f'{index+1} {resource.name}')
        
        selected_no = int(input(":"))

        for index, resource in enumerate(resources):
            if index+1 == selected_no:
                selected_resource = resource

        if selected_resource==None:
            raise InvalidResource
        return selected_resource

    def select_action_type(self):
        selected_action_type = None
        print("Select a action Types:")
        for index, action_type in enumerate(actionTypes):
            print(f'{index+1} {action_type.name}')
        
        selected_no = int(input(":"))
        for index, action_type in enumerate(actionTypes):
            if index+1 == selected_no:
                selected_action_type = action_type

        if selected_action_type==None:
            raise InvalidActionType
        return selected_action_type
    def show_all_users(self):
        for user, roles in self.__all_users.items():
            [print(f'{user}     {str(role.resource.value)}      {str(role.action_type.value)}') for role in roles]
if __name__ == "__main__":
    try:
        choice = 1
        driver = Driver()
        driver.show_all_users()
        selected_user = driver.select_user()
        selected_resource = driver.select_resource()
        selected_action_type = driver.select_action_type()
        print("I am here")
        auth_status = AccessControl().authenticate(
            selected_user, selected_action_type, selected_resource)
        if auth_status:
            print("Access Provided")
        else:
            print("Access Denied")

    except InvalidActionType:
        print("Invalid action type selected")
    except InvalidUser:
        print("Invalid user selected")
    except InvalidResource:
        print("Invalid Resource selected")
    except InvalidRole:
        print("Invalid Role selected")
    
