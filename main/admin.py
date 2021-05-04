from django.contrib import admin
from .models import Category, Post, PostComment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_uz', 'name_ru']
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


# class PostAdmin(admin.ModelAdmin):
#     class Meta:
#         model = Post
#
#
# admin.site.register(Post, PostAdmin)
#
#
# class PostCommentAdmin(admin.ModelAdmin):
#     class Meta:
#         model = PostComment
#
#
# admin.site.register(PostComment, PostCommentAdmin)