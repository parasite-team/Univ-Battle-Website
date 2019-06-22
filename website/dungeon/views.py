from django.shortcuts import render,redirect
from .forms import inputAnswer
# Create your views here.


def main(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='start':
                return redirect('dungeon:start')   
            else:
                return render(request,'dungeon/main/main.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/main/main.html',{'form':form})

def start(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='fibonaccinumbers':
                return redirect('dungeon:stage1')   
            else:
                return render(request,'dungeon/stage/start.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/start.html',{'form':form})

def stage1(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='goodjob':
                return redirect('dungeon:stage2')   
            else:
                return render(request,'dungeon/stage/stage1.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/stage1.html',{'form':form})


def stage2(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='restarts':
                return redirect('dungeon:stage3')   
            else:
                return render(request,'dungeon/stage/stage2.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/stage2.html',{'form':form})


def stage3(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='57':
                return redirect('dungeon:stage4')   
            else:
                return render(request,'dungeon/stage/stage3.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/stage3.html',{'form':form})


def stage4(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='start':
                return redirect('dungeon:stage5')   
            else:
                return render(request,'dungeon/stage/stage4.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/stage4.html',{'form':form})


def stage5(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='solo':
                return redirect('dungeon:stage6')   
            else:
                return render(request,'dungeon/stage/stage5.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/stage5.html',{'form':form})


def stage6(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='mouse':
                return redirect('dungeon:last_stage')   
            else:
                return render(request,'dungeon/stage/stage6.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/stage6.html',{'form':form})


def last_stage(request):
    if request.method=='POST':
        form = inputAnswer(request.POST)
        if form.is_valid():
            if form.cleaned_data['answer']=='hovseppushman':
                return redirect('dungeon:treasure')   
            else:
                return render(request,'dungeon/stage/last_stage.html',{'form':form,'flag':True})
    else:
        form = inputAnswer()
    return render(request,'dungeon/stage/last_stage.html',{'form':form})


def treasure(request):
    return render(request,'dungeon/bonus/treasure.html')



def stage4redirect(request):
    return redirect('dungeon:stage5')