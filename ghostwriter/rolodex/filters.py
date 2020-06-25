"""This contains all of the model filters for the Ghostwriter application."""

import django_filters
from django import forms

from .models import Client


class ClientFilter(django_filters.FilterSet):
    """Filter used to search the `Client` model."""

    name = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Client
        fields = ["name"]


class ProjectFilter(django_filters.FilterSet):
    """Filter used to search the `Project` model."""

    start_date = django_filters.DateFilter(
        lookup_expr=("gt"),
        label="Precise Start Date",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    end_date = django_filters.DateFilter(
        lookup_expr=("lt"),
        label="Precise End Date",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    start_date_range = django_filters.DateRangeFilter(
        field_name="start_date", label="Start Date Window"
    )
    end_date_range = django_filters.DateRangeFilter(
        field_name="end_date", label="End Date Windows"
    )

    STATUS_CHOICES = (
        (0, "All Projects"),
        (1, "Completed"),
    )

    complete = django_filters.ChoiceFilter(
        choices=STATUS_CHOICES, empty_label=None, label="Project status"
    )

    class Meta:
        model = Client
        fields = [
            "complete",
        ]
