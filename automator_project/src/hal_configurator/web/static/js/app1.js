'use strict';

var app1 = angular.module('myApp1', ['ngRoute']);
app1.config(function($httpProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});

app1.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/HomePage', {
                templateUrl: 'index.html',
                controller: 'HomePageCtrl'
            }).
            when('/NewConfig', {
                templateUrl: 'views/newconfig.html',
                controller: 'ConfigCtrl'
            }).
            when('/EditConfig', {
                templateUrl: 'views/editconfig.html',
                controller: 'EditConfigCtrl'
            }).
            when('/Certificates', {
                templateUrl: 'views/certificates.html',
                controller: 'CertificatesCtrl'
            }).
            otherwise({
                redirectTo: '/HomePage'
            });
    }]);


app1.controller('HomePageCtrl', function($scope) {

});

app1.controller('EditConfigCtrl', function($scope) {

});

app1.controller('CertificatesCtrl', function($scope) {

});