# What is Authorization ?
 ANS: Authorization determines what an authenticated user is allowed to do. It defines the permissions and access levels granted to the user. It can be done by creatng permission and access to any specific resource.
    For Ex: After logging in, a user might have access to their profile and settings but not to administrative functions.

# What are different types of Access control used in application development?
 ANS: There are couple of Access control strategies, such as Role-Based-Access-Control(RBAC), Attribute/Object-Based-Access-Control(ABAC), Graph-Based-Access-Control    (GBAC), Discretionary Access Control (DAC). Each one of these strategies will help application developers deal with different authorization requirements and authorization services.

# What is Attribute-Based Access Control (ABAC) and Authorization?
 ANS: Here we define whether a user has sufficient access privilages/permission based on some attribute or field. For example An example use case of this authorization process is an online store that sells alcoholic beverages. A user of the online store needs to register and provide proof of their age. The age of the consumer validated during the registration process is a claim, that is the proof of the user’s age attribute
 Presenting the age claim allows the store to process access requests to buy alcohol. So, in this case, the decision to grant access to the resource is made upon the user attribute.

# What is Role-Based Access Control (RBAC) and Authorization?
 ANS: Here we define couple of roles(In django we call it Groups) and assigns different permission to it. Post that we add users to this group, in this way the permission given to the group will also be applicable to the users. Permission can be also given to user directly. For ex, in case when we may have user like Admin, manager and employee, we will create three seperate group and assignes different level permission to it. Then upon user's registeration we will add different users to these groups based on attribute like is_admin or is_manager.
 This is comparetively easier way of implementing access-control and authorization.

# What is Relationship-Based Access Control (ReBAC) and Authorization? 
 ANS: 
