from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .user_controller import UserController


class UserView(APIView):
    user_controller = UserController()
    permission_classes = [AllowAny]

    def get(self, request, user_id=None):
        return self.user_controller.get_user(request, user_id)

    def post(self, request):
        return self.user_controller.create_user(request)

    def patch(self, request, user_id):
        return self.user_controller.update_user(request, user_id)

    def delete(self, request, user_id):
        return self.user_controller.delete_user(request, user_id)


class UserLoginView(APIView):
    user_controller = UserController()
    permission_classes = [AllowAny]

    def post(self, request):
        return self.user_controller.login(request)
