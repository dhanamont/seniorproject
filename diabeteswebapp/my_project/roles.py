from rolepermissions.roles import AbstractUserRole

class Doctor(AbstractUserRole):
    available_permissions = {
        'view_result_detail': True,
        'view_notification': True,
        'specify_features': False,
        'view_summary_features': False,
        'select_model': False,
        'edit_model': False,
        'add_patient_data': False,
        'view_summary_added_data': False,
    }

class Icnurse(AbstractUserRole):
    available_permissions = {
        'specify_features': True,
        'view_summary_features': True,
        'select_model': True,
        'edit_model': True,
        'view_result_detail': True,
        'add_patient_data': True,
        'view_summary_added_data': True,
        'view_notification': True,
        'view_model_metadata': False
    }

class Datasci(AbstractUserRole):
    available_permissions = {
    	'view_result_detail': True,
        'view_model_metadata': True,
        'specify_features': False,
        'view_summary_features': False,
        'select_model': False,
        'edit_model': False,
        'add_patient_data': False,
        'view_summary_added_data': False,
        'view_notification': False,
    }