from django.contrib import admin
from .models import Link,Sidebar
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title','href','status','weight','created_time')
    fields = ('title','href','weight','status')
    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        return super(LinkAdmin,self).save_model(request,obj,form,change)

@admin.register(Sidebar)
class Sidebar(admin.ModelAdmin):
    list_display = ('title','display_type','content','status','owner','created_time')
    fields = ('title','display_type','content','status','owner')

    def save_model(self,request,obj,form,change):
        obj.owner = request.user
        super(Sidebar,self).save_model(request,obj,form,change)