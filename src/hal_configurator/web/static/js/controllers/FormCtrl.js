'use strict';

app.controller('FormCtrl', function($scope, $log, $http, $routeParams, configSvc){
    $scope.config = {};
    $scope.state = "";
    $scope.loadingFiles = true;
    $scope.queue = [];
    $scope.resid = "Splash768x1004.png";
    
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
    var file = $scope.file,
                    state;
    // if (file.url) {
    //     file.$state = function () {
    //         return state;
    //     };
    //     file.$destroy = function () {
    //         state = 'pending';
    //         return $http({
    //             url: file.deleteUrl,
    //             method: file.deleteType
    //         }).then(
    //             function () {
    //                 state = 'resolved';
    //                 $scope.clear(file);
    //             },
    //             function () {
    //                 state = 'rejected';
    //             }
    //         );
    //     };
    // } else if (!file.$cancel && !file._index) {
    //     file.$cancel = function () {
    //         $scope.clear(file);
    //     };
    // }
});