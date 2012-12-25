===========================
Printstand Prebuild utility
===========================

Description
===========

 This utility is used for creating custom builds for the Printsand Client applications
 It uses the configuration service or local file system to setup the projects with custom resources
 the location where the resources are build is :: 
 
   /tmp/Mediawire/${PublisherName}/${PlatformName}

Installation 
============
  
  Navigate to the source dir and type ::

    sudo make install                 

Usage
=====
           
  go into the MonoDroid or Monotouch project root directory and type ::
  
    prinstand_prebuild platform=ios publisher=florida_design
  
  this will generate a new custom solution in ::
  
    /tmp/Mediawire/florida_design/ios
  
  you can build this solution then in Mono or you can use the command line utility ::
  
    make build
    
    
Tests for Services Used
=======================

  Generated On: ::  2012-07-30

get configs
===========

http://staging.halicea.com

Request
+++++++

  Selector: /svc/branded_apps/config

  Method: GET

  Data: 

  Headers: ::

    {}

Response:
+++++++++

  Status: 200

  Headers: ::

    {'content-length': '355', 'x-powered-by': 'Express', 'date': 'Mon, 30 Jul 2012 11:52:53 GMT', 'set-cookie': 'mwr.sid=f09bf3TS8ukmEs723NUpnoyB.pHrJXaMSrEcYqzofdpnyUV6jCefnpL2lVQm%2B3D08dNw; path=/; expires=Mon, 30 Jul 2012 15:52:53 GMT; httpOnly', 'content-type': 'application/json; charset=utf-8', 'connection': 'keep-alive', 'server': 'nginx/1.0.14'}

  Response Content:  ::

     {"status":"ok","data":[{"Publisher":"5013cca53b7133873e000001","Platform":"501462fed95db3a74a000005","Authentication":"5013dbbf6a4dbf5744000001","ApplicationType":"5013dbfa6a4dbf5744000006","_id":"501663bc01b5e94e72000009","PrebuildResources":[{"type":"5015e1a7f8d8c54964000010","url":"/branded_apps/501663bc01b5e94e72000009/5015e1a7f8d8c54964000010"}]}]}


get publishers
==============

http://staging.halicea.com

Request
+++++++

  Selector: /svc/branded_apps/publishers

  Method: GET

  Data: 

  Headers: ::

    {}

Response:
+++++++++

  Status: 200

  Headers: ::

    {'content-length': '189', 'x-powered-by': 'Express', 'date': 'Mon, 30 Jul 2012 11:52:53 GMT', 'set-cookie': 'mwr.sid=ec2EbqOvT0XwNPunjhVsQrNW.aVcgDtUDZg0cLgCKrS2QnsGBxhVKaAG9Vr4r6sixXrk; path=/; expires=Mon, 30 Jul 2012 15:52:53 GMT; httpOnly', 'content-type': 'application/json; charset=utf-8', 'connection': 'keep-alive', 'server': 'nginx/1.0.14'}

  Response Content:  ::

     {"status":"ok","data":[{"Name":"Florida Design","_id":"5013cca53b7133873e000001"},{"Name":"Mediawire","_id":"50145c91d95db3a74a000004"},{"Name":"Halicea","_id":"50147b458448e8c053000007"}]}


get platforms
=============

http://staging.halicea.com

Request
+++++++

  Selector: /svc/branded_apps/platforms

  Method: GET

  Data: 

  Headers: ::

    {}

Response:
+++++++++

  Status: 200

  Headers: ::

    {'content-length': '124', 'x-powered-by': 'Express', 'date': 'Mon, 30 Jul 2012 11:52:53 GMT', 'set-cookie': 'mwr.sid=C3uQTJAnhmWEz59lnerE1D03.PNhutuNFSHkMDlxwnHD%2FryHnMwfVhWe%2FFvYbJ5qZ6gI; path=/; expires=Mon, 30 Jul 2012 15:52:53 GMT; httpOnly', 'content-type': 'application/json; charset=utf-8', 'connection': 'keep-alive', 'server': 'nginx/1.0.14'}

  Response Content:  ::

     {"status":"ok","data":[{"Name":"IOS","_id":"5013d3abac1ae36141000003"},{"Name":"Android","_id":"501462fed95db3a74a000005"}]}


get resource types
==================

http://staging.halicea.com

Request
+++++++

  Selector: /svc/branded_apps/resource_types

  Method: GET

  Data: 

  Headers: ::

    {}

