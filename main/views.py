from django.shortcuts import render

from django.views.generic import TemplateView

from user.models import User
from news.models import News
from post.models import Post
from gallery.models import Gallery


class IndexView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()[:5]
        context["galleries1"] = Gallery.objects.all()[:3]
        context["galleries2"] = Gallery.objects.all()[3:6]

        news_list = News.objects.all()[:5]
        for idx, news in enumerate(news_list):
            length = len(news.content)
            tmp = length
            for i in range(80, len(news.content)):
                if news.content[i] == " ":
                    tmp = i
                    break
            news_list[idx].content = news.content[:tmp]

            if tmp < length:
                news_list[idx].content += " ..."
            print(news_list[idx].content)

        context["news_list"] = news_list
        return context
