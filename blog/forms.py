from django import forms

class ArticleForm(forms.Form):
    multiple_check_box_data = [
        ('one', 'item 1'),
        ('two', 'item 2'),
        ('three', 'item 3'),
        ('four', 'item 4'),
        ('five', 'item 5'),
    ]
    pulldown_data = [
        ('1', 'choice 1'),
        ('2', 'choice 2'),
        ('3', 'choice 3'),
    ]
    radio_data = [
        ('data 1', 'radio 1'),
        ('data 2', 'radio 2'),
        ('data 3', 'radio 3'),
    ]
    title = forms.CharField(label='Title', max_length=255)
    content = forms.CharField(label='Content', widget=forms.Textarea())
    check_box = forms.BooleanField(label='Check', required=False)
    multiple_check_box = forms.MultipleChoiceField(
        label='MultipleCheck',
        choices=multiple_check_box_data,
        widget=forms.CheckboxSelectMultiple()
    )
    pulldown = forms.ChoiceField(
        label='Pulldown',
        choices=pulldown_data
    )
    radio = forms.ChoiceField(
        label='Radio',
        choices=radio_data,
        widget=forms.RadioSelect()
    )