from django.urls import path
from . import views

app_name='dungeon'

urlpatterns = [
    path('',views.main),
    path('main/',views.main, name='main'),
    path('start/ektltlwkrgoqhwkrestarts/',views.start,name='start'),
    path('stage1/aodlfaodlfdlwmfrjqrp/',views.stage1, name='stage1'),
    path('stage2/rkatkgksmsakdmadmfh/',views.stage2,name='stage2'),
    path('stage3/godqhrgksdlstoddmftkfwk/',views.stage3,name='stage3'),
    path('stage4/dnflsmsgkftndlTdj/',views.stage4,name='stage4'),
    path('stage5/qnahsladldnflfskgdmtlfEo/',views.stage5,name='stage5'),
    path('stage6/tptkddmfdjedmswnfdkfdkTdj/',views.stage6,name='stage6'),
    path('last-stage/tnrhgktuTtmqslek/',views.last_stage,name='last_stage'),
    path('treasure/wjdakfRmxdlek/',views.treasure,name='treasure'),
]
