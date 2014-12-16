'use strict';

app.controller('AuthenticationCtrl', ['$cookieStore','$scope','$location','$routeParams','$http','$timeout', 'configSvc',
    function( $cookieStore, $scope, $location, $routeParams, $http, $timeout, configSvc ) {
        $scope.email = "";
        $scope.password = "";
        $scope.config = [];
        var getUser = function(){
            configSvc.get("FloridaDesign", "IOS", function(conf){
                $scope.config = conf;
            });
        };

        getUser();
        $scope.saveInput = function(email, password, emailJson, passwordJson) {
            $cookieStore.put("email", email);
            $cookieStore.put("password", password);

            $scope.email = email;
            $scope.password = password;
            if( email === emailJson && password === passwordJson ) {
                $cookieStore.put("emailJson", emailJson);
                $cookieStore.put("passwordJson", passwordJson);
              //  $timeout(function(){
                    window.location.assign('http://localhost:5001/index.html');
             //   }, 100);
            } else
                alert('Incorrect email/password');
        };
}]);