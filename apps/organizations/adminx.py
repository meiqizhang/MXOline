import xadmin
from apps.organizations.models import City
from apps.organizations.models import CourseOrg
from apps.organizations.models import Teacher

# 不用继承admin.ModelAdmin，

class CityAdmin(object):
    pass
xadmin.site.register(City,CityAdmin)

class CourseOrgAdmin(object):
    pass
xadmin.site.register(CourseOrg,CourseOrgAdmin)

class TeacherAdmin(object):
    pass
xadmin.site.register(Teacher,TeacherAdmin)