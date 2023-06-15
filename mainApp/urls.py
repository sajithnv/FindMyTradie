from django.conf.urls import url
from django.urls import path
from mainApp.views import *
urlpatterns = [
    # Main url
    url(r'^$',index,name='index1'),
    # Employee urls
    url(r'^empProfile/$',empProfile,name='empProfile1'),
    url(r'^empRegister/$',empRegister,name='empRegister1'),
    url(r'^scheduledServices/toggleStatus/$',toggleStatus,name='toggleStatus1'),
    url(r'^empProfile/userModeView/(?P<e_name>[\w\-]+)$',empProfileByUser,name='empProfileByUserModeView1'),
    url(r'^empProfile/empProfileEdit/(?P<phone>\d+)$',empProfileEdit,name='empProfileEdit1'),
    url(r'^empProfile/serviceHistory/$',serviceHistory,name='empServiceHistory1'),
    url(r'^scheduledServices/userProfileByEmp/(?P<uname>[\w\-]+)$',userProfileByEmp,name='userProfileByEmp1'),


    # User urls
    url(r'^userProfile/$',userProfile,name='userProfile1'),
    url(r'^userProfile/serviceHistory/$',serviceHistory,name='userServiceHistory1'),
    url(r'^userProfile/userProfileEdit/(?P<phone>\d+)$',userProfileEdit,name='userProfileEdit1'),
    url(r'^userRegister/$',userRegister,name='userRegister1'),
    url(r'^searchWorkers/$',searchWorkers,name='searchWorkers1'),
    url(r'^searchWorkers/empProfileByUser/(?P<e_name>[\w\-]+)$',empProfileByUser,name='empProfileByUser1'),
    url(r'^scheduledServices/empProfileByUser/(?P<e_name>[\w\-]+)$',empProfileByUser,name='empProfileByUser2'),
    url(r'^searchWorkers/empProfileByUser/employeeHistoryByUser/(?P<e_name>[\w\-]+)$',employeeHistoryByUser,name='employeeHistoryByUser1'),
    url(r'^searchWorkers/employeeHistoryByAdmin/(?P<e_name>[\w\-]+)$',employeeHistoryByUser,name='employeeHistoryByAdmin1'),

    # Admin urls
    url(r'^userPageByAdmin/userProfileByAdmin/(?P<uname>[\w\-]+)$',userProfileByEmp,name='userProfileByAdmin1'),
    url(r'^promote(?P<ename>[\w\-]+)$',promote,name='promote1'),
    url(r'^demote(?P<ename>[\w\-]+)$',demote,name='demote1'),
    url(r'^userPageByAdmin/$',userPageByAdmin,name='userPageByAdmin1'),
    url(r'^profit/(?P<based>[\w\-]+)$',profit,name='profit1'),
    url(r'^searchWorkers/profit/(?P<based>[\w\-]+)$',profit,name='profit2'),




    # Common urls
    url(r'^scheduledServices/$',scheduledServices,name='scheduledServices1'),
    url(r'^scheduledServices/serviceHistory/$',serviceHistory,name='user_empServiceHistory1_BysScheduledServices'),
    url(r'^searchWorkers/confirmRequest/(?P<e_name>[\w\-]+)$',confirmRequest,name='confirmRequest1'),
    url(r'^scheduledServices/payAndAccept/(?P<id>\d+)$',payAndAccept,name='payAndAccept1'),
    url(r'^scheduledServices/reject/(?P<id>\d+)$',reject,name='reject1'),
    url(r'^scheduledServices/startWorking/(?P<id>\d+)$',startWorking,name='startWorking1'),
    url(r'^scheduledServices/confirmWorking/(?P<id>\d+)$',confirmWorking,name='confirmWorking1'),
    url(r'^scheduledServices/completed/(?P<id>\d+)$',completed,name='completed1'),
    url(r'^scheduledServices/neg_feedback/(?P<id>\d+)$',neg_feedback,name='neg_feedback1'),
    url(r'^scheduledServices/pos_feedback/(?P<id>\d+)$',pos_feedback,name='pos_feedback1'),
    url(r'^scheduledServices/cancel/(?P<id>\d+)$',cancel,name='cancel1'),







    
]
