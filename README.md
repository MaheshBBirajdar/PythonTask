# PythonTask

# To migrate the database open terminal in project directory and type :-

    python manage.py makemigrations
    
    python manage.py migrate
    
    
# Run the server :-

    python manage.py runserver
    
    (Note :- Follow the steps for to run the Project)
     1) cd upforce
      
      
# API Endpoints :- 

{
    path('user/list', UserListView.as_view(), name='userlist' ),
    path('user/create/', UserCreateView.as_view(),name='usercreate' ),
    path('user/<int:pk>/', UserRetrieveView.as_view(),name='userR' ),
    path('user/update/<int:pk>/', UserUpdateView.as_view(),name='userU' ),
    path('user/delete/<int:pk>/', UserDestroyView.as_view(),name='userD' ),

    path('post/list', PostListView.as_view(), name='Postlist' ),
    path('post/create/', PostCreateView.as_view(),name='Postcreate' ),
    path('post/<int:pk>/', PostRetrieveView.as_view(),name='PostR' ),
    path('post/update/<int:pk>/', PostUpdateView.as_view(),name='PostU' ),
    path('post/delete/<int:pk>/', PostDestroyView.as_view(),name='PostD' ),

    path('like/list', LikeListView.as_view(), name='Likelist' ),
    path('like/create/', LikeCreateView.as_view(),name='Likecreate' ),
    path('like/<int:pk>/', LikeRetrieveView.as_view(),name='LikeR' ),
    path('like/update/<int:pk>/', LikeUpdateView.as_view(),name='LikeU' ),
    path('like/delete/<int:pk>/', LikeDestroyView.as_view(),name='LikeD' ),
    
   }
