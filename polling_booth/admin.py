from django.contrib import admin
from .models import Question,Choice
# Register your models here.

# admin.site.register(Question)
# admin.site.register(Choice)

#this way you can customize how the Question admin form
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['ques_text']}),
    #     ('Date information', {'fields': ['publish_date']}),
    # ]
    list_display = ('ques_text', 'publish_date')
    list_filter = ['publish_date']
    search_fields = ['ques_text']
    inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)