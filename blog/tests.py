from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Story

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework.response import Response


CustomUser = get_user_model()


def get_jwt_tokens(user):
    """Get both the refresh and access token for user"""

    try:
        token = RefreshToken.for_user(user=user)

        return {
            'access': str(token.access_token),
            'refresh': str(token)
        }

    except TokenError as e:
        data = {'status': 'error', 'message': str(e)}
        return Response(data, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class StoryDeleteTest(APITestCase):

    def setUp(self):

        self.author_user = CustomUser.objects.create_user(username='author', password='password')
        self.other_user = CustomUser.objects.create_user(username='otheruser', password='password')
        
        self.story = Story.objects.create(
            author=self.author_user,
            title='Test Story Headline',
            content='This is a short content for testing the delete restriction.',
        )

    def test_user_cannot_delete_another_users_story(self):
        # Log in with the unauthorized user

        token = get_jwt_tokens(self.other_user)

        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {token['access']}")
        
        # Try to delete the Story created by the author
        response = self.client.delete(reverse('story-detail',args=[self.story.id]))

        # Assert that the response status is 403
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Test the Story still exists in the database
        self.assertTrue(Story.objects.filter(id=self.story.id).exists())
    
    def test_author_can_delete_own_story(self):
        # Log in with the author user
        token = get_jwt_tokens(self.author_user)
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {token['access']}")
        
        # Try to delete the Story created by the author

        response = self.client.delete(reverse('story-detail',args=[self.story.id]))
        print(response.data)
        # Assert that the response status is 204
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Ensure the Story is deleted from the database
        self.assertFalse(Story.objects.filter(id=self.story.id).exists())
