from django.urls import path, include

from . import views

# Place employee related APIs here
employee_urls = [
    path('get_shifts', views.GetAssignedShifts, name='api_shifts'),
    path('get_requested_time_off', views.GetRequestedTimeOff, name='api_requested_time_off'),
    path('get_availability', views.GetAvailability, name='api_get_availability'),
    path('shift_request', views.RequestShift, name='api_request_shift'),
    path('get_open_shifts', views.GetOpenShifts, name='api_open_shifts'),
    path('request_time_off', views.SendTimeOffRequest, name='api_request_time_off'),
    path('toggle_drop_shift', views.ToggleDropShift, name='api_toggle_drop_shift')
]

# Place manager related APIs here
manager_urls = [
    path('test', views.TestManagerRole, name='api_test_manager'),
    path('get_all_shifts', views.GetValidShifts, name='api_all_shifts'),
    path('create_shift', views.CreateNewShift, name='api_create_shift'),
    path('get_employees', views.GetValidEmployees, name='api_get_employees'),
    path('get_shift_requests', views.GetUnapprovedShiftRequests, name='api_get_shift_requests'),
    path('approve_shift_request', views.ApproveShiftRequest, name='api_approve_shift_request'),
    path('get_time_off_requests', views.GetUnapprovedTimeOff, name='api_time_off_requests'),
    path('approve_time_off', views.ApproveTimeOff, name='api_approve_time_off'),
    path('update_shift', views.UpdateShift, name='api_update_shift'),
]

urlpatterns = [
    path('employee/', include(employee_urls)),
    path('manager/', include(manager_urls)),

    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]