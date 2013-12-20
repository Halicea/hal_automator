 // var mockDataForThisTest = "json=" + encodeURI(JSON.stringify('bc.json'));


var app = angular.module('myApp', []);

app.controller('JsonCtrl', function($scope, $http, $log){
    $scope.config = {};	    			
    $http.get('http://staging.mediawiremobile.com:5001/config/FloridaDesign/IOS/bc.json'
    ).success(function(data, status) {
            $scope.config = data;
    }).error(function(a, b, c, d){
		 $log.log(a)
		 $log.log(b)
		 $log.log(c)
		 $log.log(d)
	});    
});