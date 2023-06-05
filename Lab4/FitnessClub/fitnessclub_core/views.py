from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.core.exceptions import PermissionDenied
from .models import Gym, GymMembership, Schedule, GroupClass
from .forms import GymMembershipForm, GroupClassForm


def main_page(request):
    return HttpResponse('<h4>Abrqwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwacodabra</h4>')

def gym_list(request):
    gym_list = Gym.objects.all()

    return render(request, 'fitnessclub_core/gym_list.html', {'gym_list': gym_list})

def gym_detail(request, id):
    gym = get_object_or_404(Gym, id=id)

    return render(request, 'fitnessclub_core/gym_detail.html', {'gym': gym})

def gym_membership_detail(request, id):
    gym_membership = get_object_or_404(GymMembership, id=id)

    return render(request, 'fitnessclub_core/gym_membership_detail.html', {'gym_membership': gym_membership})

def create_gym_membership(request):
    if not request.user.is_staff:
        raise PermissionDenied("You are not allowed to access this page.")
    
    form = GymMembershipForm()

    if request.method == 'POST':
        form = GymMembershipForm(request.POST)

        if form.is_valid():
            gym_membership = form.save()
            return redirect('gym_membership_detail', id=gym_membership.id)

    return render(request, 'fitnessclub_core/create_gym_membership.html', {'form': form})

def group_class_list(request):
    group_class_list = GroupClass.objects.all()

    return render(request, 'fitnessclub_core/group_class_list.html', {'group_class_list': group_class_list})

def group_class_detail(request, id):
    group_class = get_object_or_404(GroupClass, id=id)

    return render(request, 'fitnessclub_core/group_class_detail.html', {'group_class': group_class})

def create_group_class(request):
    if not request.user.is_staff:
        raise PermissionDenied("You are not allowed to access this page.")
    
    form = GroupClassForm()

    if request.method == 'POST':
        form = GroupClassForm(request.POST)

        if form.is_valid():
            group_class = form.save()
            return redirect('group_class_detail', id=group_class.id)
    
    return render(request, 'fitnessclub_core/create_group_class.html', {'form': form})

def edit_group_class(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    
    group_class = None
    try:
        group_class = get_object_or_404(GroupClass, id=id)
    except:
        return HttpResponseNotFound('<h1>Group class not found</h1>')

    if request.method == 'POST':
        form = GroupClassForm(request.POST, instance=group_class)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = GroupClassForm(instance=group_class)

    return render(request, 'fitnessclub_core/edit_group_class.html', {'form': form, 'group_class': group_class})

def delete_group_class(request, id):
    if not request.user.is_staff:
        raise PermissionDenied("Permission denied!")
    
    group_class = None
    try:
        group_class = get_object_or_404(GroupClass, id=id)
        group_class.delete()
        return redirect('/')
    except:
        return HttpResponseNotFound('<h1>Group class not found</h1>')
