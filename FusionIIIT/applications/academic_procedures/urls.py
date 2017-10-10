from django.conf.urls import url
from applications.academic_procedures.views import PreRegistrationView


urlpatterns = [
    url(r'^$', PreRegistrationView.as_view()),
]