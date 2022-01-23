from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import mailSerializer
from .utils import Util
from .models import MailModel

# Create your views here.
class MailView(APIView):
	serializer_class 	= mailSerializer

	def post(self, request):
		data 			= mailSerializer(data=request.data)
		data.is_valid(raise_exception=True)
		validated_data  = data.data

		# Sending submited mail to admin
		Util.sendAdminEmailFunc({
			'company': validated_data["company_name"],
			'name': validated_data["name"],
			'email_from': validated_data["email"],
			'email_to': validated_data["company_email"],
			'message': validated_data["message"]
		})

		# Sending response mail to client
		Util.sendClientEmailFunc({
			'company': validated_data["company_name"],
			'name': validated_data["name"],
			'email_to': validated_data["email"],
			'message': validated_data["message"]
		})

		# Saving mail
		mail 		= MailModel.objects.create(
						company_name=validated_data["company_name"],
						company_email=validated_data["company_email"],
						name=validated_data["name"],
						email=validated_data["email"],
						message=validated_data["message"])

		return Response({
			"status": status.HTTP_200_OK,
			"message": "Mail successful"
			
		}, status=status.HTTP_201_CREATED)



