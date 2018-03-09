/* Service for create and edit dialog */

(function() {
  'use strict';

  var editDialog = function(Habit) {
    return {
      restrict:'E',
      templateUrl:function(tElement) {
        return '/partials/edit_dialog.html';
      },
      link:function(scope, elem, attrs) {
        scope.showDialog = function() {
          $('#dialog').modal();
        };

        scope.createHabit = function(title) {
          var habit = new Habit({title: title});
          habit.$save();
        };
      }
    };
  };

angular
.module('App.EditDialog', [])
.directive('editDialog', editDialog);
})();
