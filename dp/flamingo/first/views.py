from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Avg


from first.models import Restaurant, Review, Rating
from first.forms import RatingForm

# # # # # # # # # # # #
def Login(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'first/login.html', c)

def AuthView(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/first/home/')
    else:
        return HttpResponseRedirect('/first/login/')

def Logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/first/login/')
# # # # # # # # # # # #

def Home(request):
    return render(request, 'first/home.html', {})

class RestaurantListView(ListView):
    queryset = Restaurant.objects.all()

class RestaurantDetailView(DetailView):
    model = Restaurant

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetailView, self).get_context_data(**kwargs)
        context['review'] = Review.objects.filter(restaurant_id=self.kwargs['pk']).order_by('-time')
        context['rating'] = Rating.objects.filter(restaurant_id=self.kwargs['pk'])
        context['avgrating'] = Rating.objects.filter(restaurant_id=self.kwargs['pk']).aggregate(Avg('rating'))['rating__avg']
        return context

class WriteReview(CreateView):
    model = Review
    success_url = "/first/restaurants/%(restaurant_id)s/"
    fields = ['restaurant','review']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.restaurant = Restaurant.objects.get(id=self.kwargs['pk'])
        return super(WriteReview, self).form_valid(form)

class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['review']
    success_url = "/first/restaurants/%(restaurant_id)s/"
    pk_url_kwarg = 'id'

class ReviewDeleteView(DeleteView):
    model = Review
    success_url = "/first/restaurants/%(restaurant_id)s/"
    pk_url_kwarg = 'id'

def Rate(request, pk):
    c = {}
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            defaults = {'rating': request.POST['rating']}
            Rating.objects.update_or_create(restaurant=Restaurant.objects.get(id=pk), user=request.user, defaults=defaults)
            url = reverse('restaurant_detail', kwargs={'pk':pk})
            return HttpResponseRedirect(url)
    else:
        form = RatingForm(initial={'restaurant': Restaurant.objects.get(id=pk),'user': request.user})
    c['form'] = form
    return render(request, 'first/rating_form.html', c)
