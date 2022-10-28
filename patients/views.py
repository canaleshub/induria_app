from django.contrib import messages
from django.shortcuts import render
from .models import Patients, PatientUploads
from .classify import predict_image


# Create your views here.


def index(request):
    return render(request, 'patients/index.html')


def searchPatient(request):
    if request.method == 'GET':
        try:
            patient_code = request.GET['code']
            patient = Patients.objects.get(patient_code=patient_code)
            patient_uploads = PatientUploads.objects.get(patient_id=patient.id)
            context = {
                'patient': patient,
                'image': patient_uploads.image.url,
                'predicted_class': patient_uploads.predicted_class
            }
            messages.success(request, 'Patient found successfully.')
            return render(request, 'patients/patient_details.html', context)
        except Patients.DoesNotExist:
            messages.error(request, 'Patient not found.', extra_tags='danger')
            return render(request, 'patients/index.html')


def checkCode(code):
    if code:
        try:
            patient = Patients.objects.filter(patient_code=code).exists()
            if patient:
                return True
            else:
                return False
        except Patients.DoesNotExist:
            return False
    else:
        return False


def predict(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        gender = request.POST['gender']
        code = request.POST['code']
        image = request.FILES['image']
        check = checkCode(code)
        if not check:
            if name and age and gender and code and image is not None:
                patient_data = Patients.objects.create(
                    name=name,
                    age=age,
                    gender=gender,
                    patient_code=code,
                )
                patient_data.save()
                # Upload the image also.
                upload_image = PatientUploads.objects.create(
                    patient_id=patient_data.id,
                    image=image
                )
                upload_image.save()
                print(upload_image.image.path)
                # Predict the image.
                prediction = predict_image(upload_image.image.path)
                if prediction == 1:
                    classname = "Encia Sangrado"
                else:
                    classname = "Encia Sana"
                # Save the prediction.
                upload_image.predicted_class = classname
                upload_image.save()
                messages.success(request, 'Prediction saved successfully.')
                context = {
                    "name": name,
                    "gender": gender,
                    "age": age,
                    "code": code,
                    "predicted_class": classname,
                    "image": upload_image.image.url
                }
                return render(request, 'patients/result.html', {'context': context})
            else:
                messages.error("Please Fill every details in the form", extra_tags='danger')
                return render(request, 'patients/index.html')
        else:
            messages.error(request, "Patient already exists", extra_tags='danger')
            return render(request, 'patients/index.html')
    else:
        return render(request, 'patients/index.html')
