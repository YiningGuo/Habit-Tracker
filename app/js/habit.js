(function() {
  'use strict';

  var HabitCtrl = function($scope, Comment) {
    $scope.habits = [];

    $scope.query = function() {
      var resource = Habit.query();
      resource.$promise.then(function(messages){
        $scope.habits = messages;
      });
    };
  };

  angular
  .module('App.Habit', [])
  .controller('HabitCtrl', HabitCtrl);
})();
