from django.urls import path
from . import views

# urls connect to the corresponsing functions in views.py
urlpatterns = [
    path('fundraisers/', views.FundraiserList.as_view()),
    path('fundraisers/<int:pk>/', views.FundraiserDetail.as_view()),
    path('pledges/', views.PledgeList.as_view())
]