from django import forms

from products.models import Category, Product


class FilterForm(forms.Form):
    """Filter form class."""

    search_field = forms.CharField(
        label='Search:',
        widget=forms.TextInput(attrs={'placeholder': 'Enter pattern'}),
        max_length=128,
        required=False
    )
    min_price = forms.FloatField(
        label='Min Price:',
        widget=forms.TextInput(attrs={'placeholder': 'Enter price in $'}),
        min_value=1.0,
        required=False,
    )
    max_price = forms.FloatField(
        label='Max Price:',
        widget=forms.TextInput(attrs={'placeholder': 'Enter price in $'}),
        min_value=1.0,
        required=False,
    )
    sort_by = forms.ChoiceField(
        choices=[
            ('rating', 'Top Rated'),
            ('-created_at', 'Newest'),
            ('price', 'Price Low to High'),
            ('-price', 'Price High to Low'),
        ],
        label="Order by:",
        required=False,
    )


class FilterFormDetailed(FilterForm):
    """Detailed filter form class."""

    category = forms.ChoiceField(
        choices=[('', 'Select')] + [
            (
                category.slug,
                category.name,
            ) for category in Category.objects.all()
        ],
        label="Category:",
        required=False,
    )

    producer = forms.ChoiceField(
        choices=[('', 'Select')] + [
            (producer, producer) for producer in Product.objects.values_list(
                'producer',
                flat=True).distinct()
        ],
        label="Producer:",
        required=False,
    )
