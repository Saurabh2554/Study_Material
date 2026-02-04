"""
URL configuration for withoutRest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
# from django.conf.urls import url -- deprecated
from testApp.views import func_based_view, ClassBasedViews, EmployeeDetailCBV, EmployeeListCBV, EmployeeProfileListCBV, EmployeeRoleListCBV, ManagerRoleListCBV
from Project.views import ProjectListCBV
from User.views import login_view, logout_view, register
from Department.views import DepartmentListCBV
import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path('api/funcBasedView',func_based_view),
    path('api/classBasedView',ClassBasedViews.as_view()),
    re_path(r'api/employee/(?P<id>\d+)/$',EmployeeDetailCBV.as_view()), #$ represents no value after id
    path('api/employee/',EmployeeListCBV.as_view()), #$ represents no value after id
    path('api/department/',DepartmentListCBV.as_view()), #$ represents no value after id
    path('api/employee_profile/',EmployeeProfileListCBV.as_view()),
    path('api/role/',EmployeeRoleListCBV.as_view()),
    path('api/employee/manager/',ManagerRoleListCBV.as_view()),
    path('api/project/',ProjectListCBV.as_view()),
    path('api/login/', login_view, name='login'),
    path('api/logout/', logout_view, name='logout'),
    path('api/register/', register, name='logout'),
]
