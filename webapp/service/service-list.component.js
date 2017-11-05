angular.module('service').
component('serviceList',
{
	templateUrl: '/webapp/service/service-list.template.html?v=' + Date.now(),

	controller: function ServiceListController($scope, $http, $interval)
	{
		$scope.services = [];

		this.reload = function (){
			$http.get('/api/service/list').
			then(function(response) {
				$scope.services = response.data.services;
			});
		};
		this.reload();

		var theInterval = $interval(function(){
			this.reload();
		}.bind(this), 5000);
	}

});
