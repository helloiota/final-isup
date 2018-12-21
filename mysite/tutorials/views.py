from django.shortcuts import render

# Create your views here.
def disclaimer(request):
	return render(request, 'tutorials/disclaimer.html')

def whatisiota(request):
	return render(request, 'tutorials/whatisiota.html')

def wallets(request):
	return render(request, 'tutorials/wallets.html')

def foundation(request):
	# foundation_roster = Foundation.objects.all()
	return render(request, 'tutorials/foundation.html') #, {'foundation': foundation_roster})

def buyiota(request):
	return render(request, 'tutorials/buyiota.html')