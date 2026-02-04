import json
from django.http import HttpResponse
from django.core.serializers import serialize

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
    def serialize(self, qs):
        #serialize() only works with QuerySets of model instances. it won't work if you already perform .values, as returns dicts, not model instances.
        json_data = serialize('json',qs) 

        p_data = json.loads(json_data)
        print(p_data)
        final_fields = []
        for obj in p_data:
            final_fields.append(obj['fields'])

        return json.dumps(final_fields) 

class IsValidJsonMixin(object):
    def is_valid(self, json_obj)->bool:
        try:
            data = json.loads(json_obj)
            return True
        except Exception as e:
            return False
        

class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type = "application/json", status=status)
            
