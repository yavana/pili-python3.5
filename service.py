from pili import *









if __name__ == '__main__':
    access_key = ""
    secret_key = ""
    credentials = Credentials(access_key, secret_key)
    client = RoomClient(credentials)
    res = client.roomToken('testRoom','wangliangliang','admin',1785600000000)
    print(res)







