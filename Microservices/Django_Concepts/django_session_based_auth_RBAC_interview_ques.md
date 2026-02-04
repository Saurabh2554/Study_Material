Perfect — this is exactly the **right moment** to consolidate everything you’ve learned before moving to JWT.

Below is a **carefully curated, interview-grade question bank** covering **Django Authentication, Authorization, Permissions, RBAC, and Object-level access**.

This set is designed so that **if you can confidently answer all of these, you are 100% ready for real interviews** (SDE-1 / SDE-2 level).

---

# ✅ DJANGO AUTHENTICATION & AUTHORIZATION – COMPLETE QUESTION SET

---

## 🔹 SECTION 1: Core Authentication (Foundations)

1. What is authentication in Django?
2. What is the difference between authentication and authorization?
3. How does Django authenticate a user internally?
4. What is `django.contrib.auth`?
5. What are the default fields in Django’s `User` model?
6. What happens internally when `authenticate()` is called?
7. What does `login()` do internally?
8. What is stored in the session after login?
9. What is `request.user` and how is it populated?
10. Difference between `AnonymousUser` and `User` object.

---

## 🔹 SECTION 2: Session-Based Authentication (Very Important)

11. What is a session in Django?
12. Where are Django sessions stored?
13. How does Django map a session to a logged-in user?
14. What happens when a user logs out?
15. What is `SESSION_ENGINE`?
16. Difference between session-based auth and token-based auth.
17. How does Django protect sessions from tampering?
18. What is session fixation and how does Django prevent it?
19. What happens if session expires?
20. Can two users share the same session? Why / why not?

---

## 🔹 SECTION 3: Django User Model & Customization

21. What is `AbstractUser` vs `AbstractBaseUser`?
22. When should you create a custom user model?
23. What happens if you change the User model after migrations?
24. Why is `AUTH_USER_MODEL` important?
25. What fields are mandatory in a custom user model?
26. How does `UserManager` work?
27. What is `create_user()` vs `create_superuser()`?
28. Why is `set_password()` necessary?
29. What happens if you save password directly?
30. How to link a User with Employee/Profile model?

---

## 🔹 SECTION 4: Authorization & Permissions

31. What are Django permissions?
32. How many default permissions are created per model?
33. What is the format of permission codenames?
34. How do permissions get stored in the database?
35. How to check permission in views?
36. Difference between `has_perm()` and `has_perms()`?
37. How to restrict access using decorators?
38. What is `@login_required`?
39. What is `PermissionRequiredMixin`?
40. How to restrict API endpoints based on permissions?

---

## 🔹 SECTION 5: Groups & Role-Based Access Control (RBAC)

41. What is a Group in Django?
42. How are permissions assigned to groups?
43. How do users inherit permissions from groups?
44. Difference between role-based and permission-based access?
45. Where should group creation logic live?
46. Should group assignment happen during registration or admin?
47. How to check if a user belongs to a group?
48. Can a user belong to multiple groups?
49. What happens if user has conflicting permissions?
50. Real-world example of RBAC implementation.

---

## 🔹 SECTION 6: Object-Level Permissions

51. What are object-level permissions?
52. Why are they not supported natively in Django?
53. How does Django Guardian help?
54. Difference between model-level and object-level permissions?
55. Example use-case for object-level permissions.
56. How to check object-level permission manually?
57. Performance implications of object-level permissions?
58. When should you avoid object-level permissions?

---

## 🔹 SECTION 7: Advanced & Practical Scenarios

59. How do you restrict users to access only their own records?
60. How do you secure views without decorators?
61. How to protect class-based views?
62. How to implement admin-only access?
63. How to prevent privilege escalation?
64. How to audit permission-related bugs?
65. What happens if a user is deleted?
66. What happens to their sessions?
67. What happens to related permissions?
68. How do you revoke access immediately?
69. How do you test authentication logic?
70. How do you debug permission issues?

---

## 🔹 SECTION 8: Interview-Oriented Scenario Questions

71. User can view but not edit profile — how?
72. Admin can edit all users, others only self — design?
73. Multiple roles per user — how to handle?
74. Feature accessible only to managers — how?
75. How would you design access control for an HR system?
76. How to restrict access based on department?
77. How to restrict based on both role + ownership?
78. How to design scalable permission architecture?
79. How to migrate permission changes safely?
80. How to test permissions efficiently?

---

## 🔹 SECTION 9: Common Mistakes (Interview Gold)

81. Storing passwords manually
82. Using `is_staff` incorrectly
83. Confusing groups with roles
84. Hardcoding permission checks
85. Forgetting to protect APIs
86. Overusing decorators
87. Not revoking sessions
88. Not rotating secrets
89. Not logging auth failures
90. Mixing authentication with authorization

---

## 🔹 SECTION 10: Conceptual Understanding (High Value)

91. Why is authentication stateful in Django?
92. Why JWT is stateless?
93. When NOT to use JWT?
94. When is session-based auth better?
95. Why permissions should not be in frontend?
96. Difference between access control & business rules
97. Why RBAC is preferred over hardcoded checks?
98. How Django ensures security by default?
99. How would you design auth for microservices?
100. What changes when scaling to millions of users?

---

## 🎯 Final Verdict

If you can **confidently answer 80–90% of these**, you are:

✅ **Interview-ready for backend roles**
✅ **Strong in Django security fundamentals**
✅ **Ready to move to JWT & advanced auth systems**


