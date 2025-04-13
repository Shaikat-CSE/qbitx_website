from django import forms
from .models import ContactMessage, ServiceRequest, Newsletter
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'service_interest', 'company', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'service_interest': forms.Select(choices=[
                ('', 'Select Service Interest (optional)'),
                ('website', 'Website Development'),
                ('ecommerce', 'E-Commerce Solutions'),
                ('mobile_app', 'Mobile App Development'),
                ('erp', 'ERP Software'),
                ('digital_marketing', 'Digital Marketing'),
                ('other', 'Other Services'),
            ]),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'contact-form'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('email', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6'),
                Column('company', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('subject', css_class='form-group col-md-6'),
                Column('service_interest', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'message',
            Submit('submit', 'Send Message', css_class='btn btn-primary btn-lg mt-4')
        )
        
        # Add placeholders and required labels
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Your Phone (optional)'
        self.fields['company'].widget.attrs['placeholder'] = 'Your Company (optional)'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message'

class ServiceRequestForm(forms.ModelForm):
    budget_range = forms.ChoiceField(
        choices=[
            ('', 'Select Budget Range (optional)'),
            ('under_5k', 'Under $5,000'),
            ('5k_10k', '$5,000 - $10,000'),
            ('10k_25k', '$10,000 - $25,000'),
            ('25k_50k', '$25,000 - $50,000'),
            ('50k_plus', 'Over $50,000'),
            ('not_sure', 'Not Sure'),
        ],
        required=False
    )
    
    timeline = forms.ChoiceField(
        choices=[
            ('', 'Select Timeline (optional)'),
            ('urgent', 'Urgent (ASAP)'),
            ('1_month', 'Within 1 Month'),
            ('1_3_months', '1-3 Months'),
            ('3_6_months', '3-6 Months'),
            ('flexible', 'Flexible'),
        ],
        required=False
    )
    
    how_heard_about_us = forms.ChoiceField(
        choices=[
            ('', 'How did you hear about us? (optional)'),
            ('search_engine', 'Search Engine'),
            ('social_media', 'Social Media'),
            ('referral', 'Referral'),
            ('advertisement', 'Advertisement'),
            ('other', 'Other'),
        ],
        required=False
    )
    
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'phone', 'company', 'service_type', 
                  'budget_range', 'project_description', 'timeline', 'how_heard_about_us']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 5}),
            'service_type': forms.Select(choices=[
                ('', 'Select Service Type'),
                ('website', 'Website Development'),
                ('ecommerce', 'E-Commerce Solutions'),
                ('mobile_app', 'Mobile App Development'),
                ('erp', 'ERP Software'),
                ('digital_marketing', 'Digital Marketing'),
                ('other', 'Other Services'),
            ]),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'service-request-form'
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-6'),
                Column('email', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('phone', css_class='form-group col-md-6'),
                Column('company', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('service_type', css_class='form-group col-md-6'),
                Column('budget_range', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            Row(
                Column('timeline', css_class='form-group col-md-6'),
                Column('how_heard_about_us', css_class='form-group col-md-6'),
                css_class='form-row'
            ),
            'project_description',
            Submit('submit', 'Request Service', css_class='btn btn-primary btn-lg mt-4')
        )
        
        # Add placeholders and required labels
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email'
        self.fields['phone'].widget.attrs['placeholder'] = 'Your Phone Number'
        self.fields['company'].widget.attrs['placeholder'] = 'Your Company (optional)'
        self.fields['project_description'].widget.attrs['placeholder'] = 'Please describe your project or requirements'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name (optional)'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-5'),
                Column('name', css_class='form-group col-md-5'),
                Column(Submit('submit', 'Subscribe', css_class='btn btn-primary btn-block'), 
                       css_class='form-group col-md-2'),
                css_class='form-row'
            )
        )
