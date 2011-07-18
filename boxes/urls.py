from django.conf.urls.defaults import url, patterns


urlpatterns = patterns("boxes.views",
    url(r"^([-\w]+)/create/$", "box_create", name="box_create"),
    url(r"^([-\w]+)/create/([-\w]+)/$", "box_create", name="box_create_lang"),
    url(r"^(\d+)/edit/$", "box_edit", name="box_edit"),
)