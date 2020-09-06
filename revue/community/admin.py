from django.contrib import admin
from .models import Review, Comment, Recomment, ShortReview, Report
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content', )

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','content','created_at',)

class RecommentAdmin(admin.ModelAdmin):
    list_display = ('id','content','created_at',)

class ShortReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'content',)

class ReportAdmin(admin.ModelAdmin):
    list_display  =('id', 'r_id', 'sort', 'simple_reason', 'detail_reason', 'reported_at')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Recomment, RecommentAdmin)
admin.site.register(ShortReview, ShortReviewAdmin)
admin.site.register(Report, ReportAdmin)