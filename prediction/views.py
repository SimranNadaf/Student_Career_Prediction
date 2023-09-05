from django.shortcuts import render
import pickle
from django.views.decorators.csrf import requires_csrf_token

# Create your views here.
def index(request):
    return render(request,'index.html')

def predict(request):
    if request.method != 'POST':
        return render(request,'index.html')

    if request.method=='POST':
        Drawing=int(request.POST['Drawing'])
        Dancing=int(request.POST['Dancing'])
        Singing=int(request.POST['Singing'])
        Sports=int(request.POST['Sports'])
        Video_Game=int(request.POST['Video_Game'])
        Acting=int(request.POST['Acting'])
        Travelling=int(request.POST['Travelling'])
        Gardening=int(request.POST['Gardening'])
        Animals=int(request.POST['Animals'])
        Photography=int(request.POST['Photography'])
        Teaching=int(request.POST['Teaching'])
        Exercise=int(request.POST['Exercise'])
        Coding=int(request.POST['Coding'])
        Electricity_Components=int(request.POST['Electricity_Components'])
        Mechanic_Parts=int(request.POST['Mechanic_Parts'])
        Computer_Parts=int(request.POST['Computer_Parts'])
        Researching=int(request.POST['Researching'])
        Architecture=int(request.POST['Architecture'])
        Historic_Collection=int(request.POST['Historic_Collection'])
        Botany=int(request.POST['Botany'])
        Zoology=int(request.POST['Zoology'])
        Physics=int(request.POST['Physics'])
        Accounting=int(request.POST['Accounting'])
        Economics=int(request.POST['Economics'])
        Sociology=int(request.POST['Sociology'])
        Geography=int(request.POST['Geography'])
        Psycology=int(request.POST['Psycology'])
        History=int(request.POST['History'])
        Science=int(request.POST['Science'])
        Bussiness_Education=int(request.POST['Bussiness_Education'])
        Chemistry=int(request.POST['Chemistry'])
        Mathematics=int(request.POST['Mathematics'])
        Biology=int(request.POST['Biology'])
        Makeup=int(request.POST['Makeup'])
        Designing=int(request.POST['Designing'])
        Content_writing=int(request.POST['Content_writing'])
        Crafting=int(request.POST['Crafting'])
        Literature=int(request.POST['Literature'])
        Reading=int(request.POST['Reading'])
        Cartooning=int(request.POST['Cartooning'])
        Debating=int(request.POST['Debating'])
        Asrtology=int(request.POST['Asrtology'])
        Hindi=int(request.POST['Hindi'])
        French=int(request.POST['French'])
        English=int(request.POST['English'])
        Urdu=int(request.POST['Urdu'])
        Other_Language=int(request.POST['Other_Language'])
        Solving_Puzzles=int(request.POST['Solving_Puzzles'])
        Gymnastics=int(request.POST['Gymnastics'])
        Yoga=int(request.POST['Yoga'])
        Engeeniering=int(request.POST['Engeeniering'])
        Doctor=int(request.POST['Doctor'])
        Pharmisist=int(request.POST['Pharmisist'])
        Cycling=int(request.POST['Cycling'])
        Knitting=int(request.POST['Knitting'])
        Director=int(request.POST['Director'])
        Journalism=int(request.POST['Journalism'])
        Bussiness=int(request.POST['Bussiness'])
        Listening_Music=int(request.POST['Listening_Music'])
        
       

        with open('static/final_model','rb')as f:
            mp=pickle.load(f)

        pred_value=mp.predict([[Drawing,Dancing,Singing,Sports,Video_Game,Acting,
        Travelling,Gardening,Animals,Photography,Teaching,
        Exercise,Coding,Electricity_Components,Mechanic_Parts,
        Computer_Parts,Researching,Architecture,Historic_Collection,
        Botany,Zoology,Physics,Accounting,Economics,Sociology,
        Geography,Psycology,History,Science,Bussiness_Education,
        Chemistry,Mathematics,Biology,Makeup,Designing,
        Content_writing,Crafting,Literature,Reading,Cartooning,
        Debating,Asrtology,Hindi,French,English,Urdu,
        Other_Language,Solving_Puzzles,Gymnastics,Yoga,
        Engeeniering,Doctor,Pharmisist,Cycling,Knitting,
        Director, Journalism, Bussiness,Listening_Music]])
        # pred_value=int(pred_value[0])

        courses=list(['Animation, Graphics and Multimedia',
        'B.Arch- Bachelor of Architecture', 'B.Com- Bachelor of Commerce',
        'B.Ed.', 'B.Sc- Applied Geology', 'B.Sc- Nursing',
        'B.Sc. Chemistry', 'B.Sc. Mathematics',
        'B.Sc.- Information Technology', 'B.Sc.- Physics',
        'B.Tech.-Civil Engineering',
        'B.Tech.-Computer Science and Engineering',
        'B.Tech.-Electrical and Electronics Engineering',
        'B.Tech.-Electronics and Communication Engineering',
        'B.Tech.-Mechanical Engineering', 'BA in Economics',
        'BA in English', 'BA in Hindi', 'BA in History',
        'BBA- Bachelor of Business Administration',
        'BBS- Bachelor of Business Studies',
        'BCA- Bachelor of Computer Applications',
        'BDS- Bachelor of Dental Surgery',
        'BEM- Bachelor of Event Management',
        'BFD- Bachelor of Fashion Designing',
        'BJMC- Bachelor of Journalism and Mass Communication',
        'BPharma- Bachelor of Pharmacy',
        'BTTM- Bachelor of Travel and Tourism Management',
        'BVA- Bachelor of Visual Arts', 'CA- Chartered Accountancy',
        'CS- Company Secretary', 'Civil Services',
        'Diploma in Dramatic Arts', 'Integrated Law Course- BA + LL.B',
        'MBBS'])

        # entry=CropData(N=N,P=P,K=K,temperature=temperature,humidity=humidity,ph=ph,rainfall=rainfall,prediction=pred_value,date=datetime.datetime.now())
        # entry.save()
        data={'prediction':courses[pred_value[0]]}
        return render(request,'predict.html',data)

