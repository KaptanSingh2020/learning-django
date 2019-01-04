from django.http.response import HttpResponse, Http404
from .models import Tag, Startup
from django.template import Context, loader, RequestContext
from django.shortcuts import get_object_or_404, render_to_response, render 
from .forms import TagForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import View

class TagList(View):
    page_qwarg = 'page'
    paginate_by = 5
    template_name = 'organizer/tag_list.html'

    def get(self, request):
        tags = Tag.objects.all()
        paginator = Paginator(tags, self.paginate_by)
        page_number = request.GET.get(self.page_qwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_qwarg, n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(pkw=self.page_qwarg, n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'tag_list': page
        }
        return render(request, self.template_name, context)


def tag_list_2(request): # homepage() is now tag_list()
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = Context({'tag_list': tag_list})
    output = template.render(context)
    return HttpResponse(output)

# render_to_response() is used here to shorten the code.
def homepage_2(request):  
    return render_to_response('organizer/tag_list.html', {'tag_list': Tag.objects.all()})

# RequestContext() is used here instead of Context()
def homepage_3(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('organizer/tag_list.html')
    context = RequestContext(request, {'tag_list': tag_list})
    output = template.render(context)
    return HttpResponse(output)

# render() is used here instead of render_to_response(). It automatically uses RequestContext()
def homepage_4(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def tag_create(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            new_tag = form.save()
            return redirect(new_tag)
    else:
        form = TagForm()
    return render(request, 'organizer/tag_form.html', {'form': form})

def tag_detail(request, slug):
    try:                                         
        tag = Tag.objects.get(slug__iexact=slug)
    except Tag.DoesNotExist:
        raise Http404
    template = loader.get_template('organizer/tag_detail.html')
    context = Context({'tag': tag})
    return HttpResponse(template.render(context))

# get_object_or_404() and render_to_response() are used to shorten the code.
def tag_detail_2(request):  
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render_to_response('organizer/tag_detail.html', {'tag': tag})

# RequestContext() is used here instead of Context()
def tag_detail_3(request):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    template = loader.get_template('organizer/tag_detail.html')
    context = RequestContext(request, {'tag': tag})
    return HttpResponse(template.render(context))

# render() is used here instead of render_to_response(). It automatically uses RequestContext()
def tag_detail_4(request):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})

class StartupList(View):
    page_qwarg = 'page'
    paginate_by = 5
    template_name = 'organizer/startup_list.html'

    def get(self, request):
        startups = Startup.objects.all()
        paginator = Paginator(startups, self.paginate_by)
        page_number = request.GET.get(self.page_qwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        if page.has_previous():
            prev_url = "?{pkw}={n}".format(pkw=self.page_qwarg, n=page.previous_page_number())
        else:
            prev_url = None
        if page.has_next():
            next_url = "?{pkw}={n}".format(pkw=self.page_qwarg, n=page.next_page_number())
        else:
            next_url = None
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'paginator': paginator,
            'previous_page_url': prev_url,
            'startup_list': page
        }
        return render(request, self.template_name, context)

def startup_list_2(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})


# def homepage(request):
#     tag_list = Tag.objects.all()
#     output = ", ".join([tag.name for tag in tag_list])
#     return HttpResponse(output)

# def homepage(request):
#  tag_list = Tag.objects.all()
#  html_output = "<html>\n"
#  html_output += "<head>\n"
#  html_output += " <title>"
#  html_output += "Don't Do This!</title>\n"
#  html_output += "</head>\n"
#  html_output += "<body>\n"
#  html_output += " <ul>\n"
#  for tag in tag_list:
#    html_output += " <li>"
#    html_output += tag.name.title()
#    html_output += "</li>\n"
#  html_output += " </ul>\n"
#  html_output += "</body>\n"
#  html_output += "</html>\n"
#  return HttpResponse(html_output)
