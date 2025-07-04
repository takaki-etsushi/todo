# mytodo/urls.py
from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index,name="index"),
    path("add/", mytodo.add,name="add"), # あとで使う
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
    path("edit/<int:pk>/", mytodo.edit, name="edit"),  # 編集ページのURLを追加
    path("delete/<int:pk>/", mytodo.delete, name="delete"), # 削除用のURLを追加
]