from datetime import datetime
ahora = datetime.now()
print(ahora.year)
print(ahora.strftime("%A"))
fecha = datetime(2025 ,10 , 4)
print(fecha.strftime("%B"))
str_fecha ="23/09/09 14:58:00"
fecha_obj = datetime.strftime(str_fecha,'%d/%m/%y %H:%M:%S')
print(ahora - fecha_obj)