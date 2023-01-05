from django import forms
from .models import Board, Comment


class BoardForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._widget_update()

    class Meta:
        model = Board
        fields = ["title", "content"]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': "제목을 입력해주세요."
                }
            )
        }

    def _widget_update(self):
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'board']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '댓글입력',
                'rows': 3
            }),
            'board': forms.HiddenInput()
        }
