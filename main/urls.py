from django.urls import path
from main.views import show_main, create_product, delete_product, edit_product
from main.views import show_xml, show_json
from main.views import show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import increment_amount, decrement_amount

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('delete_product/<int:id>/', delete_product, name='delete_product'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increment_amount/<int:id>/', increment_amount, name='increment_amount'),
    path('decrement_amount/<int:id>/', decrement_amount, name='decrement_amount'),
]