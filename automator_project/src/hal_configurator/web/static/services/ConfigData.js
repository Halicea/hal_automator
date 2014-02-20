'use strict';
var app = angular.module('myApp', []);
myApp.factory('ConfigData', function(){
	app.controller('ConfigCtrl', function($scope, $http, $log){
    $scope.config = {};
    $scope.configuraitons = [];
    $scope.configId = 'FloridaDesign';
    $scope.platform = 'IOS';

        $http.get('/config').success(function(data){
            $scope.configurations=['--Select Configuration--'];
            $scope.configurations = _.union($scope.configurations, data);
            $scope.reloadConfig($scope.configId);
        }).error(function(status, headers, response, config){
            $log.warn(status, headers, response, config);
            $scope.config = null;
        });
        $scope.reloadConfig = function(configId){
            $http.get('/config/'+configId+'/'+$scope.platform+'/bc.json'
                ).success(function(data, status) {
                $scope.config = data;
            }).error(function(status, headers, response, config){
                $scope.config = null;
                $log.warn(status, headers, response, config);
            });
        };
        $scope.reloadPlatform = function(platform){
            $http.get('/config/'+$scope.configId+'/'+$scope.platform+'/bc.json'
                ).success(function(data, status) {
                $scope.config = data;
            }).error(function(status, headers, response, config){
                $scope.config = null;
                $log.warn(status, headers, response, config);
            });
        };
        $scope.saveConfig = function() {
            $http.post('/config/'+$scope.configId+'/'+$scope.platform+'/bc.json', $scope.config).success(function(data){
                alert(data);
            }).error(function(status, headers, response, cnf){
                    $log.warn(status, headers, response, cnf);
                    alert(status);
            });
        };
    });
});