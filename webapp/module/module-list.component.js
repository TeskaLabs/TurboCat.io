angular.module('module').
component('moduleList',
{
	templateUrl: '/webapp/module/module-list.template.html?v=' + Date.now(),

	controller: function ModuleListController($scope, $http, $interval)
	{
		$scope.modules = [];

		this.reload = function (){
			$http.get('/api/module/list').
			then(function(response) {
				$scope.modules = response.data.modules;
			});
		};
		this.reload();

		var theInterval = $interval(function(){
			this.reload();
		}.bind(this), 5000);
	}

});
