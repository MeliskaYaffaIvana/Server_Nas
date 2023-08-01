"""
URL configuration for server_nas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('api/add_folder/', views.add_folder, name='add_folder'),
    path('api/add_unix_user/', views.add_unix_user, name='add_unix_user'),
    path('api/izin_user/', views.izin_user, name='izin_user'),
    path('api/izin_data/', views.izin_data, name='izin_data'),

]


# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('api/update-containers/', views.update_containers),
#     # path('api/create-folders/', views.create_folders),
#     path('api/add-folders/', views.add_folder),
# ]


