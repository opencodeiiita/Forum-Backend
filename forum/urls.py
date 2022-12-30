from django.urls import include, path
from rest_framework import routers
from forum import views
from accounts.views import logout_view
router = routers.DefaultRouter()
router.register(r'answers', views.AnswerView)
router.register(r'questions', views.QuestionView)   
router.register(r'logout',logout_view)
router.register(r'user_questions',views.ListQuestionByUserView)

urlpatterns = [
    path('', include(router.urls)),
]