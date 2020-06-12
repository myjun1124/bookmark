from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Bookmark
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# 줄이 너무 길어서 안보일 경우 \를 넣고 다음 줄에 넣으면 됨.
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
# from django.views.generic.edit import UpdateView
# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3     # 한 페이지에 몇 개씩 출력할 것인지 결정

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']       # 어떤 필드를 입력받을지 설정
    success_url = reverse_lazy('list')  # 글쓰기를 완료하고 이동할 페이지
    template_name_suffix = '_create'    #사용할 템플릿의 접미사만 변경하는 설정값

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')