#!/usr/bin/env python

import argparse
import datetime
import urllib, urllib2, os
import json


parser = argparse.ArgumentParser(prog='test_api',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--client_id',required=True)
parser.add_argument('--client_secret',required=True)
parser.add_argument('--username',required=True)
parser.add_argument('--password',required=True)

args = parser.parse_args()

if not os.path.exists('json'):   os.makedirs('json')

basename = "https://apiflowerpower.parrot.com"

client_id = args.client_id
client_secret = args.client_secret
username = args.username
password = args.password


oauth_bearer = {}

def URLRequest(url, params, method="GET", headers={}):
    if method == "POST":
        return urllib2.Request(url, headers=headers, data=urllib.urlencode(params))
    else:
        return urllib2.Request(url + "?" + urllib.urlencode(params),headers=headers)


def api_json(url, params, method='GET', headers={}):
    request = URLRequest(basename+url, params, method, headers=headers)
    request.add_header('Accept-Language', 'en_us')
    result = urllib2.urlopen(request)

    # print url
    # print "status", result.getcode()
    # print result.headers

    result_string = result.read()
    return json.loads(result_string)


def test_api_and_dump_to_json(key, url):
    json_data = api_json(url, {}, headers=oauth_bearer, method='GET')
    dump = json.dumps(json_data, indent=4, sort_keys=True)
    
    dirname = "json/" + username
    if not os.path.exists(dirname):   os.makedirs(dirname)
    
    
    out = open( dirname + "/" + key+'.json','w')
    out.write(dump)
    out.close()
    return json_data
    

# first get OAuth token
result = api_json('/user/v1/authenticate', {'grant_type':'password','client_id':client_id,'client_secret':client_secret,'username':username, 'password':password}, method='POST')
access_token = result['access_token']

oauth_bearer = {'Authorization':'Bearer '+access_token}

# some generic search in the PlantDB
for key,url in (
    ('api-4.02-search-rosa','/search/v5/plants/rosa?generate_index=ASC'),
    ('api-5.01-plants','/plant_library/v1/plant/6677'),
    ('api-5.06-plants','/plant_library/v1/plants/6677,146,405,5671,7548,3461,3462,2394,6003,710'),
):
    print key
    test_api_and_dump_to_json(key,url)

# user data : sync (garden_locations and sensors) and statuses.
for key,url in (
    ('api-1.25-sync','/sensor_data/v2/sync?include_s3_urls=1'),
    ('api-1.28-status','/sensor_data/v1/garden_locations_status'),
    ('api-3.05-images','/image/v2/location/user_images'),
):
    print key
    test_api_and_dump_to_json(key,url)


# get last week samples for each garden_locations.
sync_message = api_json('/sensor_data/v2/sync?include_s3_urls=1', {}, headers=oauth_bearer, method='GET')
for location in sync_message['locations']:
    location_identifier = location['location_identifier']
    print location_identifier
    last_sample_utc_string = location["last_sample_utc"]
    if last_sample_utc_string:
        last_sample_utc = datetime.datetime.strptime(last_sample_utc_string,'%Y-%m-%d %H:%M:%S UTC')
        from_datetime_utc = (last_sample_utc - datetime.timedelta(days=7)).strftime("%Y-%m-%dT%H:%M:%SZ")
        to_datetime_utc   = last_sample_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
        url = '/sensor_data/v2/sample/location/' + location_identifier + '?from_datetime_utc=' + from_datetime_utc + '&to_datetime_utc=' + to_datetime_utc
        print url
        test_api_and_dump_to_json('api-1.03-samples-'+location_identifier, url)

    