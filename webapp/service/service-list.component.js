angular.module('service').
component('serviceList',
{
	templateUrl: '/webapp/service/service-list.template.html?v=' + Date.now(),

	controller: function ServiceListController($scope, $http)
	{

		this.services = [];
		var that = this;

		$http.get('/api/service/list').
		then(function(response) {
			that.services = response.data.services;
		});
	}

});
