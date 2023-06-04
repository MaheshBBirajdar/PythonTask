# PythonTask

# To migrate the database open terminal in project directory and type :-

    python manage.py makemigrations
    
    python manage.py migrate
    
    
# Run the server :-

    python manage.py runserver
    
    (Note :- Follow the steps for to run the Project)
     1) cd upforce
      
      
# API Endpoints :- 

    path('user/list', UserListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserRetrieveView.as_view() ),
    path('user/update/<int:pk>/', UserUpdateView.as_view()),
    path('user/delete/<int:pk>/', UserDestroyView.as_view() ),

    path('post/list', PostListView.as_view() ),
    path('post/create/', PostCreateView.as_view() ),
    path('post/<int:pk>/', PostRetrieveView.as_view() ),
    path('post/update/<int:pk>/', PostUpdateView.as_view() ),
    path('post/delete/<int:pk>/', PostDestroyView.as_view() ),

    path('like/list', LikeListView.as_view() ),
    path('like/create/', LikeCreateView.as_view() ),
    path('like/<int:pk>/', LikeRetrieveView.as_view()),
    path('like/update/<int:pk>/', LikeUpdateView.as_view()),
    path('like/delete/<int:pk>/', LikeDestroyView.as_view() ),
    
  
