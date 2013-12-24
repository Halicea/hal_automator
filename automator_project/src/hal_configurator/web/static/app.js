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
    $scope.showDialog = function () {
        var msg = 'Hello World!';
        var options = {
            resolve: {
                msg: function () { return msg; }
            }
        };
        var dialog = $dialog.dialog(options);

        dialog.open('table.html', 'DialogCtrl');
    };

    $scope.saveConfig = function() {
        $http.post('/config/'+$scope.configId+'/'+$scope.platform+'/bc.json', $scope.config).success(function(data){
            alert(data);
        }).error(function(status, headers, response, cnf){
                $log.warn(status, headers, response, cnf);
                alert(status);
        });
    };
    app.controller('DialogCtrl', function ($scope, dialog, msg) {
        $scope.msg = msg;
    });
    $scope.cancelEdit = function() {
        window.location = "/table.html";
    };
});
    config(['$routeProvider', function($routeProvider) {
        $routeProvider.when('/partial1', {templateUrl: 'partial1.html', controller: 'ViewCtrl'});
        $routeProvider.when('/partial2', {templateUrl: 'partial2.html', controller: 'ViewCtrl'});
        $routeProvider.otherwise({redirectTo: '/partial1'});
    }]);
