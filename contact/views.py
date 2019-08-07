from .models import Contact
from .forms import ContactForm
from django.shortcuts import render, redirect, get_object_or_404


# -------------------------------------
# ---------- Contact view -------------
# -------------------------------------
def contactUs(request):
	if request.method == 'POST':
		form = ContactForm(request.POST or None)
		if form.is_valid():
			if request.user.is_authenticated:
				instance = form.save(commit=False)
				instance.user = request.user
				instance.save()
				return redirect('home:home')

	else:
		form = ContactForm()

	context = {
		'form': form,
	}

	return render(request, 'contact/contact_form.html', context)



def messages(request):

	messages = Contact.objects.all().order_by('-msg_send_date')

	context ={
		'messages': messages,
	}

	return render(request, 'contact/messages.html', context)