'use strict';

app.controller('CertificatesResourcesCtrl', function($scope, $log, configSvc){
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
    refreshConfig();
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