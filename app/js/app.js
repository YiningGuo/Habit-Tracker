'use strict';

var App = angular.module('App',
['ngRoute',
 'ngResource',
 'Resource'])
.config(function($routeProvider){

  $routeProvider.when('/',{
    templateUrl: 'partials/habit.html',
    controller: 'HabitCtrl',
  });
  
});
