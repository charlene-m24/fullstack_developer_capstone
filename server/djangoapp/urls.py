# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='login', view=views.login_user, name='login'),
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path(route='logout', view=views.logout_request, name="logout"),
     path(route="register", view=views.registration, name="signup"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
