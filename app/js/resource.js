'use strict';

var Habit = function($resource){
	return $resource('/service/habit/:id', null, {});
};

angular
	.module('Resource',['ngResource'])
	.factory('Habit',Habit);
