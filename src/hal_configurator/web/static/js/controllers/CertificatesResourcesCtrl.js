'use strict';

app.controller('CertificatesResourcesCtrl', function($scope, $log, configSvc){
    $scope.config = {};
    $scope.options = {
        url: url
    };
    $scope.loadingFiles = true;
    $http.get(url).then(
        function (response) {
            $scope.loadingFiles = false;
            $scope.queue = response.data.files || [];
        },
        function () {
            $scope.loadingFiles = false;
        }
    );
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
    $scope.setFiles = function(element) {
        $scope.$apply(function($scope) {
            console.log('files:', element.files);
            $scope.files = [];
            for (var i = 0; i < element.files.length; i++) {
                $scope.files.push(element.files[i]);
            }
        });
    };
    $scope.uploadFile = function() {
        var fd = new FormData();
        for (var i in $scope.files) {
            fd.append("uploadedFile", $scope.files[i]);
        }
        var xhr = new XMLHttpRequest();
        xhr.addEventListener("load", uploadComplete, false);
        xhr.addEventListener("error", uploadFailed, false);
        xhr.addEventListener("abort", uploadCanceled, false);
        xhr.open("POST", "http://localhost:5001/config/FloridaDesign/IOS/Resources/fileupload");
        xhr.send(fd);
    };

    function uploadComplete(evt) {
        alert(evt.target.responseText)
    }

    function uploadFailed(evt) {
        alert("There was an error attempting to upload the file.")
    }

    function uploadCanceled(evt) {
        alert("The upload has been canceled by the user or the browser dropped the connection.")
    }
});