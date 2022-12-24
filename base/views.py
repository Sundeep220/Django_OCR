from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import logging
logger = logging.getLogger(__name__)
from django.contrib.auth.decorators import login_required
import PyPDF2
from PIL import Image
from pytesseract import pytesseract
import pypdfium2 as pdfium
# Create your views here.

def loginreq(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)

def register(request):
    if request.method != 'POST':
        return render(request, 'base/register.html')
    # Check if user exists
    username = request.POST['uname']
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    password = request.POST['pass']
    user_exist = False
    try:
        User.objects.get(username=username)
        user_exist = True
    except:
        logger.error("New user")
    if not user_exist:
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,email=email,
                                        password=password)
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'User already exists')
        return render(request, 'base/register.html')

def logout_req(request):
    logout(request)
    return render(request, 'base/form.html')


# def pdf_to_text(pdffile):


#     # Read the file
#     pdf = PyPDF2.PdfFileReader(pdffile)
#     content = ""
#     print(pdf.getNumPages())
#     for ii in range(pdf.getNumPages()):
#         # Get the page
#         page = pdf.getPage(ii)
#         print(page.extract_text())
#         content += page.extract_text()

#     print(content)

#     return content


def checkExt(file):
    """
    Function to return the extension of the file.
    """
    file_name: str = file.name
    file_extension = file_name.split(".")[-1]

    if file_extension == "pdf":
        return "pdf"
    else:
        return "image"

def ocr(file):
    """
    Function to returns the converted text from a PDF or an Image
    """
    # If the file type is PDF
    if checkExt(file) == "pdf":
        doc = pdfium.PdfDocument(file)
        # Check if the PDF contains more than one page
        if len(doc) > 1:
            return None
        else:
            page = doc.get_page(0)
            pil_image = page.render_to(
                pdfium.BitmapConv.pil_image,
            )
            content = ""
            pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"
            # Using pytesseract image_to_string method to get text from image 
            image_text = pytesseract.image_to_string(pil_image)

            content = image_text
            return content

    # If the file type is IMAGE
    elif checkExt(file) == "image":
        doc = Image.open(file)
        content = ""

        pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

        image_text = pytesseract.image_to_string(doc)

        content = image_text
        return content


@login_required(login_url="login")
def home(request):
    """
    Function that returns the form for user to upload file.
    """
    if request.method == "POST":
        files = request.FILES['file']
        doc = Document.objects.create(file=files, user=request.user, title=files.name)
        doc.save()
        content = ocr(file=files)
        print(content)
        if content is None:
            print("PDF should have more than one page")
            return redirect("home")

        ExtractedText.objects.create(file=doc,user=request.user,title=files.name,body=content)
        messages.success(request, 'File was uploaded successfully')
        return redirect('home')
    return render(request, 'base/form.html')

@login_required(login_url="login")
def files(request):
    """
    Function to returns all the uploaded files of user
    """
    user = request.user
    docs = user.document_set.all()
    # texts = ExtractedText.objects.filter(user=user)
    context = {'docs': docs}
    return render(request, 'base/files.html', context)

@login_required(login_url="login")
def textDetailedView(request, pk):
    """
    Function that returns the text extracted from pdf.
    """
    # user = request.user
    item = ExtractedText.objects.filter(file=pk)
    print(item[0].title)
    context = {'item': item}
    return render(request, 'base/text.html', context)
