u"""Customized form classes that uses widgets built with Material Components
for the Web.

``MaterialForm`` and ``MaterialModelForm`` modifies ``django.forms.Form`` and
``django.forms.ModelForm`` respectively, and are used to declare Django forms
that will render with Material widgets.

References
----------
`Material Design for the Web <https://material.io/components/web/>`_

"""
# pylint: disable=no-member
# pylint: disable=too-few-public-methods, too-many-ancestors
# pylint: disable=unused-wildcard-import, wildcard-import
from __future__ import absolute_import
from copy import deepcopy
from sys import modules
from django.forms import Form, ModelForm, widgets
from django.forms.utils import ErrorList
from .widgets import MaterialComponent, MaterialMultiWidget
from .widgets import *

__all__ = (u'MaterialForm', u'MaterialModelForm',)

def str_to_object(string):
    u"""Return python object from string.

    Parameters
    ----------
    string : str
        Dot (.) separated location of python object.

    Returns
    -------
    module : python object
        The actual python object.

    Examples
    --------
    >>> text_input = str_to_object('django.forms.widgets.TextInput')

    """
    module = modules[__name__]
    for submodule in string.split(u'.'):
        module = getattr(module, submodule)
    return module


def materialize_field(name, field):
    u"""Convert Django field widgets to use Material widgets.

    Change all default Django widgets in the provided form field to use
    Material Component widgets. Add label and help_text data to the Material
    widget, then return the field.

    Parameters
    ----------
    name : str
        Name of the form field.
    field : class object
        Field object from `django.forms.fields`.

    Returns
    -------
    field : class object
        Field object modified with `material_widgets.widgets`.

    Examples
    --------
    >>> field = materialize_field('username', django.forms.fields.CharField())

    """
    # Convert only widgets.Widget fields to Material widgets
    if (
            isinstance(field.widget, widgets.Widget)
            and not
            isinstance(
                field.widget, (MaterialComponent, MaterialMultiWidget)
                )
        ):
        # match Django widget to Material widget
        material_widget = str_to_object(
            u'Material' + field.widget.__class__.__name__
            )()
        # remove widget.MultiWidget.widgets as it is hardcoded to
        # use django.widgets
        if isinstance(field.widget, widgets.MultiWidget):
            field.widget.__dict__.pop(u'widgets', None)
        # replicate Django widget attributes to Material widget
        for key, value in field.widget.__dict__.items():
            material_widget.__dict__[key] = deepcopy(value)
        field.widget = material_widget
    # set additional fields used in material_widgets.widgets
    field.widget.label = (field.label if field.label is not None
                          else name.replace(u'_', u' ').title())
    field.widget.help_text = field.help_text
    return field


class MaterialErrorList(ErrorList):
    u"""ErrorList formatted with Material Components."""

    def __str__(self):
        return self.as_components()

    def as_components(self):
        u"""Return error_list rendered with Material Components and layout."""
        if not self:
            return u''
        error_group = (
            u'<ul class="mdc-errorlist mdc-list">{}</ul>'
            )
        error_item = (
            u'<li class="mdc-list-item">'
            u'<i class="mdc-list-item__start-detail material-icons"'
            u' aria-hidden="true">error</i>'
            u'<span class="mdc-typography--caption">{}</span></li>'
            )
        error_items = [error_item.format(error) for error in self]
        error_list = error_group.format(u''.join(error_items))
        return error_list


class BaseMaterialForm(object):
    u"""Superclass of `MaterialForm` and `MaterialModelForm` which modifies
    `django.forms.Form` and `django.forms.ModelForm` to use
    `material_widgets.widgets`.

    Parameters
    ----------
    *args
    **kwargs

    Attributes
    ----------
    error_css_class, required_css_class : str
        CSS class attributes added to erroneous fields and required fields
        respectively.
        See `Django Forms API documentation <https://docs.djangoproject.com\
        /en/dev/ref/forms/api/#styling-required-or-erroneous-form-rows>`_.

    """
    error_css_class = u"mdc-error"
    required_css_class = u"mdc-required"

    def __init__(self, *args, **kwargs):
        u"""Change all default `django.forms.widgets` in Form to
        `material_widgets.widgets`. Set self.error_class to use
        `MaterialErrorList`.

        """
        super(BaseMaterialForm, self).__init__(*args, **kwargs)
        self.error_class = MaterialErrorList
        for name, field in self.fields.items():
            field = materialize_field(name, field)

    def as_components(self):
        u"""Return form rendered with Material Components and layout."""
        return self._html_output(
            normal_row=u'<div%(html_class_attr)s>%(field)s</div>',
            error_row=u'%s',
            row_ender=u'</div>',
            help_text_html=u'%s',
            errors_on_separate_row=True,
            )


class MaterialForm(BaseMaterialForm, Form):
    u"""Modified `django.forms.Form` that uses `material_widgets.widgets`.

    Examples
    --------
    Declare your Form fields as usual but subclass `MaterialForm` instead of
    `django.forms.Form`.

    >>> class ExampleForm(MaterialForm):
    >>>     username = forms.CharField(required=True)

    """
    pass


class MaterialModelForm(BaseMaterialForm, ModelForm):
    u"""Modified `django.forms.ModelForm` that uses `material_widgets.widgets`.

    Examples
    --------
    Declare your ModelForm Meta as usual but subclass `MaterialModelForm`
    instead of `django.forms.ModelForm`.

    >>> class ExampleModelForm(MaterialModelForm):
    >>>     class Meta:
    >>>         model = ExampleModel
    >>>         fields = '__all__'

    """
    pass
