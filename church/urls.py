from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('about/', include('about.urls')),
    path('admin/', admin.site.urls),
    # path('blog/', include('blog.urls')),
    path('contacts/', include('contacts.urls')),
    path('events/', include('events.urls')),
    # path('media/', include('media.urls')),
    path('ministries/', include('ministries.urls')),
    path('sermons/', include('sermons.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

