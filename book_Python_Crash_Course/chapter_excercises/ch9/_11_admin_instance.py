"""
Create instances of restaurants.
"""
from _11_user_classes import Admin


admin = Admin("michelle", "domingo", "san francisco")
admin.greet_user()
admin.admin_privilege.show_privileges()
