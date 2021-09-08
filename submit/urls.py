from django.urls import path
from . import views
from submit.views import SuccessView, FailureView

urlpatterns = [
    path('submit', views.submit, name="submit"),
    path('submit/success', SuccessView.as_view(), name='submit_success'),
    path('submit/failure', FailureView.as_view(), name='submit_failure'),
]