Response:
+++++++++

  Status: 200

  Headers: ::

    {'content-length': '1039', 'x-powered-by': 'Express', 'date': 'Mon, 30 Jul 2012 11:52:53 GMT', 'set-cookie': 'mwr.sid=e3erpdekEQQZc4jYDGlmbh4e.HLySFs769IaXGV2pZhfQ%2FQtYJukcqTRrEVZm%2FB8Soj4; path=/; expires=Mon, 30 Jul 2012 15:52:53 GMT; httpOnly', 'content-type': 'application/json; charset=utf-8', 'connection': 'keep-alive', 'server': 'nginx/1.0.14'}

  Response Content:  ::

     {"status":"ok","data":[{"Platform":"501462fed95db3a74a000005","Name":"Splash Screen","Destination":"Resources/Drawable/splash18.jpg","_id":"5015e0b7f8d8c5496400000f"},{"Platform":"501462fed95db3a74a000005","Name":"icon-ldpi","Destination":"Resources/drawable-ldpi/Icon.png","_id":"5015e1a7f8d8c54964000010"},{"Platform":"501462fed95db3a74a000005","Name":"icon-ndpi","Destination":"Resources/drawable-ndpi/Icon.png","_id":"5015e1b4f8d8c54964000011"},{"Platform":"501462fed95db3a74a000005","Name":"icon-xhdpi","Destination":"Resources/drawable-xhdpi/Icon.png","_id":"5015e1c7f8d8c54964000012"},{"Platform":"501462fed95db3a74a000005","Name":"icon-hdpi","Destination":"Resources/drawable-hdpi/Icon.png","_id":"5015e1e2f8d8c54964000013"},{"Platform":"501462fed95db3a74a000005","Name":"MDWLogo-hdpi","Destination":"Resources/drawable-hdpi/MDW_logo.png","_id":"5015e345f8d8c54964000014"},{"Platform":"501462fed95db3a74a000005","Name":"background","Destination":"Resources/Drawable/background_ipad_portrait.png","_id":"5015e3fdf8d8c54964000015"}]}


get authentication types
========================

http://staging.halicea.com

Request
+++++++

  Selector: /svc/branded_apps/authentication_types

  Method: GET

  Data: 

  Headers: ::

    {}

Response:
+++++++++

  Status: 200

  Headers: ::

    {'content-length': '186', 'x-powered-by': 'Express', 'date': 'Mon, 30 Jul 2012 11:52:53 GMT', 'set-cookie': 'mwr.sid=5bDeSCVteAiFC8f0pX4GRYBq.QAQP8Z397JrITJrXERyH%2Br3btdbd3OHkN2Hu2CvN5u0; path=/; expires=Mon, 30 Jul 2012 15:52:53 GMT; httpOnly', 'content-type': 'application/json; charset=utf-8', 'connection': 'keep-alive', 'server': 'nginx/1.0.14'}

  Response Content:  ::

     {"status":"ok","data":[{"Name":"Auto Login","_id":"5013dbbf6a4dbf5744000001"},{"Name":"Mediawire","_id":"5013dbc56a4dbf5744000002"},{"Name":"Facebook","_id":"5013dbc96a4dbf5744000003"}]}


get application types
=====================

http://staging.halicea.com

Request
+++++++

  Selector: /svc/branded_apps/application_types

  Method: GET

  Data: 

  Headers: ::

    {}

Response:
+++++++++

  Status: 200

  Headers: ::

    {'content-length': '196', 'x-powered-by': 'Express', 'date': 'Mon, 30 Jul 2012 11:52:54 GMT', 'set-cookie': 'mwr.sid=JYAjoO42iXPl2eGjrKiLjSVu.ZhHMlFP4Gav5c3GDTmVBy5XskIdJurBwcH%2FtoCYYD%2BE; path=/; expires=Mon, 30 Jul 2012 15:52:54 GMT; httpOnly', 'content-type': 'application/json; charset=utf-8', 'connection': 'keep-alive', 'server': 'nginx/1.0.14'}

  Response Content:  ::

     {"status":"ok","data":[{"Name":"Full-Mediawire","_id":"5013dbed6a4dbf5744000004"},{"Name":"Single Title","_id":"5013dbf46a4dbf5744000005"},{"Name":"Multi Title","_id":"5013dbfa6a4dbf5744000006"}]}
  
  
   