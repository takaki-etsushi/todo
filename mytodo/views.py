
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View # クラスベースビューを継承するのに必要
from .models import Task
from .forms import TaskForm
from django.views.generic import DeleteView
from django.urls import reverse_lazy

# Create your views here.

class IndexView(View):
    def get(self, request):
        # todoリストを取得
        todo_list = Task.objects.all().order_by('complete', 'id')
        context = {"todo_list": todo_list}

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)

class AddView(View):
    def get(self, request):
        form = TaskForm()
        # テンプレートのレンダリング処理
        return render(request, "mytodo/add.html", {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})
    
class EditView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return render(request, "mytodo/edit.html", {'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'mytodo/edit.html', {'form': form, 'task': task})
        
        
class DeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('index')

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')
    

    
# ビュークラスをインスタンス化
index = IndexView.as_view()
add = AddView.as_view()
edit = EditView.as_view()
delete = DeleteView.as_view()
update_task_complete = Update_task_complete.as_view()