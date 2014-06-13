Parrot Flower Power Api access guide
====================================

What do we provide ?
--------------------

If you are a Parrot Flower Power user, you can already access your data via the iOs free application, or see it in our website: https://myflowerpower.parrot.com.

We also give you access directly to the api if you want to reuse the data.
This api is readonly.

How to start ?
--------------

You can find documentation and quickstarts on the web API here:
    https://flowerpowerdev.parrot.com/projects/flower-power-web-service-api/wiki


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

With that token, you will be able to access different read-only api, see documentation for that


Problem ? Something not working ? Need something more ?
-------------------------------------------------------

Please create an issue on github or on the forum:
    https://flowerpowerdev.parrot.com/projects/flower-power-web-service-api/boards

Have fun !
