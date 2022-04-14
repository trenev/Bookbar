from django import forms

from bookbar.books.models import Book
from bookbar.common.mixins import BootstrapFormControlMixin


class CreateBookForm(BootstrapFormControlMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Book
        fields = ('category', 'title', 'author', 'annotation', 'cover_image', 'quantity', 'price')
        widgets = {
            'annotation': forms.Textarea(
                attrs={'rows': 4, }
            ),
        }
