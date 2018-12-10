u"""
DJANGO MATERIAL WIDGETS FORMS TEST MODULE
material_widgets/tests/test_forms.py
"""
# pylint: disable=invalid-name, missing-docstring, no-member
# pylint: disable=too-few-public-methods, too-many-ancestors
# pylint: disable=too-many-public-methods

from __future__ import absolute_import
from django import forms
from django.test import TestCase
from .. import widgets
from ..forms import MaterialForm, MaterialModelForm
from .models import MaterialWidgetsTestModel

class MaterialFormTests(TestCase):
    u"""Test cases for material_widgets.forms.MaterialForm.
    Each field's widget should automatically use a Material Component.
    """

    def test_MaterialForm_materializes_BooleanField(self):
        u"""django.forms.widgets.CheckboxInput should be converted to
        material_widgets.widgets.MaterialCheckboxInput.
        """

        class CheckboxInputForm(MaterialForm):
            checkbox_input = forms.BooleanField()

        form = CheckboxInputForm()
        self.assertEqual(
            type(form.fields[u'checkbox_input'].widget),
            widgets.MaterialCheckboxInput,
            )

    def test_MaterialForm_materializes_CharField(self):
        u"""django.forms.widgets.TextInput should be converted to
        material_widgets.widgets.MaterialTextInput.
        """

        class TextInputForm(MaterialForm):
            text_input = forms.CharField()

        form = TextInputForm()
        self.assertEqual(
            type(form.fields[u'text_input'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialForm_materializes_CheckboxSelectMultiple(self):
        u"""django.forms.widgets.CheckboxSelectMultiple should be converted to
        material_widgets.widgets.MaterialCheckboxSelectMultiple.
        """

        class MultipleChoiceForm(MaterialForm):
            checkbox_select_multiple = forms.MultipleChoiceField(
                widget=forms.widgets.CheckboxSelectMultiple(),
                )

        form = MultipleChoiceForm()
        self.assertEqual(
            type(form.fields[u'checkbox_select_multiple'].widget),
            widgets.MaterialCheckboxSelectMultiple,
            )

    def test_MaterialForm_materializes_ChoiceField(self):
        u"""django.forms.widgets.Select should be converted to
        material_widgets.widgets.MaterialSelect.
        """

        class SelectForm(MaterialForm):
            select = forms.ChoiceField()

        form = SelectForm()
        self.assertEqual(
            type(form.fields[u'select'].widget),
            widgets.MaterialSelect,
            )

    def test_MaterialForm_materializes_DateField(self):
        u"""django.forms.widgets.DateInput should be converted to
        material_widgets.widgets.MaterialDateInput.
        """

        class DateInputForm(MaterialForm):
            date_input = forms.DateField()

        form = DateInputForm()
        self.assertEqual(
            type(form.fields[u'date_input'].widget),
            widgets.MaterialDateInput,
            )

    def test_MaterialForm_materializes_DateTimeField(self):
        u"""django.forms.widgets.DateTimeInput should be converted to
        material_widgets.widgets.MaterialDateTimeInput.
        """

        class DateTimeInputForm(MaterialForm):
            date_time_input = forms.DateTimeField()

        form = DateTimeInputForm()
        self.assertEqual(
            type(form.fields[u'date_time_input'].widget),
            widgets.MaterialDateTimeInput,
            )

    def test_MaterialForm_materializes_DecimalField(self):
        u"""django.forms.widgets.NumberInput should be converted to
        material_widgets.widgets.MaterialNumberInput.
        """

        class NumberInputForm(MaterialForm):
            number_input = forms.DecimalField()

        form = NumberInputForm()
        self.assertEqual(
            type(form.fields[u'number_input'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialForm_materializes_EmailField(self):
        u"""django.forms.widgets.EmailInput should be converted to
        material_widgets.widgets.MaterialEmailInput.
        """

        class EmailInputForm(MaterialForm):
            email_input = forms.EmailField()

        form = EmailInputForm()
        self.assertEqual(
            type(form.fields[u'email_input'].widget),
            widgets.MaterialEmailInput,
            )

    def test_MaterialForm_materializes_FileField(self):
        u"""django.forms.widgets.ClearableFileInput should be converted to
        material_widgets.widgets.MaterialClearableFileInput.
        """

        class ClearableFileInputForm(MaterialForm):
            clearable_file_input = forms.FileField()

        form = ClearableFileInputForm()
        self.assertEqual(
            type(form.fields[u'clearable_file_input'].widget),
            widgets.MaterialClearableFileInput,
            )

    def test_MaterialForm_materializes_FileInput(self):
        u"""django.forms.widgets.FileInput should be converted to
        material_widgets.widgets.MaterialFileInput.
        """

        class FileInputForm(MaterialForm):
            file_input = forms.FileField(
                widget=forms.widgets.FileInput(),
                )

        form = FileInputForm()
        self.assertEqual(
            type(form.fields[u'file_input'].widget),
            widgets.MaterialFileInput,
            )

    def test_MaterialForm_materializes_HiddenInput(self):
        u"""django.forms.widgets.HiddenInput should be converted to
        material_widgets.widgets.MaterialHiddenInput.
        """

        class HiddenInputForm(MaterialForm):
            hidden_input = forms.CharField(
                widget=forms.widgets.HiddenInput(),
                )

        form = HiddenInputForm()
        self.assertEqual(
            type(form.fields[u'hidden_input'].widget),
            widgets.MaterialHiddenInput,
            )

    def test_MaterialForm_materializes_IntegerField(self):
        u"""django.forms.widgets.NumberInput should be converted to
        material_widgets.widgets.MaterialNumberInput.
        """

        class NumberInputForm(MaterialForm):
            number_input = forms.IntegerField()

        form = NumberInputForm()
        self.assertEqual(
            type(form.fields[u'number_input'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialForm_materializes_MultipleChoiceField(self):
        u"""django.forms.widgets.SelectMultiple should be converted to
        material_widgets.widgets.MaterialSelectMultiple.
        """

        class SelectMultipleForm(MaterialForm):
            select_multiple = forms.MultipleChoiceField()

        form = SelectMultipleForm()
        self.assertEqual(
            type(form.fields[u'select_multiple'].widget),
            widgets.MaterialSelectMultiple,
            )

    def test_MaterialForm_materializes_MultipleHiddenInput(self):
        u"""django.forms.widgets.MultipleHiddenInput should be converted to
        material_widgets.widgets.MaterialMultipleHiddenInput.
        """

        class MultipleHiddenInputForm(MaterialForm):
            multiple_hidden_input = forms.MultipleChoiceField(
                widget=forms.widgets.MultipleHiddenInput(),
                )

        form = MultipleHiddenInputForm()
        self.assertEqual(
            type(form.fields[u'multiple_hidden_input'].widget),
            widgets.MaterialMultipleHiddenInput,
            )

    def test_MaterialForm_materializes_NullBooleanField(self):
        u"""django.forms.widgets.NullBooleanSelect should be converted to
        material_widgets.widgets.MaterialNullBooleanSelect.
        """

        class NullBooleanSelectForm(MaterialForm):
            null_boolean_select = forms.NullBooleanField()

        form = NullBooleanSelectForm()
        self.assertEqual(
            type(form.fields[u'null_boolean_select'].widget),
            widgets.MaterialNullBooleanSelect,
            )

    def test_MaterialForm_materializes_PasswordInput(self):
        u"""django.forms.widgets.PasswordInput should be converted to
        material_widgets.widgets.MaterialPasswordInput.
        """

        class PasswordInputForm(MaterialForm):
            password_input = forms.CharField(
                widget=forms.widgets.PasswordInput(),
                )

        form = PasswordInputForm()
        self.assertEqual(
            type(form.fields[u'password_input'].widget),
            widgets.MaterialPasswordInput,
            )

    def test_MaterialForm_materializes_RadioSelect(self):
        u"""django.forms.widgets.RadioSelect should be converted to
        material_widgets.widgets.MaterialRadioSelect.
        """

        class RadioSelectForm(MaterialForm):
            radio_select = forms.ChoiceField(
                widget=forms.widgets.RadioSelect(),
                )

        form = RadioSelectForm()
        self.assertEqual(
            type(form.fields[u'radio_select'].widget),
            widgets.MaterialRadioSelect,
            )


    def test_MaterialForm_materializes_SelectDateWidget(self):
        u"""django.forms.widgets.SelectDateWidget should be converted to
        material_widgets.widgets.MaterialSelectDateWidget.
        """

        class SelectDateForm(MaterialForm):
            select_date_widget = forms.DateField(
                widget=forms.widgets.SelectDateWidget(),
                )

        form = SelectDateForm()
        self.assertEqual(
            type(form.fields[u'select_date_widget'].widget),
            widgets.MaterialSelectDateWidget,
            )

    def test_MaterialForm_materializes_SplitDateTimeField(self):
        u"""django.forms.widgets.SplitDateTimeWidget should be converted to
        material_widgets.widgets.MaterialSplitDateTimeWidget.
        """

        class SplitDateTimeInputForm(MaterialForm):
            split_date_time_widget = forms.SplitDateTimeField()

        form = SplitDateTimeInputForm()
        self.assertEqual(
            type(form.fields[u'split_date_time_widget'].widget),
            widgets.MaterialSplitDateTimeWidget,
            )

    def test_MaterialForm_materializes_SplitHiddenDateTimeWidget(self):
        u"""django.forms.widgets.SplitHiddenDateTimeWidget should be converted to
        material_widgets.widgets.MaterialSplitHiddenDateTimeWidget.
        """

        class SplitHiddenDateTimeInputForm(MaterialForm):
            split_hidden_date_time_widget = forms.SplitDateTimeField(
                widget=forms.widgets.SplitHiddenDateTimeWidget(),
                )

        form = SplitHiddenDateTimeInputForm()
        self.assertEqual(
            type(form.fields[u'split_hidden_date_time_widget'].widget),
            widgets.MaterialSplitHiddenDateTimeWidget,
            )

    def test_MaterialForm_materializes_Textarea(self):
        u"""django.forms.widgets.Textarea should be converted to
        material_widgets.widgets.MaterialTextarea.
        """

        class TextareaForm(MaterialForm):
            textarea = forms.CharField(
                widget=forms.widgets.Textarea(),
                )

        form = TextareaForm()
        self.assertEqual(
            type(form.fields[u'textarea'].widget),
            widgets.MaterialTextarea,
            )

    def test_MaterialForm_materializes_TimeField(self):
        u"""django.forms.widgets.TimeInput should be converted to
        material_widgets.widgets.MaterialTimeInput.
        """

        class TimeInputForm(MaterialForm):
            time_input = forms.TimeField()

        form = TimeInputForm()
        self.assertEqual(
            type(form.fields[u'time_input'].widget),
            widgets.MaterialTimeInput,
            )

    def test_MaterialForm_materializes_URLField(self):
        u"""django.forms.widgets.URLInput should be converted to
        material_widgets.widgets.MaterialURLInput.
        """

        class URLInputForm(MaterialForm):
            url_input = forms.URLField()

        form = URLInputForm()
        self.assertEqual(
            type(form.fields[u'url_input'].widget),
            widgets.MaterialURLInput,
            )


class MaterialModelFormMaterializeTests(TestCase):
    u"""Test cases for material_widgets.forms.MaterialModelForm.
    Each field's widget should automatically use a Material Component.
    """

    @classmethod
    def setUpClass(cls):
        class TestModelForm(MaterialModelForm):
            u"""Test ModelForm with Material Component fields"""

            class Meta(object):
                u"""Meta settings for TestModelForm"""
                model = MaterialWidgetsTestModel
                fields = u'__all__'

        cls._form = TestModelForm()

    @classmethod
    def tearDownClass(cls):
        del cls._form

    def test_MaterialModelForm_materializes_BigIntegerField(self):
        u"""django.models.BigIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'big_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_BooleanField(self):
        u"""django.models.BooleanField should use
        material_widgets.widgets.MaterialCheckboxInput.
        """
        self.assertEqual(
            type(self._form.fields[u'boolean_field'].widget),
            widgets.MaterialCheckboxInput,
            )

    def test_MaterialModelForm_materializes_CharField(self):
        u"""django.models.CharField should use
        material_widgets.widgets.MaterialTextInput.
        """
        self.assertEqual(
            type(self._form.fields[u'char_field'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialModelForm_materializes_DateField(self):
        u"""django.models.DateField should use
        material_widgets.widgets.MaterialDateInput.
        """
        self.assertEqual(
            type(self._form.fields[u'date_field'].widget),
            widgets.MaterialDateInput,
            )

    def test_MaterialModelForm_materializes_DateTimeField(self):
        u"""django.models.DateTimeField should use
        material_widgets.widgets.MaterialDateTimeInput.
        """
        self.assertEqual(
            type(self._form.fields[u'date_time_field'].widget),
            widgets.MaterialDateTimeInput,
            )

    def test_MaterialModelForm_materializes_DecimalField(self):
        u"""django.models.DecimalField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'decimal_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_EmailField(self):
        u"""django.models.EmailField should use
        material_widgets.widgets.MaterialEmailInput.
        """
        self.assertEqual(
            type(self._form.fields[u'email_field'].widget),
            widgets.MaterialEmailInput,
            )

    def test_MaterialModelForm_materializes_FileField(self):
        u"""django.models.FileField should use
        material_widgets.widgets.MaterialClearableFileInput.
        """
        self.assertEqual(
            type(self._form.fields[u'file_field'].widget),
            widgets.MaterialClearableFileInput,
            )

    def test_MaterialModelForm_materializes_FilePathField(self):
        u"""django.models.FilePathField should use
        material_widgets.widgets.MaterialSelect.
        """
        self.assertEqual(
            type(self._form.fields[u'file_path_field'].widget),
            widgets.MaterialSelect,
            )

    def test_MaterialModelForm_materializes_FloatField(self):
        u"""django.models.FloatField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'float_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_ForeignKey(self):
        u"""django.models.ForeignKey should use
        material_widgets.widgets.MaterialSelect.
        """
        self.assertEqual(
            type(self._form.fields[u'foreign_key'].widget),
            widgets.MaterialSelect,
            )

    def test_MaterialModelForm_materializes_IntegerField(self):
        u"""django.models.IntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_GenericIPAddressField(self):
        u"""django.models.GenericIPAddressField should use
        material_widgets.widgets.MaterialTextInput.
        """
        self.assertEqual(
            type(self._form.fields[u'generic_ip_address_field'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialModelForm_materializes_ManyToManyField(self):
        u"""django.models.ManyToManyField should use
        material_widgets.widgets.MaterialSelectMultiple.
        """
        self.assertEqual(
            type(self._form.fields[u'many_to_many_field'].widget),
            widgets.MaterialSelectMultiple,
            )

    def test_MaterialModelForm_materializes_NullBooleanField(self):
        u"""django.models.NullBooleanField should use
        material_widgets.widgets.MaterialNullBooleanSelect.
        """
        self.assertEqual(
            type(self._form.fields[u'null_boolean_field'].widget),
            widgets.MaterialNullBooleanSelect,
            )

    def test_MaterialModelForm_materializes_PositiveIntegerField(self):
        u"""django.models.PositiveIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'positive_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_PositiveSmallIntegerField(self):
        u"""django.models.PositiveSmallIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'positive_small_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_SlugField(self):
        u"""django.models.SlugField should use
        material_widgets.widgets.MaterialTextInput.
        """
        self.assertEqual(
            type(self._form.fields[u'slug_field'].widget),
            widgets.MaterialTextInput,
            )

    def test_MaterialModelForm_materializes_SmallIntegerField(self):
        u"""django.models.SmallIntegerField should use
        material_widgets.widgets.MaterialNumberInput.
        """
        self.assertEqual(
            type(self._form.fields[u'small_integer_field'].widget),
            widgets.MaterialNumberInput,
            )

    def test_MaterialModelForm_materializes_TextField(self):
        u"""django.models.TextField should use
        material_widgets.widgets.MaterialTextarea.
        """
        self.assertEqual(
            type(self._form.fields[u'text_field'].widget),
            widgets.MaterialTextarea,
            )

    def test_MaterialModelForm_materializes_TimeField(self):
        u"""django.models.TimeField should use
        material_widgets.widgets.MaterialTimeInput.
        """
        self.assertEqual(
            type(self._form.fields[u'time_field'].widget),
            widgets.MaterialTimeInput,
            )

    def test_MaterialModelForm_materializes_URLField(self):
        u"""django.models.URLField should use
        material_widgets.widgets.MaterialURLInput.
        """
        self.assertEqual(
            type(self._form.fields[u'url_field'].widget),
            widgets.MaterialURLInput,
            )


class MaterialModelFormMethodTests(TestCase):
    u"""Test cases for material_widgets.forms.MaterialModelForm.
    Inherited ModelForm methods should process form data.
    """

    @classmethod
    def setUpClass(cls):
        class TestModelForm(MaterialModelForm):
            u"""Test ModelForm with Material Component fields"""

            class Meta(object):
                u"""Meta settings for TestModelForm"""
                model = MaterialWidgetsTestModel
                fields = u'__all__'

        cls._form = TestModelForm

    @classmethod
    def tearDownClass(cls):
        del cls._form

    def test_MaterialModelForm_is_valid_should_validate_correct_data(self):
        u"""MaterialModelForm.is_valid() should return True with valid data."""
        data = {u'integer_field': 1}
        form = self._form(data=data)
        self.assertTrue(form.is_valid())

    def test_MaterialModelForm_is_valid_should_invalidate_wrong_data(self):
        u"""MaterialModelForm.is_valid() should return False with invalid data."""
        data = {u'positive_integer_field': -1}
        form = self._form(data=data)
        self.assertFalse(form.is_valid())

    def test_MaterialModelForm_save_valid_data_should_create_a_new_entry(self):
        u"""MaterialModelForm.save() should create a new database entry with
        valid form data.
        """
        data = {u'url_field': u'https://github.com/ooknosi'}
        form = self._form(data=data)
        self.assertEqual(MaterialWidgetsTestModel.objects.count(), 0)
        form.save()
        self.assertEqual(MaterialWidgetsTestModel.objects.count(), 1)
        self.assertEqual(
            MaterialWidgetsTestModel.objects.get().url_field,
            u'https://github.com/ooknosi'
            )

    def test_MaterialModelForm_save_invalid_data_should_not_create_a_new_entry(self):
        u"""MaterialModelForm.save() should not create a new database entry with
        invalid form data.
        """
        data = {u'url_field': u'ooknosi'}
        form = self._form(data=data)
        self.assertRaises(ValueError, form.save)
        self.assertEqual(MaterialWidgetsTestModel.objects.count(), 0)
