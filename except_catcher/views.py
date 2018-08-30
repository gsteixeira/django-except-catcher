# Create your views here.
from django.contrib.auth.decorators import user_passes_test
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse
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
    return redirect(reverse('view_error', kwargs={'pk': pk}))

@user_passes_test(lambda u: u.is_superuser)
def delete_error(request, pk):
    """ Mark a particular exceptions as resolved
    """
    report = ExceptionReport.objects.get(pk=pk)
    report.delete()
    return redirect(reverse('list_reports'))

@user_passes_test(lambda u: u.is_superuser)
def resolve_all(request):
    """ Mark all exceptions as resolved
    """
    list_reports = ExceptionReport.objects.filter(resolved=False)
    with transaction.atomic():
        for rep in list_reports:
            rep.resolved = True
            rep.save()
    return redirect(reverse('list_reports'))

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
    return redirect(reverse('list_reports'))
