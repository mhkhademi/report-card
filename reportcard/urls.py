from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reportcard'

admin.site.site_header = 'مديريت سامانه'
admin.site.site_title = 'مديريت سامانه نمرات'
admin.site.index_title = 'به بخش مديريت سامانه نمرات مدرسه علامه حلي 1 همدان خوش آمديد'

urlpatterns = [
    path('', views.home, name='home'),
    path('bot/', views.bot, name='bot'),
    path('upload/', views.upload, name='upload'),
    path('delete/', views.delete, name='delete'),
    path('getscore/', include('getscore.urls')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),
    path('statistics/', views.statistics),
    path('tuition/', include('pay.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
