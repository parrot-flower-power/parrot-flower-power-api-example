Parrot Flower Power Api access guide
====================================

What we provide ?
-----------------

If you are a Parrot Flower Power user, you can already access your data via the iOs free application, or see it in our website: https://myflowerpower.parrot.com.

We also give you access directly to the api if you want to reuse the data.
This api is readonly.


How to use it ?
---------------

### Get your OAuth client_id

First you need to get an OAuth `client_id` and `client_secret`

You can receive it by email by doing a request there:
  https://apiflowerpower.parrot.com/api_access/signup

In case you forget the secret, you can reuse this form to ask it again.


### Authenticate via OAuth 2

With that `client_id` and `client_secret`, and a `username` and `password` you can authenticate to the webservice to get an OAuth token.

### Access your data

With that token, you will be able to access this different read-only api:

 * api-4.02, search for a plant.
 * api-5.01, get PlantDB details for one plant
 * api-5.06, get PlantDB details for many plants.
 * api-1.25, get all the data for your garden
 * api-1.28, get all the statuses for all your garden locations.
 * api-3.05, get all the images url, attached to all your garden locations.
 * api-1.03, get all the samples (every measurement) for a garden locations.


Use our python example to test it
---------------------------------

We have a made a python script to illustrate how to call these api. You can use it like that:

    python test_api.py --client_id YOUR_CLIENT_ID --client_secret YOUR_CLIENT_SECRET --username YOUR_FLOWER_POWER_USERNAME --password YOUR_FLOWER_POWER_PASSWORD

(Change YOUR_CLIENT_ID/SECRET, YOUR_FLOWER_POWER_USERNAME/PASSWORD with the actual values).

And you will find the json response in the directory


Problem ? Something not working ? Need something more ?
-------------------------------------------------------

Please create an issue on github.

Have fun !
