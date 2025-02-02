from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang = self.request.query_params.get('lang', 'en')
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        faqs = FAQ.objects.all()
        cache.set(cache_key, faqs, timeout=3600)  # Cache for 1 hour
        return faqs
