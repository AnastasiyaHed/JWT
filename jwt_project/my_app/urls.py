# from django.urls import path
# from .views import ExampleView
#
# urlpatterns = [
#     path('example/', ExampleView.as_view(), name='example'),
#
# ]


from django.urls import path
from .views import HelloView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
]