from django.urls import path
from api.views import QuoteView, QuoteDetailView

urlpatterns = [
    path('quotes', QuoteView.as_view(), name='quotes'),
    path('quotes/<id>', QuoteDetailView.as_view(), name='quotes_details')
]