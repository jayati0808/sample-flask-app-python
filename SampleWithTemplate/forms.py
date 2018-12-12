#!/usr/bin/env python

from wtforms import Form, BooleanField, TextField, PasswordField, validators
from wtforms import StringField
from wtforms.widgets import html_params, HTMLString

class ButtonWidget(object):
    """
    Renders a multi-line text area.
    `rows` and `cols` ought to be passed as keyword args when rendering.
    """
    input_type = 'submit'

    html_params = staticmethod(html_params)

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        if 'value' not in kwargs:
            kwargs['value'] = field._value()

        return HTMLString('<button {params}>{label}</button>'.format(
            params=self.html_params(name=field.name, **kwargs),
            label=field.label.text)
        )

class ButtonField(StringField):
    widget = ButtonWidget()

class TestForm(Form):
    neautral = ButtonField('neutral')
    positive = ButtonField('positive')

class UserForm(Form):
    username = TextField('username', [validators.Length(min=6, max=35)])
    sentiment = TextField('Sentiment', [validators.Length(min=6, max=35)])
