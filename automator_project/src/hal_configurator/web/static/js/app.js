'use strict';

var app = angular.module('myApp', ['ngRoute']);

app.config(function($httpProvider, $routeProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
    $routeProvider.
        when('/HomePage', {
            templateUrl: 'homepage.html',
            controller: 'HomePageCtrl'
        }).
        when('/NewConfig', {
            templateUrl: 'newconfig.html',
            controller: 'ConfigCtrl'
        }).
        when('/EditConfig', {
            templateUrl: 'editconfig.html',
            controller: 'EditConfigCtrl'
        }).
        when('/Certificates', {
            templateUrl: 'certificates.html',
            controller: 'CertificatesCtrl'
        });
});


app.controller('EditConfigCtrl', function($scope) {
    $scope.message = "EditConfigCtrl";
});


app.controller('HomePageCtrl', function($scope) {
    $scope.message = "HomePageCtrl";
});

app.controller('CertificatesCtrl', function($scope) {
    $scope.message = "CertificatesCtrl";
});

app.controller('ConfigCtrl', function($scope, $log, configSvc){
    $scope.config = {};
    $scope.configuraitons = [];
    $scope.configId = 'FloridaDesign';
    $scope.platform = 'IOS';
    $scope.platforms = ['IOS', 'Android'];
    var refreshConfig = function(){
        configSvc.get($scope.configId, $scope.platform, function(conf){
            $scope.config = conf;
        });
    };
    //refreshConfig();
    configSvc.index(function(result){
        $scope.configurations =  _.union(['-- Select Item --'], result);
    });

    $scope.reloadConfig = function(configId){
        $scope.configId = configId;
        refreshConfig();
    };
    $scope.reloadPlatform = function(platform){
        $scope.platform = platform;
        refreshConfig();
    };
    $scope.saveConfig = function() {
        configSvc.save($scope.configId, $scope.platform, $scope.config, function(validationResult){
            if(validationResult && validationResult.errors){
                alert(validationResult.errors);
            }
        });
    };
});