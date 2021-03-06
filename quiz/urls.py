from django.urls import path
from . views import ExamListView, ResultPageListView, StartPage, ExamCalculationView

app_name = 'quiz'

urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('quiz/',
         ExamListView.as_view(), name='question_page'),
    path('results/', ResultPageListView.as_view(), name='result_page'),
    path('calculate/', ExamCalculationView.as_view(), name='calculation_page'),
]
