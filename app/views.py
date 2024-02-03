from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from app.models import JobPost

job_title = ['Intern_role1', 'Data Engineer', 'Software Engineer', 'DevOps Engineer', 'Intern_role2',
             'Frontend Developer']

job_description = ['Developer', 'Azure Data Engineer', 'Software Development Engineer I', 'Azure DevOps Engineer',
                   'Data Analyst Intern', 'React Developer']


# Create your views here.
# def home_page(request):
#   return HttpResponse("<i><h1><b>JOB Details</h1></b></i>\n<ul><li>Intern</li><li>Data Engineer</li><li>Software "
#                        "Engineer</ul>")
# noinspection PyUnusedLocal
def job_list_homepage_view(request):
    # jobs_list = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_details', args=(job_id,))
    jobs = JobPost.objects.all()
    print(jobs)
    context = {"jobs": jobs}
    return render(request, template_name='app/job_list.html', context=context)
    # jobs_list += f"<li><a href = '{detail_url}'> {j} </a></li>"


# jobs_list += '</ul>'


class TempClass:
    x = 8


def hello_view(request):
    # template = loader.get_template('app/hello.html')
    name_list = ['Karan', 'Anurag', 'Rupen', 'Pratik']
    is_authenticated = False
    a_temp = TempClass()
    context = {'Name': 'kunal', 'age': 25, 'Name_list': name_list, 'a_temp': a_temp,
               'is_authenticated': is_authenticated}
    # return HttpResponse(template.render(context, request))
    return render(request, 'app/hello.html', context)


def job(request, ids):
    try:
        print("ids are this",ids)
        if ids == 0:  # or ids == "home" but error showing up. --expected int but got favicon.ico
            return redirect(reverse('job_list_home'))
        # context = {'Job_title': job_title[ids], 'Job_description': job_description[ids]}
        jo = JobPost.objects.get(pk=ids)
        print("jo value is ",jo)
        context = {"job": jo}
        return render(request, 'app/job_details.html', context)
    except IndexError:
        return HttpResponseNotFound("Page Not Found")
