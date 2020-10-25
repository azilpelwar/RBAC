from RBAC.entity.user import UserEntity
from RBAC.entity.role import RoleEntity
from RBAC.access_control import AccessControl
from RBAC.models.resources import Resources as resources
from RBAC.models.action_types import ActionTypes as actionTypes
from RBAC.exceptions import InvalidActionType, InvalidResource, InvalidRole, InvalidUser

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
        print(f'User     Resource Name      Action Type')
        for user, roles in self.__all_users.items():
            [print(f'{user}     {str(role.resource.value)}      {str(role.action_type.value)}') for role in roles]

if __name__ == "__main__":
    try:
        driver = Driver()
        driver.show_all_users()
        selected_user = driver.select_user()
        selected_resource = driver.select_resource()
        selected_action_type = driver.select_action_type()
        auth_status = AccessControl().authenticate(
            selected_user, selected_action_type, selected_resource)
        if auth_status:
            print(f'Access Provided for {selected_user} -> {selected_resource.value} -> {selected_action_type.value}')
        else:
            print(f'Access Denied for {selected_user} -> {selected_resource.value} -> {selected_action_type.value}')

    except InvalidActionType:
        print("Invalid action type selected")
    except InvalidUser:
        print("Invalid user selected")
    except InvalidResource:
        print("Invalid Resource selected")
    except InvalidRole:
        print("Invalid Role selected")