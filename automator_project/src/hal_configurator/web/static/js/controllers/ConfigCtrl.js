'use strict';

app.controller('ConfigCtrl', function($scope, $log, $http, $routeParams, configSvc){
    $scope.config = {};
    
    $scope.loadingFiles = true;
    $scope.queue = [];
    $scope.resid = "Splash768x1004.png";
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
    $scope.options = {
        url: "/config/FloridaDesign/IOS/bc.json/res/"+$scope.resid
    };
    $http.get($scope.options.url).then(
        function (response) {
            $scope.loadingFiles = false;
            $scope.queue = response.data.files || [];
        },
        function () {
            $scope.loadingFiles = false;
        }
    );
    var refreshConfig = function(){
        configSvc.get($scope.configId, $scope.platform, function(conf){
            var variables = conf.Variables;
            var resources = conf.Resources;
            $scope.config = variables.concat(resources);
        });
    };
    $scope.triggerUpload = function(){
        $('#uploadfield').click();
    };

    $scope.popup = function(conf) {
        $("html").tooltip({ selector: '[data-toggle="tooltip"]' });
        /*
        $('#helptext').tooltip('hide').attr('data-original-title', conf.tooltip)
          .tooltip('fixTitle')
          .tooltip('show');
        */
    };
    $scope.groupChanged = function(group){
        for (var i = $scope.groups.length - 1; i >= 0; i--) {
            if($scope.groups[i].title == group) {
                $scope.displayed_group = group;
            }
        };
        //if(group == "IOS")
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
    /*
    $scope.$on('fileuploaddone', function(event, files){ 
        alert('done');
    });
    $scope.$on('fileuploadfail', function(event, files){ 
        alert('fail');
    });
*/
    $scope.saveConfig = function() {
        $scope.submit();
        // configSvc.save($scope.configId, $scope.platform, $scope.config, function(validationResult){
        //     if(validationResult && validationResult.errors){
        //         alert(validationResult.errors);
        //     }
        // });
    };
    // $http.get($scope.url).then(
    //     function (response) {
    //         $scope.loadingFiles = false;
    //         $scope.queue = response.data.files || [];
    //     },
    //     function () {
    //         $scope.loadingFiles = false;
    //     }
    // );
});