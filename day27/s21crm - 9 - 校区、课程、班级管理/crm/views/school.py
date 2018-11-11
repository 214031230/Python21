from django.shortcuts import render,redirect
from django.urls import reverse
from crm import models
from crm.forms.school import SchoolModelForm

def school_list(request):
    """
    :param request:
    :return:
    """
    queryset = models.School.objects.all()
    return render(request,'school_list.html',{'queryset':queryset})


def school_add(request):
    """
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = SchoolModelForm()
        return render(request,'form.html',{'form':form})
    
    form = SchoolModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_list'))
    return render(request, 'form.html', {'form': form})


def school_edit(request,nid):
    """
    :param request:
    :param nid:
    :return:
    """
    obj = models.School.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = SchoolModelForm(instance=obj)
        return render(request, 'form.html', {'form': form})
    form = SchoolModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('school_list'))
    else:
        return render(request, 'form.html', {'form': form})
    
    
def school_del(request,nid):
    """
    课程删除
    :param request:
    :param nid:
    :return:
    """
    models.School.objects.filter(id=nid).delete()
    return redirect(reverse('school_list'))