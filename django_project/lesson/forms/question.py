# coding=utf-8
"""Question form."""

from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Layout,
    Fieldset,
    Field,
    Submit,
    HTML,
)

from modeltranslation.forms import TranslationModelForm
from lesson.models.worksheet_question import WorksheetQuestion


class QuestionForm(TranslationModelForm):
    """Form for creating Question."""

    class Meta:
        model = WorksheetQuestion
        fields = (
            'question',
            'question_image',
        )

    def __init__(self, *args, **kwargs):
        self.worksheet = kwargs.pop('worksheet')
        self.helper = FormHelper()
        layout = Layout(
            Fieldset(
                _('Worksheet {}: question details').format(self.worksheet),
                Field('question', css_class='form_control'),
                HTML(
                    '{% if form.question_image.value %}'
                    '<img class="img-responsive" '
                    'src="{{ MEDIA_URL }}{{ form.question_image.value }}">'
                    '{% endif %}', ),
                css_id='project-form'
            )
        )

        self.helper.layout = layout
        self.helper.html5_required = False

        super(QuestionForm, self).__init__(*args, **kwargs)

        self.helper.add_input(Submit('submit', 'Submit', css_class='button is-success pt-2 mt-5'))

    def save(self, commit=True):
        instance = super(QuestionForm, self).save(commit=False)
        instance.worksheet = self.worksheet
        instance.save()
        return instance
