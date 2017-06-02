from django.conf.urls import url

import blog.views as views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
