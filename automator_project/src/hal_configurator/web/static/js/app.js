'use strict';

var app = angular.module('myApp', ['ngRoute']).config(function($httpProvider, $routeProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    $routeProvider.
        when('/HomePage', {
            templateUrl: 'homepage.html',
            controller: 'HomePageCtrl'
        }).
        when('/NewConfig', {
            templateUrl: 'new_config.html',
            controller: 'ConfigCtrl'
        }).
        when('/EditConfig', {
            templateUrl: 'edit_config.html',
            controller: 'EditConfigCtrl'
        }).
        when('/CertificatesAndResources', {
            templateUrl: 'certificates_resources.html',
            controller: 'CertificatesResourcesCtrl'
        });
});