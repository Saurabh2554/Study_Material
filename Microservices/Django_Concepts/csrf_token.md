# CSRF can be exempted at three level : 
   1. ___{ At Method level}__  by using  @csrf_exempt, which we get from *** { django.views.decorators.csrf } ***
   2. ___{At class level }__ by using @method_decorator(csrf_exempt, name='dispatch'), which we get from *** { django.utils.decorators import method_decorator } ***
   3. ___{ At project level }__ by commenting the csrf related middleware in settings.py