'use strict';

var app = angular.module('myApp', ['ngRoute', 'ngCookies']);
app.config(function($httpProvider, $routeProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    $routeProvider.
        when('/config/:appname/:platform', {
            templateUrl: 'new_config.html',
            controller: 'ConfigCtrl'
        })
        .when('/config/:appname', {
            templateUrl: 'new_config.html',
            controller: 'ConfigCtrl'
        });
});