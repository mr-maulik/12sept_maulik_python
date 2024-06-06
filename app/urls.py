from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
  # path('login/',views.login,name="login"),
  # path('register/',views.register, name="register"),
  path('',views.index, name="index"),
  path('update_appointment_time/', views.update_appointment_time, name='update_appointment_time'),
  path('userlogout/',views.userlogout),
  # path('contact/',views.contact, name='contact'),
  path('data/',views.data, name='data'),
  path('book_appointment/', views.book_appointment, name='book_appointment'),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)