from .auth import auth_interface
import pili.conf as conf
from urllib.request import Request
import json, base64, hmac

def normalize(args, keyword):
    if set(args) - set(keyword):
        raise ValueError('invalid key')
    # for k, v in args.items():
    #     if v is None:
    #         del args[k]
    temp={}
    for k,v in args.items():
        if not (v is None) :
            temp[k]=v

    args = temp
    return args




@auth_interface
def delete_room(version, roomName):
    url = "http://%s/%s/rooms/%s" % (conf.RTC_API_HOST, version, roomName)
    print(url)
    return Request(url=url,method='DELETE')


@auth_interface
def get_room(version, roomName):
    url = "http://%s/%s/rooms/%s" % (conf.RTC_API_HOST, version, roomName)
    print(url)
    return Request(url=url,method='GET')


@auth_interface
def create_room(ownerId, version, roomName=None):
    params = {'owner_id': ownerId}
    url = "http://%s/%s/rooms" % (conf.RTC_API_HOST, version)
    print(url)
    if bool(roomName):
        params['room_name'] = roomName
    encoded = json.dumps(params)
    return Request(url=url, data=encoded.encode('utf-8'),method='POST')

@auth_interface
def create_stream(**args):
    keyword = ['hub', 'title', 'publishKey', 'publishSecurity']
    encoded = json.dumps(normalize(args, keyword))
    url = "http://%s/%s/streams" % (conf.API_HOST, conf.API_VERSION)
    return Request(url=url, data=encoded.encode('utf-8'))

@auth_interface
def get_stream(stream_id):
    url = "http://%s/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, stream_id)
    return Request(url=url)

@auth_interface
def get_stream_list(**args):
    keyword = ['liveonly', 'marker', 'limit', 'prefix','hub']

    args = normalize(args, keyword)
    hub = ''
    if args.get('hub'):
        hub = args.get('hub')

    if args.get('idonly'):
        if args['idonly'] is not True:
            del args['idonly']
    url = "http://%s/%s/hubs/%s/streams?" % (conf.API_HOST, conf.API_VERSION, hub)
    for k, v in args.items():
        url += "&%s=%s" % (k, v)
    req = Request(url=url)
    return req

@auth_interface
def update_stream(stream_id, **args):
    keyword = ['publishKey', 'publishSecurity', 'disabled']
    encoded = json.dumps(normalize(args, keyword))
    url = "http://%s/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, stream_id)
    return Request(url=url, data=encoded.encode('utf-8'))

@auth_interface
def delete_stream(stream_id):
    url = "http://%s/%s/streams/%s" % (conf.API_HOST, conf.API_VERSION, stream_id)
    req = Request(url=url)
    req.get_method = lambda: 'DELETE'
    return req

@auth_interface
def get_status(stream_id):
    url = "http://%s/%s/streams/%s/status" % (conf.API_HOST, conf.API_VERSION, stream_id)
    return Request(url=url)

@auth_interface
def get_segments(stream_id, start_second=None, end_second=None, limit=None):
    url = "http://%s/%s/streams/%s/segments" % (conf.API_HOST, conf.API_VERSION, stream_id)
    if start_second and end_second:
        url += "?start=%s&end=%s" % (start_second, end_second)
    if limit != None:
        url += "&limit=%s" % (limit)
    return Request(url=url)

@auth_interface
def save_stream_as(stream_id, **args):
    keyword = ['name', 'notifyUrl', 'start', 'end', 'format', 'pipeline']
    encoded = json.dumps(normalize(args, keyword))
    url = "http://%s/%s/streams/%s/saveas" % (conf.API_HOST, conf.API_VERSION, stream_id)
    return Request(url=url, data=encoded.encode('utf-8'))

@auth_interface
def snapshot_stream(stream_id, **args):
    '''
    POST /v2/hubs/<Hub>/streams/<EncodedStreamTitle>/snapshot
Host: pili.qiniuapi.com
Authorization: <QiniuToken>
Content-Type: application/json
{
    "fname": "<Fname>",
    "time": <Time>,
    "format": "<Format>",
    "deleteAfterDays": <DeleteAfterDays>
}
    :param stream_id:
    :param args:
    :return:
    '''
    keyword = ['fname', 'format', 'time', 'DeleteAfterDays','hub_name']
    encoded = json.dumps(normalize(args, keyword))
    hub_name = ''
    if args.get('hub_name'):
        hub_name = args.get('hub_name')
    #url = "http://%s/%s/hubs/%s/streams/%s/snapshot" % (conf.API_HOST, conf.API_VERSION, 'futurearriving','ZGVtb18zOV84N19BQUZUeFFWYmhTb0RBUDBVMnlqRDhWdUI=')
    url = "http://%s/%s/hubs/%s/streams/%s/snapshot" % (conf.API_HOST, conf.API_VERSION, hub_name, str(base64.urlsafe_b64encode(stream_id.encode('utf8')),'utf8'))
    return Request(url=url, data=encoded.encode('utf-8'))
