import django_filters
from .models import Ticket

class TicketFilter(django_filters.FilterSet):
    seat_status = django_filters.CharFilter(field_name='seat_id__status', lookup_expr='exact')
    user_id = django_filters.NumberFilter(field_name='user_id', lookup_expr='exact')
    # course_name = django_filters.CharFilter(field_name='course_id__name', lookup_expr='icontains')

    class Meta:
        model = Ticket
        fields = ['seat_status', 'user_id']
