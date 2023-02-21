from django.shortcuts import render
from django.shortcuts import HttpResponse
# from DFA.conn import r1,r2,r3,r4,r5,r6,r7

# Create your views here.
def q1(request):
 r1,r2,r3,r4,r5,r6,r7=193,1381,1589,1141,21,83,0
 return render(request, 'index.html', {'result1':r1,'result2':r2,'result3':r3,'result4':r4,'result5':r5,'result6':r6,'result7':r7})