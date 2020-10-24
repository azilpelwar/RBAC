from RBAC.models.action_types import ActionTypes
from RBAC.models.resources import Resources
class Role():
    def __init__(self, name:str, resource: Resource, action_type: ActionTypes):
        self.__name = name
        self.__resource = resource
        self.__action_type = action_type

    @property
    def name(self):
        return self.__name

    @property
    def resource(self):
        return self.__resource

    @property
    def action_type(self):
        return self.__action_type