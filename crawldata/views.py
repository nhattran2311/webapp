from bs4 import BeautifulSoup
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.contrib import messages
from config.settings.base import API_URL, API_USER, API_PASSWORD
data_craw = None

@login_required
def craw_data_viblo(request):
    if request.method == "POST":
        try:
            website_link = request.POST.get('web_link', None)

            #requests
            url = website_link #url
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}#headers
            source=requests.get(url, headers=headers).text # url source
            #beautifulsoup
            html = BeautifulSoup(source, 'html.parser')
            h1_val = html.h1.string #h1
            articles = html.find('article').find("div", {'class': 'article-content__body'}).find_all()
            Uniques = set()
            paragraphs = []
            for paragraph in articles:
                # if paragraph not in Uniques:
                #     Uniques.add(paragraph.prettify())
                paragraphs.append(paragraph.prettify())
                content = "".join(paragraphs)
            global data_craw
            data_craw = {
                'title':h1_val,
                'content':content,
                'author': 1,
            }
            return render(request, 'crawldata/craw_data_viblo.html', data_craw )
        except:
            messages.error(request,f"Please just insert viblo article url!!! \n \
            Example: https://viblo.asia/p/su-dung-ai-danh-gia-san-pham-tren-lazadatiki-dua-tren-comment-aWj53b9ol6m")
            return render(request, 'crawldata/craw_data_viblo.html')
    return render(request, 'crawldata/craw_data_viblo.html')

@login_required
def create_article(request):
    if request.method == 'POST':
        r = requests.post(API_URL, auth=(API_USER, API_PASSWORD), data=data_craw)
        if r.status_code == 201:
            messages.success(request, f'Your data has been updated!')
            data_craw = None
            return render(request, 'crawldata/craw_data_viblo.html')
        else:
            messages.error(request,f'Wrong data format - status code : {r.status_code}',)
            return render(request, 'crawldata/craw_data_viblo.html')
    else:
        return render(request, 'crawldata/craw_data_viblo.html')
