from django.conf.urls import url
from filed.views import file_element, file_collection

urlpatterns = [
    url('^(?P<audioFileType>\w+)/?$', file_collection, name='collection'),
    url('^(?P<audioFileType>\w+)/(?P<audioFileID>\w+)/?$', file_element, name='element')
]