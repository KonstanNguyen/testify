from django.urls import path
from . import views
from . import features

urlpatterns = [
    # Login - Register
    path('', views.login_register, name='login-register'),
    path('login/lsv', features.login_sv, name='login-sv'),
    path('login/lgv', features.login_gv, name='login-gv'),
    path('login/rgv', features.register_sv, name='register-sv'),
    path('list-question', features.get_list_questions, name='list-question'),
    path('answer-question', features.update_answer, name='answer-question'),
    path('update-time', features.update_time, name='update-time'),
    path('', views.coso_table, name='coso'),
    path('khoa/', views.khoa_table, name='khoa'),
    path('lop/', views.lop_table, name='lop'),
    path('giangvien/', views.gv_table, name='giangvien'),
    path('sinhvien/', views.sv_table, name='sinhvien'),
    path('monhoc/', views.mon_table, name='monhoc'),
    path('bode/', views.bode_table, name='bode'),
    path('cauhoi/', views.bode_table_gv, name='cauhoi'),
    path('dangkythi/', views.dangky_table, name='dangkythi'),
    path('dangkythi_gv/', views.dangky_table_gv, name='dangkythi-gv'),
    path('danhsachthi/', views.dangky_table_sv, name='danhsachthi'),

    # Tính năng của Coso
    path('add_khoa/', features.add_Khoa, name='add-khoa'),
    path('update_khoa/', features.update_Khoa, name='update-khoa'),
    path('delete_khoa/', features.delete_Khoa, name='delete-khoa'),
]