from django.urls import path, include
from markdownx import urls as markdownx

# from . import views

from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    # path('', views.home, name="home")

    path('', HomeView.as_view(), name="home"),

    # pk: primary key
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),

    path('add_post/', AddPostView.as_view(), name='add_post'),

    # path('math_latex/', LatexView.as_view(), name='latex_view'),

    # path('markdownx/', include('markdownx.urls')),
]