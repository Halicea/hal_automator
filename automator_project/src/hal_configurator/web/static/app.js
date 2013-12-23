 // var mockDataForThisTest = "json=" + encodeURI(JSON.stringify('bc.json'));
'use strict';

var app = angular.module('myApp', []);
app.config(function($httpProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});
// Application Identifier doesn't need to show
app.controller('ConfigCtrl', function($scope, $http, $log){
    $scope.config = {};
    $scope.configuraitons = [];
    $scope.configId = 'FloridaDesign';
    $scope.platform = 'IOS';
    $http.get('/config').success(function(data){
        $scope.configurations = data;
    }).error(function(status, headers, response, config){
        $log.warn(status, headers, response, config);
    });
    $scope.reloadConfig = function(configId){
        $http.get('/config/'+$scope.configId+'/'+$scope.platform+'/bc.json'
            ).success(function(data, status) {
            $scope.config = data;
        }).error(function(status, headers, response, config){
            $log.warn(status, headers, response, config);
        });
    };
});
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/partial1', {templateUrl: 'partial1.html', controller: 'ViewCtrl'});
        $routeProvider.when('/partial2', {templateUrl: 'partial2.html', controller: 'ViewCtrl'});
        $routeProvider.otherwise({redirectTo: '/partial1'});
    }]);
