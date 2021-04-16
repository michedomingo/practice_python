"""
Create instances of restaurants.
"""
from _12_admin_privileges import Admin


admin = Admin("michelle", "domingo", "san francisco")
admin.greet_user()
admin.admin_privilege.show_privileges()
