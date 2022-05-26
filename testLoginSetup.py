from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User
import pdb

class TestLoginSetup(APITestCase):

	#* Function to create a fake user log in
	def setUp(self):
		self.login_url = '/auth/login/'
		self.user = User.objects.create_superuser(email='test@test.com', password='test')

		response = self.client.post(
			self.login_url,
			{
				'email': self.user.email,
				'password': 'test'
			},
			format='json'
		)

		self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
		#pdb.set_trace() #* Whit this line we can see the response of the request
		self.token = response.data['access_token']
		self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
		return super().setUp()

	def test_login_setup(self):
		print(self.token)
