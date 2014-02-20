'use strict';

app.controller('ConfigCtrl', function($scope, $log, $routeParams, configSvc){
    $scope.config = {};
    $scope.configId = $routeParams.appname;
    $scope.platform = $routeParams.platform;
    $scope.groups = configSvc.getGroups($scope.platform);
    $scope.displayed_group = $scope.groups[0];
    $scope.platforms = configSvc.platformsForApp($routeParams.appname);
    for (var i = $scope.platforms.length - 1; i >= 0; i--) {
        if($scope.platforms[i].value === $scope.platform){
            $scope.platforms[i].active = "active";
        }
    };
    if(!$scope.platform){
        $scope.platform  = $scope.platforms[0].value;
    }
    var refreshConfig = function(){
        configSvc.get($scope.configId, $scope.platform, function(conf){
            $scope.config = conf;
        });
    };

    $scope.groupChanged = function(group){
        for (var i = $scope.groups.length - 1; i >= 0; i--) {
            if($scope.groups[i] == group) {
                $scope.displayed_group = group;
            }
        };
    };
    refreshConfig();
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