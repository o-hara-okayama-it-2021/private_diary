from django.contrib import admin

from .models import Blog

# 管理サイトにブログモデルを登録
admin.site.register(Blog)
