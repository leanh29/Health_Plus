from django.contrib import admin
from .models import ProfileModel
#from django.contrib.auth.models import User
#from django_mail_admin import mail
# Register your models here.

#admin.site.register(ProfileModel)

# def send_mail(modeladmin, request):
#     send_mail.short_description = "Send mail notify account created"

class SendMailAdmin(admin.ModelAdmin):
    actions = ['send_EMAIL']

    def send_EMAIL(self, request, queryset):
        from django.core.mail import send_mail
        for i in queryset:
            if i.user.email:
                send_mail('New Account for doctor', 'Your account has been created with password "Doctorpurple". Login here http://127.0.0.1:8000/login/ and change your password to continue!', 'leanh.ltha@gmail.com',[i.user.email], fail_silently=False)
            else:
                self.message_user(request, "Mail sent successfully ") 
    send_EMAIL.short_description = "Send an email to selected users"

admin.site.register(ProfileModel,SendMailAdmin)