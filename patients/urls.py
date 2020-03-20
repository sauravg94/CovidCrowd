from django.urls import path

from . import views

app_name = "patients"

urlpatterns = [
    path("", views.index, name="index"),
    path("report", views.report, name="report"),
    path("thank_you", views.thank_you, name="thank_you"),
    path("review", views.review, name="review"),
    path("logout", views.logout, name="logout"),
    path("login-form", views.login_form, name="login-form"),
    path("review-report/<int:report_id>/", views.review_report, name="review-report"),
    path("add-patient", views.add_patient, name="add-patient"),
]
