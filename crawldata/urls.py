from django.urls import path,include
from . import views
from crawldata.views import  (craw_data_viblo, create_article)

urlpatterns = [
    path('craw_data_viblo/', craw_data_viblo, name="craw_data_viblo"),
    path('craw_data_viblo/success', create_article, name="create_article"),
]