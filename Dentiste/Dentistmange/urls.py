from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DentistViewSet, AppointmentViewSet, InvoiceViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'dentists', DentistViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    # ... your other urlpatterns ...
    path('api/', include(router.urls)),
]
