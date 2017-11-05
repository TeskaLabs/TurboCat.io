angular.module('module').
component('moduleList',
{
	templateUrl: '/webapp/module/module-list.template.html',

	controller: function ModuleListController($scope, $http)
	{
		this.modules = [];
		var that = this;

		$http.get('/api/module/list').
		then(function(response) {
			that.modules = response.data.modules;
		});
	}

});
