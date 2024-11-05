from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .serializers import RegisterSerializer
from django.urls import reverse

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = user.password  # Using password hash as a token example (not recommended in production)
            verification_url = f"http://{get_current_site(request).domain}{reverse('activate', args=[uid, token])}"
            subject = 'Activate your account'
            message = render_to_string('/activationemail.html', {
                'user': user,
                'verification_url': verification_url
            })
            send_mail(subject, message, 'noreply@example.com', [user.email])
            return Response({"message": "Check your email to activate your account."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ActivateAccountView(APIView):
    def get(self, request, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
            if user.password == token:
                user.is_active = True
                user.save()
                return Response({"message": "Account activated successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({"error": "Invalid activation link"}, status=status.HTTP_400_BAD_REQUEST)
