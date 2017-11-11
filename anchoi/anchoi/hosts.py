from django.conf import settings

from django_hosts import host, patterns


host_patterns = patterns(
    '',
    host(r'(|www)', settings.ROOT_URLCONF, name='normal'),
    host(r'text', 'text.urls', name='text'),
)
