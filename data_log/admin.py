from django.contrib import admin
from testproject.data_log.models import Log,Single_Main,Main_Testing,Single_Nutrient
from testproject.data_log.models import Micro_Nutrient_Testing,Ammonia_Nitrate
from testproject.data_log.models import Ammonia_Nitrate_Testing

admin.site.register(Log)
admin.site.register(Single_Main)
admin.site.register(Main_Testing)
admin.site.register(Single_Nutrient)
admin.site.register(Micro_Nutrient_Testing)
admin.site.register(Ammonia_Nitrate)
admin.site.register(Ammonia_Nitrate_Testing)
