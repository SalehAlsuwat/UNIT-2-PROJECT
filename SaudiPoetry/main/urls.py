from . import views
from django.urls import path
app_name = 'main'

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('about/', views.about_view, name="about_view"),
    path('contact/', views.contact_view, name="contact_view"),
    path('about-poetry/', views.about_poetry_view, name="about_poetry_view"),
    path('cultural-features/', views.cultural_features_view, name="cultural_features_view"),
    path('poetry-forms/', views.poetry_forms_view, name="poetry_forms_view"),
    path('poets/', views.poets_view, name="poets_view"),
    path('mode/<mode>/', views.mode_view, name="mode_view"),
]