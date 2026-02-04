from django.shortcuts import render
from django.views.generic import View
from .mixins import SerializerMixin, HttpResponseMixin, IsValidJsonMixin
from .models import Department
from .forms import DepartmentForms
from django.db.models import Count, Avg, Max
from django.http import JsonResponse
import json
# Create your views here.

class DepartmentListCBV(SerializerMixin, HttpResponseMixin, IsValidJsonMixin, View):

    def get(self, request, *args, **kwargs):
        try:
          #4. Count employees per department
            # qs = Department.objects.annotate(emp_count = Count('employee')).values('dept_name','dept_code','emp_count')
            # print(qs.query)
            # return JsonResponse(list(qs), safe=False)

          #8. Departments with more than 5 employees
            # qs = Department.objects.annotate(emp_count = Count('employee__id')).filter(emp_count__gt=5)  
          # For each department, return:
            #  department name
            #  total employees
            #  average salary
            #  max salary  

           

            print(qs)
        
            json_data = self.serialize(qs, True)
            return self.render_to_http_response(json_data)
        except Exception as e:
            print(e)

    def post(self, request, *args, **kwargs):
        try:
            data = request.body
            valid_data = self.is_valid(data)

            if not valid_data:
                return self.render_to_http_response(json.dumps({'msg':"data is not a valid json"},status = 400))
            
            deptData = json.loads(data)
            form = DepartmentForms(deptData)

            if form .is_valid():
                form.save(commit=True)
                self.render_to_http_response({'msg':'Resource created successfully.'})

            if form.errors:
                return self.render_to_http_response(json.dumps(form.errors), 400)

        except Exception as e:
            pass 

