from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('marriage/', views.marriage, name= 'marriage'),
    path('funeral-burial/', views.funeral_burial, name= 'funeral-burial'),
    path('care-4-converts/', views.convert_group, name= 'convert_group'),
    path('interfaith/', views.interfaith, name= 'interfaith'),
    path('financial-assistance/', views.financial_assistance, name= 'financial_assistance'),
    path('community-relief/', views.community_relief, name= 'community_relief'),
    path('zakat/', views.zakat, name= 'zakat'),
]

