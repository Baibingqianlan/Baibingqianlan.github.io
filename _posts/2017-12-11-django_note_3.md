---
layout: post
---

## django's generic view ##

1. Convert the URLconf.
1. inherite from django.views
> from django.views import generic.
 
	 class IndexView(generic.ListView):
    	template_name='blog/index.html'
    	context_object_name='latest_question_list'#overide'question_list'

     def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

	class DetailView(generic.DetailView):
    	model = Question
    	template_name = 'polls/detail.html'


	class ResultsView(generic.DetailView):
    	model = Question
    	template_name = 'polls/results.html'



[generic view document](https://docs.djangoproject.com/en/dev/topics/class-based-views/ "generic view")

## automated testing ##
