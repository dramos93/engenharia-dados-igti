import json
from tweepy import OAuthHandler, Stream, StreamListener
from datetime import datetime

# cadastrar as chaves de acesso


#Definir um arquivo de saída para armazenar os tweets coletados
data_hoje = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
out = open(f"collected_tweets_{data_hoje}.txt", "w")

# Implementar uma classe para conexão com o twitter
class MyListener(StreamListener):
    
    def on_data(self, data):
        #print(data)
        itemString = json.dumps(data)
        out.write(itemString + "\n")
        return True

    def on_error(self,status):
        print(status)

# Implementar nossa Função Main
if __name__ == "__main__":
    l = MyListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track =["Trump"])



#Project:
#bootcamp-daniel-001

#API key:
#6vB9vPXZ1bsMMMXwnfXIHCwH6

#API key secret:
#qxlUBZBwK5XINoDoLqlH8pSkOs3ivqn3GpzCWxM5f3oAjap6Kk
#
#Bearer token:
#AAAAAAAAAAAAAAAAAAAAAEYwKAEAAAAAaHnKPE%2FegxIX%2BANR5P%2BNwrPMgL0%3D3yk6YwgEOa0OGVD205D76r028QQhRah9bXJ9b4jKNssdHkA1Ys

#Access token:
#929345820452904960-89TtDub2Aqe7p74gzQDEzoSWT4Bhpil

#Access token secret:
#kVji0G3dWbM5OZnfDGKWZ6y5bQaUHhZ1XjuLH46XNWuSw