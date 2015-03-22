angular.module('list', []);

function FunRunGet($scope, $http) {
	$http.get({
		method: 'Get',
		url: 'http://104.239.139.43:8000/api/funruns'}).
	success(function(data) {
		$scope.funrun = data.funruns;
	});
}