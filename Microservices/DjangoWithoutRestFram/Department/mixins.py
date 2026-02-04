from django.http import HttpResponse
from django.core.serializers import serialize
import json

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
    def serialize(self, qs, include_employees=False):
        data = []

        for dept in qs:
            dept_data = {
                "id": dept.id,
                "dept_name": dept.dept_name,
                "dept_code": dept.dept_code,
                
            }

            if include_employees:
                dept_data["employees"] = [
                    {
                        "id": emp.id,
                        "name": emp.emp_name,
                    }
                    for emp in dept.employee_set.all()
                ]
            employee_count = getattr(dept, 'emp_count', None)

            if employee_count:
                dept_data['emp_count'] = dept.emp_count 

            data.append(dept_data)

        return json.dumps(data)

class IsValidJsonMixin(object):
    def is_valid(self, json_obj)->bool:
        try:
            data = json.loads(json_obj)
            return True
        except Exception as e:
            return False
            