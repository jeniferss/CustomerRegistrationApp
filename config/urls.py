from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from client.views.client_list import ClientListView
from client.views.client_register import ClientRegisterView
from client.views.home import HomeView
from client.views.login import LoginView
from client.views.logout import logout_user

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('client/list/', ClientListView.as_view()),
                  path('client/register/', ClientRegisterView.as_view()),
                  path('', HomeView.as_view()),
                  path('login/', LoginView.as_view()),
                  path('logout/', logout_user)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
