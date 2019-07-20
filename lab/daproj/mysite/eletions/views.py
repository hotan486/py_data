from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

# 실제 html를 생성하는곳
def index(request):
	candidates = Candidate.objects.all()
	# str = ''
	# for candidate in candidates:
	# 	str += "<p>{} 기호{}번({})<br>".format(candidate.name,
	# 		candidate.party_number,
	# 		candidate.area)
	# 	str += candidate.introduction+"</p>"
	#return HttpResponse(str)
	context = {'candidates':candidates}
	return render(request, 'elections/index.html',context)