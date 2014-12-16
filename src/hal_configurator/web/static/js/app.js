'use strict';

var app = angular.module('myApp', ['ngRoute', 'ngCookies', 'blueimp.fileupload']);
app.config(['$httpProvider', '$routeProvider', 'fileUploadProvider', 
    function($httpProvider, $routeProvider, fileUploadProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    fileUploadProvider.defaults.redirect = '/config/:appname/:platform';
    $routeProvider.
        when('/config/:appname/:platform', {
            templateUrl: 'new_config.html',
            controller: 'ConfigCtrl'
        })
        .when('/config/:appname', {
            templateUrl: 'new_config.html',
            controller: 'ConfigCtrl'
        });
}]);