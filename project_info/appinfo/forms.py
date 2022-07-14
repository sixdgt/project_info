from django.forms import PasswordInput, forms

from appinfo.models import StudentDetail

class StudentDetailForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput)
    class Meta:
        # fields = "__all__" - to load all fields
        fields = ("first_name", "middle_name", "last_name", "contact", "email", "password") # selective fields
        model = StudentDetail

class StudentLoginForm(forms.ModelForm):
    class Meta:
        fields = ("email", "password")
        model = StudentDetail

# Todo list
# 1. git setup
# 2. create project
# 3. create app
# 4. set database
# 5. make models and migrations
# 6. do migrate
# 7. make views
# 8. make templates and render
# 9. organize layouts
# 10. make urls
# 11. make forms