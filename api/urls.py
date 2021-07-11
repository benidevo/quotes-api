from django.urls import path
from api.views import QuoteView

urlpatterns = [
    path('quotes', QuoteView.as_view(), name='quotes'),
]