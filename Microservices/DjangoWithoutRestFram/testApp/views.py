from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.forms.models import model_to_dict
from django.db import transaction
from .mixins import HttpResponseMixin, ManagerSerializer, SerializerMixin, IsValidJsonMixin, ROleSerializerMixin
from .models import Employee, EmployeeProfile, EmployeeRole
from .forms import EmployeeForms, EmployeeProfileForm
from django.db.models import Count, Q, Avg, OuterRef, Subquery, F, Max
from functools import reduce
from operator import or_
from django.utils import timezone
from datetime import timedelta


import json
# Create your views here.
#Function based views

def func_based_view(request,*args, **kwargs):
    em = {
        "em_no":"123",
        "em_name":"emp-1",
        "em_age":23,
        "em_gender":"Male"
        
    }
    json_data = json.dumps(em)
    
    if request.method == "GET":
        return HttpResponse(json_data, content_type="application/json")
    
    elif request.method == "POST":
        print(json.loads(request.body)) # In case if something sent via form, we will have to do request.POST
        print("Sending post request...")
        return HttpResponse(json_data, content_type="application/json")
    
# Function based views are not generally used in prod level code...



# Here we are writting same code(return HttpResponse(json_data, content_type = "application/json") ) again and again. So in order to promote code reusability we can use mixins. Mixins are nothing but a class inherited directly from Object class, which can hold numerous lines of repetitive code , promoting code reusaility by using the concept of Multiple Inheritance. Note Mixins does not have instance variables.
class ClassBasedViews(HttpResponseMixin,View):
    
    # used to handle get request--->
    def get(self, request, *args, **kwargs):
        json_data = json.dumps({"msg":"This is the response from get"})
        return self.render_to_http_response(json_data)
    
    def post(self, request, *args, **kwargs):
        json_data = json.dumps({"msg":"This is the response from Post"})
        return self.render_to_http_response(json_data)
    
    def put(self, request, *args, **kwargs):
        json_data = json.dumps({"msg":"This is the response from Put"})
        return self.render_to_http_response(json_data)

    def delete(self, request, *args, **kwargs):
        json_data = json.dumps({"msg":"This is the response from delete"})
        return self.render_to_http_response(json_data)


# CRUD Operation on Employee model using class based view

from django.core.serializers import serialize # it's a built-in django package used for serialization and de-serialization. 

