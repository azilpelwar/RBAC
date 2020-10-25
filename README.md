## Role Based Access Control:

A role based auth system is able to assign a role to a user and remove a role from a user.

Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level  (READ, WRITE, DELETE)

Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system should be able to tell whether user has access or not.

The RBAC system supports following resources:
#### FILE STORAGE
#### DATABASE
#### DEVICE MANAGEMENT

To add new resources, add a enum variable in RBAC/models/resources.py

The RBAC system supports following action types:
#### READ
#### WRITE
#### DELETE

To add new action types, add a enum variable in RBAC/modesl/action_types.py

Currently the system supports adding the users and roles via adding entries in RBAC/entity/user.py. No runtime addition of user and roles is currently supported.

### Code structure:
* RBAC/models/
    * action_types.py
        Stores all the supported action types for any resources in the system
    * resources.py
        Keeps the record of all supported resources
    * roles.py
        Stores the roles for a each resource and action type
    * user.py
        Stores the user details such as user name and its assined roles
*RBAC/entity
    * user.py
        Contains the user interaction methods. To add more users add it in populate_default_entity() method
    * role.py
        Contains the role interation methods. To add more roles add those in populate_default_entity() method
*RBAC/
    * access_control.py
        Class to manage the access control, it authenticates/validates whther the user has access to specific role and action type
    * exceptions.py
        Defines the exceptions to be used in RBAC

* driver.py
    Contain the driver method which displays the all the supported users, roles, action types. This class takes the user input and checks whether the user-resource-action type is allowed or denied by validating the user input.

## To run the program run following command from root of the folder:
    * python3 driver.py