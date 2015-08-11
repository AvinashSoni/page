import random

from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, TemplateView, FormView
from .models import MCQuestion
from quiz.models import Question, SubCategory, Category, Goal, Course
from django.shortcuts import render
#from .forms import QuestionForm, EssayForm
#from .models import Quiz, Category, Progress, Sitting, Question
#from essay.models import Essay_Question

class Myview(ListView):
	model = Category
	#queryset = Post.objects.filter(category__category = 'Tech')
	template_name = 'quiz/question_list.html'

class Myview0(ListView):
	model = Course
	template_name = 'quiz/course_list.html'
	#def get_queryset(self):
		#self.Category = get_object_or_404(Category, category=self.kwargs.get('category'))
		#return SubCategory.objects.filter(category=self.Category)

class Myview1(ListView):
	model = Category
	template_name = 'quiz/subcategory_list.html'
	def get_queryset(self):
		self.Course = get_object_or_404(Course, course=self.kwargs.get('course'))
		return Category.objects.filter(course=self.Course)

#class Myview7(ListView):
class Myview2(ListView):
	model = SubCategory
	template_name = 'quiz/mathematics_question_list.html'
	def get_queryset(self):
		self.Category = get_object_or_404(Category, category=self.kwargs.get('category'))
		return SubCategory.objects.filter(category=self.Category)

class Myview3(ListView):
	model = Goal
	template_name = 'quiz/mathematics_question_list1.html'
	def get_queryset(self):
		self.SubCategory = get_object_or_404(SubCategory, sub_category=self.kwargs.get('sub_category'))
		return Goal.objects.filter(sub_category=self.SubCategory)
        
class Myview4(ListView):
	model = MCQuestion
	template_name = 'quiz/mathematics_question_list2.html'
	def get_queryset(self):
		self.Goal = get_object_or_404(Goal, goal=self.kwargs.get('goal'))
		return MCQuestion.objects.filter(goal=self.Goal)

