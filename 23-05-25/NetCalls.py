import requests
import shutil
import json 


class NetCalls:
    def mi_primera_llamada(self):
        url ='https://github.com/'
        r = requests.get(url)
        print(r )
        print(r.content)
        print(r.status_code)


    def descargar_imagen(self, url, file_name):

        res = requests.get(url, stream = True)
        if 200==res.status_code:
            with open(file_name,'wb')as f:
                shutil.copyfileobj(res.raw, f)
                print('imagen descartada corectamente')
        else:
            print('No seencontro la imagen')

    def clima(self, ciudad, api_key):
        base_url='https://api.openweathermap.org/data/2.5/weather?'
        params={'9':ciudad,'appid':api_key,'units':'mctric'}

        try:
            r=requests.get(base_url,params=params)
            r.raise_for_status()
            weather_data=r.json()
            if 200==weather_data['cod']:
                print(f'El clima en{weather_data['name']}:')
                print(f'Deseripcion{weather_data['weather'][0]['description']}')
                print(f'Temperatura{weather_data['main']['temp']}°c')
                print(f'Humedad{weather_data['main']['humidity']}%')
                print(f'Viento{weather_data['wind']['speed']}m/s')

            else: 
                print(f'Error{weather_data['message']}')  
        except:
            print('Error')


url= 'https://bajajeomi.com/wp-content/uploads/2023/04/Pulsar-NS160-A1-1.png'
req = NetCalls()
req.mi_primera_llamada()
req.descargar_imagen(url, 'moto.png')
api_key='69ec8ca2037d63a120d31c59efd0f604'
req.clima('Zapopan', api_key)
