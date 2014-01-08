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