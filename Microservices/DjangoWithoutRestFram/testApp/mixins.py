from django.http import HttpResponse
from django.core.serializers import serialize
import json
from django.forms.models import model_to_dict

class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type = "application/json", status=status)
    

"""
 [
  {
    "model": "testApp.employee",
    "pk": 1,
    "fields": {
      "eno": 100,
      "ename": "Employee 1",
      "eaddr": "Mars"
    }
  }
]

 """
# this is designed only to extract fields obj from the above qs format response, as it can be used at multiple place.
class SerializerMixin(object):
    def serialize(self, qs, include_profile=False):

        #django in-built serialize() only works with QuerySets of model instances. Bcoz it does something like obj._meta.model_name and _meta is a Django Model internal attribute it won't work if you already perform .values, as .values returns dicts, not model instances.
        # json_data = serialize('json',qs) 

        # p_data = json.loads(json_data)
        final_fields = []
        print(type(qs))
        for emp_data in qs:
            emp = {
                "emp_name":emp_data.emp_name,
                "emp_email":emp_data.emp_email,
                "emp_id":emp_data.id,
                "salary":emp_data.salary,
                "joining_date" : emp_data.joining_date.isoformat()
            }

            profile = getattr(emp_data, "employeeprofile", None)
            department = getattr(emp_data,'department', None)
            if profile:
                emp['emp_profile'] = {
                    "phone": profile.phone_number,
                    "address": profile.address,
                    "DOB": profile.date_of_birth.isoformat()
                }
            if department:
                emp['department'] = {
                    "name":emp_data.department.dept_name,
                    "code":emp_data.department.dept_code
                }
                     
            final_fields.append(emp)        


        return json.dumps(final_fields)   

class IsValidJsonMixin(object):
    def is_valid(self, json_obj)->bool:
        try:
            data = json.loads(json_obj)
            return True
        except Exception as e:
            return False

class ROleSerializerMixin(object):
    def serialize(self, qs, include_employees=False):
        data = []
        for role in qs:
            role = {
                "title": role.title,
                "level": role.level
            }

            if include_employees:
                role["employees"] = [
                    {
                        "id": emp.id,
                        "name": emp.emp_name,
                    }
                    for emp in role.employee_set.all()
                ]
            data.append(role)    

        return json.dumps(data)    

class ManagerSerializer(object):
    def serialize(self, qs, include_subordinate=False):
        data = []
        for manager in qs:
            print(type(manager.role))
            manager_obj = {
                "name":manager.emp_name,
                "email":manager.emp_email,
                "role":(
                        {
                        "title": manager.role.title,
                        "level": manager.role.level
                        } if manager.role else None
                ),
                "subordinates": []
            }

            if include_subordinate:
                print(include_subordinate)
                for subordinate in manager.subordinates.all():
                    manager_obj['subordinates'].append({
                        "name":subordinate.emp_name,
                        "email":subordinate.emp_email,
                        "role":(
                            {
                                "title": subordinate.role.title,
                                "level": subordinate.role.level
                            } if subordinate.role else None
                         ),
                    })
            data.append(manager_obj)    
        return json.dumps(data)    



