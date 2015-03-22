function FunRuns($scope, $http) {
	$http.get('http://104.239.139.43:8000/api/funruns').
	success(function(data) {
		$scope.funrun = data;
	});
}