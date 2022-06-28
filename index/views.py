from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import Helper
from .models import User


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)  ## gets email and password to create a user
        if serializer.is_valid():
            serializer.save()
            token = Helper(request).get_token(
                serializer.data["id"], serializer.data["fullname"]
            )

            return Response(
                {
                    "status": True,
                    "message": "User created successfully",
                    "token": token,
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "message": serializer.errors},
                status=status.HTTP_200_OK,
            )

class Login(APIView):
    def post(self, request, *args, **kwargs):

        email = request.data["email"]
        password = request.data["password"]
        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(
                {"status": False, "message": "User not Found"},
                status=status.HTTP_200_OK,
            )
        
        if not user.check_password(password):
            return Response(
                {"status": False, "message": "Incorrect Password"},
                status=status.HTTP_200_OK,
            )

        token = Helper(request).get_token(user.id)
        serializers = UserSerializer(user)
        return Response(
            {
                "status": True,
                "message": "success",
                "token": token,
                "data": serializers.data,
            },
            status=status.HTTP_200_OK,

        )

class ForgotPasswordView(APIView):
	## Add your forgot password functionalities here
	pass


class VerifyForgotPasswordView(APIView):
	#Verify forgot password functionalities
	pass