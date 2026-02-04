from django.shortcuts import render
from django.views import View
from .mixins import IsValidJsonMixin, HttpResponseMixin, SerializerMixin
from .forms import ProjectForm
from .models import Project
from django.http import JsonResponse
import json
# Create your views here.

class ProjectListCBV(IsValidJsonMixin, HttpResponseMixin, SerializerMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            qs = Project.objects.all().prefetch_related('asignee')
            
            data = self.serialize(qs)

            return self.render_to_http_response(data)
        except Exception as e:
            print(e)

    def post(self, request, *args, **kwargs):
        try:
            body = request.body
            
            is_json = self.is_valid(body)
            print(is_json)

            if not is_json:
                self.render_to_http_response(json.dumps({"msg":"body is not a valid json"}), 400)
                return
            project_data = json.loads(body)
            form = ProjectForm(project_data)

            if form.is_valid():
                form.save(commit=True)
                return  self.render_to_http_response(json.dumps({"msg":"resource created"}))

            if form.errors:
                print(form.errors)
                return self.render_to_http_response(json.dumps(form.errors), 400)

        except Exception as e:
            print(e)   