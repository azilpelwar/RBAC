## Role Based Access Control:

A role based auth system is able to assign a role to a user and remove a role from a user.

Entities are USER, ACTION TYPE, RESOURCE, ROLE

ACTION TYPE defines the access level (Ex: READ, WRITE, DELETE)

Access to resources for users are controlled strictly by the role. One user can have multiple roles. Given a user, action type and resource, the system should be able to tell whether user has access or not.