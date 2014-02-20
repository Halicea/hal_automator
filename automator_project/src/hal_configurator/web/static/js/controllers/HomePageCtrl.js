'use strict';

app.controller('HomePageCtrl',
    function($cookieStore, $scope, $location, $routeParams, $http, $timeout, configSvc) {
        $scope.appname = $routeParams.appname;
        $scope.selected_platform = $routeParams.platform;
        $scope.platforms = configSvc.platformsForApp($routeParams.appname);
    });
