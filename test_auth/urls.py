from rest_framework.routers import SimpleRouter
from .views import TestView, AdminView, StaffView



routers = SimpleRouter()
routers.register('test', TestView, base_name="test_view")
routers.register('admin_view', AdminView, base_name="admin_view")
routers.register('staff', StaffView, base_name="staff_view")

app_name = "test_auth"