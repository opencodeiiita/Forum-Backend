from django.urls import include, path
from rest_framework import routers
from forum import views

router = routers.DefaultRouter()
router.register(r'answers', views.AnswerView)
router.register(r'questions', views.QuestionView)   

urlpatterns = [
    path('', include(router.urls)),
    path('answers/', ListAnswerView.as_view())      #for list answer view
]