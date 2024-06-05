from django.contrib import admin
from django.urls import path, include
from actividades.views import ActividadViewSet
from reviews.views import ProductViewSet, ImageViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from bootstrap import views as bootstrapviews
from uiauth import views as uiviews
from django.conf.urls.i18n import i18n_patterns

router = DefaultRouter()
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'image', ImageViewSet, basename='Image')
router.register(r'actividad', ActividadViewSet, basename='Actividad')



urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('auth/', include('auth.urls')),
    path('api/', include(router.urls)),
    path('personas/', include('personas.urls')),
    path('', bootstrapviews.home, name='index'),
    path('signup/', uiviews.signup, name='signup'),
    path('signin/', uiviews.signin, name='signin'),
    path('signout/', uiviews.signout, name='signout'),
    path('aiopen/', include('aiopen.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
