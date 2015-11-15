from django.contrib import admin
from search.models import Page, Expression

class ExpressionInline(admin.TabularInline):
      model = Expression
      extra = 3

class PageAdmin(admin.ModelAdmin):
      fieldsets = [
        (None,               {'fields': ['title','url','datetime']}),

      ]
      inlines = [ExpressionInline]

     


admin.site.register(Page,PageAdmin)


