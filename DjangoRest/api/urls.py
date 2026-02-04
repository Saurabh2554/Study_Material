from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename = 'employees')
urlpatterns = [
    path('students/',views.studentsView),
    path('student/<int:pk>',views.studentDetailView),


    # path('employees/',views.Employees.as_view()),
    # path('employee/<int:pk>',views.EmployeeDetail.as_view())

    path('', include(router.urls)),
    path('blogs/',  views.BlogsView.as_view()),
    path('comments/',  views.CommentsView.as_view()),
    path('comments/<int:pk>',  views.CommentsView.as_view())
]