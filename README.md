# Pili Streaming Cloud server-side library for Python

## Features

- Stream Create,Get,List
    - [x] hub.create_stream()
    - [x] hub.get_stream()
    - [x] hub.list_streams()
- Stream operations else
    - [x] stream.to_json()
    - [x] stream.update()
    - [x] stream.disable()
    - [x] stream.enable()
    - [x] stream.rtmp_publish_url()
    - [x] stream.rtmp_live_urls()
    - [x] stream.hls_live_urls()
    - [x] stream.http_flv_live_urls()
    - [x] stream.status()
    - [x] stream.segments()
    - [x] stream.hls_playback_urls()
    - [x] stream.snapshot()
    - [x] stream.save_as()
    - [x] stream.delete()


## Contents

- [Installation](#installation)
- [Usage](#usage)
    - [Configuration](#configuration)
    - [Hub](#hub)
        - [Instantiate a Pili Hub object](#instantiate-a-pili-hub-object)
        - [Create a new Stream](#create-a-new-stream)
        - [Get a Stream](#get-a-stream)
        - [List Streams](#List-streams)
    - [Stream](#stream)
        - [To JSON string](#to-json-string)
        - [Update a Stream](#update-a-stream)
        - [Disable a Stream](#disable-a-stream)
        - [Enable a Stream](#enable-a-stream)
        - [Generate RTMP publish URL](#generate-rtmp-publish-url)
        - [Generate RTMP live play URLs](#generate-rtmp-live-play-urls)
        - [Generate HLS live play URLs](generate-hls-live-play-urls)
        - [Generate Http-Flv live play URLs](generate-http-flv-live-play-urls)
        - [Get Stream status](#get-stream-status)
        - [Get Stream segments](#get-stream-segments)
        - [Generate HLS playback URLs](generate-hls-playback-urls)
        - [Save Stream as a file](#save-stream-as-a-file)
        - [Snapshot Stream](#snapshot-stream)
        - [Delete a Stream](#delete-a-stream)
- [History](#history)


## Installation

```shell
 python3 setup.py build
 python3 setup.py install
```

## Usage:

### Configuration

```python
from pili import *

access_key = 'qiniu_access_key'
secret_key = 'qiniu_secret_key'

hub_name   = 'pili_hub_name' # The Hub must be exists before use

# Change API host as necessary
#
# pili.qiniuapi.com as default
# pili-lte.qiniuapi.com is the latest RC version
#
# conf.API_HOST = 'pili.qiniuapi.com' # default
```

### Hub

#### Instantiate a Pili Hub object

```python
credentials = Credentials(access_key, secret_key)
hub = Hub(credentials, hub_name)
```

#### Create a new Stream

```python
# title          : optional, string, auto-generated as default
# publishKey     : optional, string, auto-generated as default
# publishSecrity : optional, string, can be "dynamic" or "static", "dynamic" as default
stream = hub.create_stream(title=None, publishKey=None, publishSecurity="static")
# return stream object...
print "\ncreate_stream()\n", stream.to_json()
# {
#   "publishSecurity": "dynamic",
#   "hub": "test-origin",
#   "title": "55db4a9ee3ba573b20000004",
#   "publishKey": "976655fbf3bee71e",
#   "disabled": false,
#   "hosts": {
#     "live": {
#       "http": "e4kvkh.live1-http.z1.pili.qiniucdn.com",
#       "rtmp": "e4kvkh.live1-rtmp.z1.pili.qiniucdn.com"
#     },
#     "playback": {
#       "http": "e4kvkh.playback1.z1.pili.qiniucdn.com"
#     },
#     "publish": {
#       "rtmp": "e4kvkh.publish.z1.pili.qiniup.com"
#     }
#   },
#   "updatedAt": "2015-08-24T16:47:26.786Z",
#   "id": "z1.test-origin.55db4a9ee3ba573b20000004",
#   "createdAt": "2015-08-24T16:47:26.786Z"
# }
```

#### Get a Stream

```python
# stream_id: required, string
stream = hub.get_stream(stream_id=id)
# return stream object...
print "\nget_stream()\n", stream
# <pili.stream.Stream object at 0x106365490>
```

#### List Streams

```python
# marker : optional, string
# limit  : optional, int
# title  : optional, string
# status : optional, string, the only acceptable value is "connected"
# idonly : optional, bool
res = hub.list_streams(marker=None, limit=10, title="prefix_")
for s in res["items"]:
    # s is stream object...
    # Do someting...
    pass
next = hub.list_streams(marker=res["marker"])
print "\nlist_streams()\n", res
# {
#   "marker": "10",
#   "items": [
#     <pili.stream.Stream object at 0x106365490>,
#     <pili.stream.Stream object at 0x1063654d0>,
#     <pili.stream.Stream object at 0x106365510>,
#     <pili.stream.Stream object at 0x106365550>,
#     <pili.stream.Stream object at 0x106365590>,
#     <pili.stream.Stream object at 0x1063655d0>,
#     <pili.stream.Stream object at 0x106365610>,
#     <pili.stream.Stream object at 0x106365650>,
#     <pili.stream.Stream object at 0x106365690>,
#     <pili.stream.Stream object at 0x1063656d0>
#   ]
# }
```

### Stream

#### To JSON string

```python
print stream.to_json()
# {
#   "publishSecurity":"static",
#   "hub":"test-origin",
#   "title":"55db4ecae3ba573b20000006",
#   "publishKey":"new_secret_words",
#   "disabled":false,
#   "hosts":{
#     "live":{
#       "http":"e4kvkh.live1-http.z1.pili.qiniucdn.com",
#       "rtmp":"e4kvkh.live1-rtmp.z1.pili.qiniucdn.com"
#     },
#     "playback":{
#       "http":"e4kvkh.playback1.z1.pili.qiniucdn.com"
#     },
#     "publish":{
#       "rtmp":"e4kvkh.publish.z1.pili.qiniup.com"
#     }
#   },
#   "updatedAt":"2015-08-24T13:05:15.272975102-04:00",
#   "id":"z1.test-origin.55db4ecae3ba573b20000006",
#   "createdAt":"2015-08-24T13:05:14.526-04:00"
# }
```

#### Update a Stream

```python
# publishKey     : optional, string
# publishSecrity : optional, string
# disabled       : optional, bool
stream.update(publishKey = "new_secret_words", publishSecurity="dynamic")
```

#### Disable a Stream

```python
stream.disable()
```

#### Enable a Stream

```python
stream.enable()
```

#### Generate RTMP publish URL

```python
url = stream.rtmp_publish_url()
print url
# rtmp://e4kvkh.publish.z1.pili.qiniup.com/test-origin/55db52e1e3ba573b2000000e?key=new_secret_words
```

#### Generate RTMP live play URLs

```python
urls = stream.rtmp_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original RTMP live url
original_url = urls["ORIGIN"]
# {"ORIGIN": "rtmp://e4kvkh.live1-rtmp.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e"}
```

#### Generate HLS play live URLs

```python
urls = stream.hls_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original HLS live url
original_url = urls["ORIGIN"]
# {"ORIGIN": "http://e4kvkh.live1-http.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e.m3u8"}
```

#### Generate Http-Flv live play URLs

```python
urls = stream.http_flv_live_urls()
for k in urls:
    print k, ":", urls[k]

# Get original Http-Flv live url
original_url = urls["ORIGIN"]
# {"ORIGIN": "http://e4kvkh.live1-http.z1.pili.qiniucdn.com/test-origin/55db52e1e3ba573b2000000e.flv"}
```

#### Get Stream status

```python
status = stream.status()
print status
# {
#     "addr": "222.73.202.226:2572",
#     "status": "connected",
#     "bytesPerSecond": 16870.200000000001,
#     "framesPerSecond": {
#         "audio": 42.200000000000003,
#         "video": 14.733333333333333,
#         "data": 0.066666666666666666,
#     }
# }
```

#### Get Stream segments

```python
# start_second : optional, int64, in second, unix timestamp
# end_second   : optional, int64, in second, unix timestamp
# limit        : optional, uint32
# ...but you must provide both or none of the arguments.
segments = stream.segments(start_second=None, end_second=None, limit=None)
print segments
# [
#     {
#         "start": 1440282134,
#         "end": 1440437833
#     },
#     {
#         "start": 1440437981,
#         "end": 1440438835
#     },
#     ...
# ]
```

#### Generate HLS playback URLs

```python
# start : required, int64, in second, unix timestamp
# end   : required, int64, in second, unix timestamp
urls = stream.hls_playback_urls(start, end)
for k in urls:
    print k, ":", urls[k]

# Get original HLS playback url
original_url = urls["ORIGIN"]
```

#### Save Stream as a file

```python
# name      : required, string
# start     : required, int64, in second, unix timestamp
# end       : required, int64, in second, unix timestamp
# format    : optional, string, see http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# notifyUrl : optional, string
# pipeline  : optional, string
res = stream.save_as(name="videoName.mp4", format="mp4", start=1440282134, end=1440437833, notifyUrl=None)
print res
# {
#     "url": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-hub.55d81a72e3ba5723280000ec/videoName.m3u8",
#     "targetUrl": "http://ey636h.vod1.z1.pili.qiniucdn.com/recordings/z1.test-hub.55d81a72e3ba5723280000ec/videoName.mp4",
#     "persistentId": "z1.55d81c6c7823de5a49ad77b3"
# }
```

#### Snapshot stream

```python
# name      : required, string
# format    : required, string see http://developer.qiniu.com/docs/v6/api/reference/fop/av/avthumb.html
# time      : optional, int64, in second, unix timestamp
# notifyUrl : optional, string
res = stream.snapshot(name="imageName.jpg", format="jpg", time=None, notifyUrl=None)
print res
# {
#     "targetUrl": "http://ey636h.static1.z1.pili.qiniucdn.com/snapshots/z1.test-hub.55d81a72e3ba5723280000ec/imageName.jpg",
#     "persistentId": "z1.55d81c247823de5a49ad729c"
# }
```

While invoking `saveAs()` and `snapshot()`, you can get processing state via Qiniu FOP Service using `persistentId`.  
API: `curl -D GET http://api.qiniu.com/status/get/prefop?id={PersistentId}`  
Doc reference: <http://developer.qiniu.com/docs/v6/api/overview/fop/persistent-fop.html#pfop-status>  

#### Delete a stream

```python
stream.delete()
```

## History

- 1.5.8
    - Add pipeline in saveAs
- 1.5.7
    - Use save_as in hls_playback_urls
- 1.5.0
    - Update Stream Create,Get,List
        - hub.create_stream()
        - hub.get_stream()
        - hub.list_streams()
    - Add Stream operations else
        - stream.to_json()
        - stream.update()
        - stream.disable()
        - stream.enable()
        - stream.rtmp_publish_url()
        - stream.rtmp_live_urls()
        - stream.hls_live_urls()
        - stream.http_flv_live_urls()
        - stream.status()
        - stream.segments()
        - stream.hls_playback_urls()
        - stream.snapshot()
        - stream.save_as()
        - stream.delete()
