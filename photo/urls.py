from django.urls import path
from . import views

#URLパターンを逆引きできるように名前を付ける
app_name = 'photo'

#URLパターンを登録する
urlpatterns = [
    #photoアプリへのアクセスはviewsモジュールのIndexViewを実行
    path('', views.IndexView.as_view(), name='index'),
    
    #写真投稿ページへのアクセスはviewsモジュールのCreatePhotoViewを実行
    path('post/', views.CreatePhotoView.as_view(), name='post'),
    
    #投稿完了ぺーじへのアクセスはviesモジュールｎPostSuccessViewを実行
    path('post_done/',views.PostSuccessView.as_view(),name='post_done'),
    
    #カテゴリ一覧ページ
    path('photos/<int:category>',views.CategoryView.as_view(),name='photos_cat'),
    
    #ユーザーの投稿一覧ページ
    path('user-list/<int:user>',views.UserView.as_view(),name='user_list'),
    
    #詳細ページ
    path('photo-detail/<int:pk>',views.DetailView.as_view(),name= 'photo_detail'),
    
    #マイページ
    path('mypage/',views.MypageView.as_view(),name='mypage'),
    
    path('photo/<int:pk>/delete/',views.PhotoDeleteView.as_view(),name= 'photo_delete'),
]