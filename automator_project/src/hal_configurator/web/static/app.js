'use strict';

var app = angular.module('myApp', []);
app.config(function($httpProvider){
    delete $httpProvider.defaults.headers.common['X-Requested-With'];
});
