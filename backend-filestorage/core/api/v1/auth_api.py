# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny,)
#     serializer_class = RegisterSerializer
#
#
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#
#     @action(methods=['get'], detail=True)
#     def whoami(self, request):
#         hostname = socket.getfqdn()
#         ip = socket.gethostbyname_ex(hostname)[2][0]
#         return Response({"id": self.request.user.id,
#                          "username": self.request.user.username,
#                          "email": self.request.user.email,
#                          "local ip": ip
#                          })
