'use strict';

var App = angular.module('App',
['ngRoute',
 'ngResource',
 'Resource',
 'App.Habit',
 'App.EditDialog'])
.config(function($routeProvider){

  $routeProvider.when('/',{
    templateUrl: 'partials/habit.html',
    controller: 'HabitCtrl',
  });

  $routeProvider.otherwise({
    redirectTo : '/'
  });
});
