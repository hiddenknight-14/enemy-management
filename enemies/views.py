from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse

from enemies.models import Enemy

# Create your views here.

def addEnemy(request):
    enemyName = request.POST['enemyName'] 
    enemyReason = request.POST['enemyReason']

    Enemy.objects.create(name=enemyName, reason=enemyReason)

    return redirect('enemy-home')


def mark_as_revenge_taken(request, pk):
    enemy = get_object_or_404(Enemy, pk=pk)
    enemy.revenge_taken = True
    enemy.save()
    return redirect('enemy-home')


def mark_as_revenge_not_taken(request, pk):
    enemy = get_object_or_404(Enemy, pk=pk)
    enemy.revenge_taken = False
    enemy.save()
    return redirect('enemy-home')

def deleteEnemy(request, pk):
    enemy = get_object_or_404(Enemy, pk=pk)
    enemy.delete()
    return redirect('enemy-home')

def editEnemy(request, pk):
    enemy = get_object_or_404(Enemy, pk=pk)

    if request.method == 'POST':
        updatedName = request.POST['updatedName']
        updatedReason = request.POST['updatedReason']
        
        enemy.name = updatedName
        enemy.reason = updatedReason

        enemy.save()

        return redirect('enemy-home')

    else:
        context = {
            'enemy': enemy,
        }
        return render(request, 'edit_enemy.html', context=context)