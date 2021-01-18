# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from except_catcher.models import ExceptionReport

@user_passes_test(lambda u: u.is_superuser)
def view_error(request, pk):
    """ View details about an specific exception
    """
    report = ExceptionReport.objects.get(pk=pk)
    data = {
        'report': report,
        }
    return render(request, 'except_catcher/view_error.html', data)

@user_passes_test(lambda u: u.is_superuser)
def mark_resolved(request, pk):
    """ Mark a particular exceptions as resolved
    """
    report = ExceptionReport.objects.get(pk=pk)
    report.resolved = not report.resolved
    report.save()
    return redirect(reverse('except_catcher:view_error', kwargs={'pk': pk}))

@user_passes_test(lambda u: u.is_superuser)
def delete_error(request, pk):
    """ Delete a particular exception report
    """
    report = ExceptionReport.objects.get(pk=pk)
    report.delete()
    return redirect(reverse('except_catcher:list_reports'))

@user_passes_test(lambda u: u.is_superuser)
def resolve_all(request):
    """ Mark all exceptions as resolved
    """
    list_reports = ExceptionReport.objects.filter(resolved=False)
    with transaction.atomic():
        for rep in list_reports:
            rep.resolved = True
            rep.save()
    return redirect(reverse('except_catcher:list_reports'))

@user_passes_test(lambda u: u.is_superuser)
def delete_all(request):
    """ Mark all exceptions as resolved
    """
    list_reports = ExceptionReport.objects.all()
    list_reports.delete()
    return redirect(reverse('except_catcher:list_reports'))

@user_passes_test(lambda u: u.is_superuser)
def list_reports(request):
    """ Lists all recorded exceptions
    """
    if 'all' in request.GET.keys():
        list_reports = ExceptionReport.objects.all()
    else:
        list_reports = ExceptionReport.objects.filter(resolved=False)
    data = {
        'list_reports': list_reports,
        }
    return render(request, 'except_catcher/list_report.html', data)

@user_passes_test(lambda u: u.is_superuser)
def test_exception(request):
    """ This is just to purposely throw an exception to test the system
    """
    one = 1
    zero = 0
    divide_by_zero = one / zero
    return redirect(reverse('except_catcher:list_reports'))

@csrf_exempt
def report_api(request):
    """ This view receives a post with an exception report
    """
    if request.method == "POST":
        remote_host = request.POST.get('host')
        msg = request.POST.get('message')
        message = ' - '.join([ host, msg ])
        html_message = request.POST.get('html_message')
        report = ExceptionReport.objects.create(subject=subject,
                                                message=message,
                                                html_message=html_message)
        return HttpResponse('200')
    return HttpResponse('400', status_code=400)
