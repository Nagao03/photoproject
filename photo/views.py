from django.shortcuts import render
#django.views.genericからTemplateをインポート
from django.views.generic import TemplateView, ListView
#django.views.genericからCreateViewをインポート
from django.views.generic import CreateView
#django.urlsからreverse_lazyをインポート
from django.urls import reverse_lazy
#formsモジュールからPhotoPostFormをインポート
from .forms import PhotoPostForm
#method_decoratorをインポート
from django.utils.decorators import method_decorator
#login_requiredをインポート
from django.contrib.auth.decorators import login_required
#modelsモジュールからモデルPhotoPostをインポート
from .models import PhotoPost
#django.views.genericからDetailViewをインポート
from django.views.generic import DetailView
#django.views.genericからDeleteViewをインポート
from django.views.generic import DeleteView
    

class IndexView(ListView):
    #index.htmlをレタリングする
    template_name ='index.html'
    queryset = PhotoPost.objects.order_by('-posted_at')
    paginate_by = 9

@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    #forms.pyPhotoPostFormをフォームクラスとして登録
    form_class = PhotoPostForm
    #レタリングするテンプレート
    template_name = "post_photo.html"
    #フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('photo:post_done')
    
    def form_valid(self, form):
        #commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        #投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        #投稿データをデータベースに登録
        postdata.save()
        #戻り値はスーパークラスのform_valild()の戻り値(HttpResponseRedirect)
        return super().form_valid(form) 

class PostSuccessView(TemplateView):
    #index.htmlをレタリングする
    template_name = 'post_success.html'       
    
class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9
    
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories

class UserView(ListView):
    template_name = 'index.html'
    paginate_by = 9
    
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = PhotoPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list

class DetailView(DetailView):
    template_name = 'detail.html'
    model = PhotoPost   

class MypageView(ListView):
    template_name ='mypage.html'
    paginate = 9
    
    def get_queryset(self):
        queryset = PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset

class PhotoDeleteView(DeleteView):
    model = PhotoPost
    template_name ='photo_delete.html'
    success_url = reverse_lazy('photo:mypage')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)    
        