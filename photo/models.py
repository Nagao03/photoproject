from django.db import models
#accountsアプリのmodelsモジュールからCustomUserをインポート
from accounts.models import CustomUser

class Category(models.Model):
    '''投稿する写真のカテゴリを管理するモデル
    '''
    #カテゴリ名のフィールド
    title = models.CharField(verbose_name='カテゴリ',max_length=20)
    
    def __str__(self):
        return self.title
    
class PhotoPost(models.Model):
    '''投稿されたデータを管理するモデル
    '''
    user = models.ForeignKey(
        CustomUser,
        verbose_name='ユーザー', #フィールドのタイトル
        on_delete=models.CASCADE
        )
    category = models.ForeignKey(
        Category,
        verbose_name='カテゴリ', #フィールドのタイトル
        on_delete=models.PROTECT
        )
    
    #タイトル用のフィールド
    title = models.CharField(
        verbose_name='タイトル', #フィールドのタイトル
        max_length=200
        )
    
    #コメント用のフィールド
    comment = models.TextField(
        verbose_name='コメント', #フィールドのタイトル
        )
    
    #イメージのフィールド1    
    image1 = models.ImageField(
        verbose_name='イメージ1', #フィールドのタイトル
        upload_to = 'photos'
        )
    
    #イメージのフィールド2
    image2 = models.ImageField(
        verbose_name='イメージ2', #フィールドのタイトル
        upload_to = 'photos',
        blank=True,
        null=True
        )
    
    #投稿日時のフィールド
    posted_at = models.DateTimeField(
        verbose_name='投稿日時', #フィールドのタイトル
        auto_now_add=True
        )
    
    def __str__(self):
        return self.title
    
# Create your models here.