class EmployeeDetailCBV(HttpResponseMixin,SerializerMixin,IsValidJsonMixin,View):
    def get_object_by_id(self, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp=None
        return emp    
    
    def get(self, request, id, *args, **kwargs):
        try:
            print(id)
            emp = self.get_object_by_id(id)
            # json_emp = json.dumps(emp) # not possible because Employee object is not json serializable. so we will manually have to create json by extracting fields.

            # Manual serializattion----
            # emp_dict = {
            #     "empno":emp.eno,
            #     "emname":emp.ename,
            #     "empaddr":emp.eaddr,
            # }
            # emp_json = json.dumps(emp_dict) # Serializing python dict to json string to send over network. Manual Serialization process

            # Serialization using django serializers package
            # emp_json = serialize('json', [emp,], fields=('eno','ename','eaddr'))
            emp_json = self.serialize([emp,])

            return HttpResponse(emp_json, content_type = "application/json")
        except Exception as e:
            print("some error occurred: ", e)
    
    # def delete(self, request, *args, **kwargs):
    #     Employee.objects.all().delete()
    
    def put(self, request, id, *args, **kwargs):
        try:
            existing_emp = self.get_object_by_id(id)
            if existing_emp is None:
                return self.render_to_http_response(json.dumps({'msg':'Requested resource not available.'}), 400)

            data = request.body
            json_data = self.is_valid(data)
            provided_data = json.loads(data)

            # this approach is not acceptable in prod. Rather make a seperate updateEmployeeForm dedicated to update operations.
            original_data = {
                **model_to_dict(existing_emp)
            }.update(provided_data)
            print(original_data)

            if not json_data:
                return self.render_to_http_response(json.dumps({"msg":"body is not a valid json"}, 400))
            
            update_form = EmployeeForms(original_data, instance=existing_emp)

            if update_form.is_valid():
                self.render_to_http_response(json.dumps({'msg':'resource updated successfully.'}), 201)

            if update_form.errors:
                return self.render_to_http_response(json.dumps(update_form.errors), 400)
        except Exception as e:
            print("ex", e)


# SerializerMixin is designed manually only to extract fields obj from queryset
class EmployeeListCBV(SerializerMixin, HttpResponseMixin, IsValidJsonMixin, View):
    def create_employee_with_profile(self, emp_data, profile_data=None):
        emp_form = EmployeeForms(emp_data)

        if emp_form.errors:
            return self.render_to_http_response(json.dumps(emp_form.errors), 400)
        
        profile_form = None
        if profile_data:
            profile_form = EmployeeProfileForm(profile_data)

            if profile_form.errors:
                return self.render_to_http_response(json.dumps(profile_form.errors), 400)
            
        with transaction.atomic():
            employee = emp_form.save()

            if profile_form:
                profile = profile_form.save(commit=False)
                profile.employee =  employee
                profile.save()   
        
        return self.render_to_http_response(json.dumps({'msg':'resource created.'}), 201)
    

    def get(self, request, *args, **kwargs):
      #1. Get all employees without profiles (can be done in two ways)
        # qs = Employee.objects.filter(employeeprofile__isnull=True)
        # qs = Employee.objects.select_related('employeeprofile').annotate(profile_count=Count('employeeprofile_id')).filter(profile_count=0)

      #2. Get employees who joined in last 30 days  
        # last_30_days_date = timezone.now() - timedelta(30)
        # qs = Employee.objects.filter(joining_date__gte=last_30_days_date)

      #3. Fetch employees with no department (can be done in two ways)
        # qs = Employee.objects.filter(department__isnull=True)  
        # qs1 = Employee.objects.values('emp_name','department_id').annotate(dept_count=Count('department_id')).filter(dept_count__gte=0)
        # qs = Employee.objects.select_related('department').annotate(dept_count=Count('department_id')).filter(dept_count__gte=0)

      #4. Employees whose name starts with “A”
        # qs = Employee.objects.filter(emp_name__istartswith = 'a')  

      #5. Employees having profile but no address
        # qs = Employee.objects.filter(Q(employeeprofile__isnull=False) & Q(employeeprofile__address__isnull=True))
        # print(qs)

      #6. Employees with duplicate emails
        # qs = Employee.objects.values('emp_email').annotate(email_count = Count('emp_email')).filter(email_count__gt=1).values_list('emp_email', flat=True)  
        # qs2 = Employee.objects.filter(emp_email__in = qs)

      #9. Employees ordered by joining date (desc)
        # qs = Employee.objects.order_by('-joining_date') 

      #10. Employees with profile + department in single query
        # qs = Employee.objects.select_related('employeeprofile','department')  

      #11. Employees whose salary is ABOVE their department’s average  
        # qs = Employee.objects.filter(department=OuterRef('department')).values('department').annotate(avg_salary = Avg('salary')).values_list('avg_salary', flat=True)
        # qs2 = Employee.objects.annotate(avg_salary = Subquery(qs)).filter(salary__gte = F('avg_salary'))

      #12. Highest paid employee in each department
        # qs = Employee.objects.filter(department=OuterRef('department')).values('department').annotate(maxm_salary = Max('salary')).values_list('maxm_salary', flat=True)
        # qs2 = Employee.objects.annotate(maxm_salary_per_dept = Subquery(qs)).filter(salary = F('maxm_salary_per_dept'))

      #13. Departments where average salary > 3000
        # qs = Employee.objects.values('department').annotate(avg_sal = Avg('salary')).filter(avg_sal__gt=8000)
      # For each department, return:
            #  department name
            #  total employees
            #  average salary
            #  max salary

        # qs = Employee.objects.values('department').annotate(total_emp = Count('id')).annotate(avg_salary = Avg('salary')).annotate(maxm_salary = Max('salary')).values('department__dept_name','total_emp','avg_salary','maxm_salary')

      #15. Employees whose salary is greater than their manager’s salary
        # qs = Employee.objects.filter(salary__gt=F('manager__salary')).values('emp_name','salary','manager__salary') 

      #17. Departments having at least one employee earning more than 2× department average
        # qs = Employee.objects.filter(department=OuterRef('department')).values('department').annotate(avg_sal = Avg('salary')).values_list('avg_sal', flat=True)
        # qs2 = Employee.objects.annotate(avg_sal_per_dept = Subquery(qs)).filter(salary__gt = F('avg_sal_per_dept')).values('department').distinct() # here i can also write .filter(salary__gt = Subquery(qs)).values('department').distinct()
   
        print(qs)

        data = self.serialize(qs)
        return self.render_to_http_response(data)
        pass
    
    def post(self, request, *args, **kwargs):
        data = request.body
        valid_json = self.is_valid(data)

        if not valid_json:
            self.render_to_http_response(json.dumps({"msg":"body is not a valid json"}, 400))
            return
        
        json_data = json.loads(data)
        payload = json_data.copy()
        profile = json_data.pop('profile',None)

        return self.create_employee_with_profile(payload, profile)


class EmployeeProfileListCBV(SerializerMixin,HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            qs = EmployeeProfile.objects.select_related("employee").prefetch_related('employee__department').values(
                "id",
                "phone_number",
                "employee__id",
                "employee__emp_name",
                "employee__emp_email",
                "employee__department__id",
                "employee__department__dept_name",

            )

            return JsonResponse(list(qs), safe=False)
        except Exception as e:
            print(e)

        
class EmployeeRoleListCBV(ROleSerializerMixin, HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            qs = EmployeeRole.objects.all()
            include_employee = request.GET.get('employee') == 'true'
            print(include_employee)

            if include_employee:
                qs = qs.prefetch_related('employee_set')

            serialize = self.serialize(qs, True)
            print(serialize)
            return self.render_to_http_response(serialize)
        except Exception as e:
            print(e)


class ManagerRoleListCBV(ManagerSerializer, HttpResponseMixin, View):
    def get(self, request, *args, **kwargs):     
        try:
            qs = Employee.objects.filter(manager__isnull = True)

            include_subordinate = request.GET.get('include_subordinate').lower().strip() == 'true'

            if not include_subordinate:
                qs = qs.select_related('role').prefetch_related('subordinates') # Here if you won't use select_related, still you will be able to access role(see mixin) but that will be doing N+1 query thing means for each manager/subordinates it will fire a seperate query to db

            serialized_data = self.serialize(qs, True)    

            return self.render_to_http_response(serialized_data)
        except Exception as e:
            print(e)

