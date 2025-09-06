from django.shortcuts import render
from django.views.generic import  ListView,TemplateView
from .models import Characters,diagram
from django.urls import reverse_lazy

# Create your views here.
class SearchView(ListView):
    template_name = 'search.html'
    model = Characters
    success_url= reverse_lazy('search')
    c={}
    even=4.9 #相性五分とする勝率下限
    fighters_tuple=(
        'luke', 'jamie', 'manon', 'kimberly', 'marisa', 
        'lily', 'jp', 'juri', 'deejay', 'cammy', 
        'ryu', 'ehonda', 'blanka', 'guile', 'ken',
        'chunli', 'zangief', 'dhalsim', 'rashid',
        'aki', 'ed', 'akuma', 'mbison', 'terry',
        'mai', 'elena'
    ) #8/13現在実装されているキャラ
    #サガットも実装されているが勝率が発表されていないので無視
    

    def post(self,request): #POSTリクエストでメインキャラを受け取る
        main_dia=[]
        choice=request.POST.get("choice")
        wanted=request.POST.get("wanted")
        y=Characters.objects.get(name=choice)
        if(wanted!="なし"):
            w=Characters.objects.get(name=wanted)
        else:
            w="a"
        m=diagram.objects.get(id=y.id) #メインキャラの勝率を取得
        mc=[]
        for i in self.fighters_tuple:
            mc.append(eval("m."+i))
        pos=1
        for i in mc:
            if i <= self.even:
                main_dia.append(pos) #不利キャラをリストに入れる
            pos+=1
        for i in Characters.objects.all():
            count=0
            x=1
            sc=[]
            if(type(w)!= str):
                if(eval("diagram.objects.get(id=i.id)."+self.fighters_tuple[w.id-1])<=self.even):
                    self.c[i.name]=0
                    continue
            for j in self.fighters_tuple:
                if x in main_dia: 
                    sc.append(eval("diagram.objects.get(id=i.id)."+j))
                x+=1
            for j in sc: #メインで不利かつ候補のキャラで五分以上(j>=self.even)の数を数える
                if j>=self.even:
                    count+=1
            self.c[i.name] = count
        submit_data=dict(sorted(self.c.items(), key=lambda x:x[1], reverse=True))
        return render(request,"search.html",{"submit":submit_data})
    
class indexView(TemplateView):
    template_name="index.html"