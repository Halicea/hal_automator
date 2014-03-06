'use strict';

app.factory('configSvc', function($http, $log){
	var result = {};
    result.index = function(callback){
        $http.get('/config').success(function(data){
           callback(data);
        }).error(function(status, headers, response, config){
            $log.warn(status, headers, response, config);
            callback([]);
        });
    };
    
    result.get = function(id, platform, callback){
        $http.get('/config/'+id+'/'+platform+'/bc.json').success(function(data, status) {
            callback(data);
        }).error(function(status, headers, response, config){
            callback(null);
            $log.warn(status, headers, response, config);
        });
    };
    
    result.platformsForApp = function(appName){
        return [{display:'iOS', value:'IOS', img_prefix:"/img/ico_ios"}, {display:'Android', value:'Android', img_prefix:"/img/ico_android"}];
    };
    
    result.getGroups = function(platform){
        var groups = {
            'IOS':[
                {title:'General', color:"#d477fc"}, 
                {title:'Settings', color:"#a25cdb"},
                {title:'Resources', color:"#5d31a8"},
                {title:'Design', color:"#312294"},
                {title:'Build App', color:"#030f69"}
            ],
            'Android':[
                {title:'Themes', color:"#d477fc"}, 
                {title:'Resources', color:"#a25cdb"},
                {title:'Settings', color:"#5d31a8"},
                {title:'Design', color:"#312294"},
                {title:'Build App', color:"#030f69"}
            ],

        };
        return groups[platform];
    };
    
    result.save = function(id, platform, config, callback){
        $http.post('/config/'+id+'/'+platform+'/bc.json', config)
        .success(function(data, status) {
            callback(data);
        }).error(function(status, headers, response, config){
            callback({
                errors:['Server threw an error']
            });
            $log.warn(status, headers, response, config);
        });
    };

    return result;
});