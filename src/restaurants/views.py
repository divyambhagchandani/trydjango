from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView,CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin\
import ramdom, urllib3

from .models import RestaurantLocation
from .forms import RestaurantCreateForms, RestaurantLocationCreateForm
# Create your views here.

@login_required
def restaurant_createview(request):
	form=RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		return HttpResponseRedirect("/restaurants/")
	template_name='restaurants/forms.html'
	context={"form": form}
	return render(request,template_name,context)

def restaurant_listview(request):
	template_name= 'restaurants/restaurants_list.html'
	Queryset=RestaurantLocation.objects.all()
	context={
	"object_list":Queryset
	}
	return render(request, template_name, context)
class RestaurantListView(ListView):
	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			queryset=RestaurantLocation.objects.filter(category__iexact=slug)
		else:
			queryset=RestaurantLocation.objects.all()
		return queryset
class RestaurantDetailView(DetailView):
			queryset=RestaurantLocation.objects.all()
			# def get_context_data(self,*args, **kwargs):
			# 	print(self.kwargs)
			# 	context=super(RestaurantDetailView, self).get_context_data(*args,**kwargs)
			# 	print(context)
			# def get_object(self,*args,**kwargs):
			# 	rest_id= self.kwargs.get('rest_id')
			# 	obj=get_object_or_404(RestaurantLocation, id=rest_id) #pk=rest_id
			# 	return obj
class RestaurantCreateView(LoginRequiredMixin,CreateView):
	login_url='/login/'
	form_class = RestaurantLocationCreateForm
	template_name= 'restaurants/forms.html'
	success_url="/restaurants/"
	def form_valid(self, form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		# instance.save()
		return super(RestaurantCreateView,self).form_valid(form)
class classbasedvesw():
	login_url='/login/'
	form_class = RestaurantLocationCreateForm
	template_name= 'restaurants/forms.html'
	success_url="/restaurants/"
	def form_valid(self, form):
		instance=form.save(commit=False)
		instance.owner=self.request.user
		# instance.save()
		return super(RestaurantCreateView,self).form_valid(form)
	












