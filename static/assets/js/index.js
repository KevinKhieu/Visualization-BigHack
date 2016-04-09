var app = angular.module('refugee', ['ui.bootstrap', 'ngMap']);
/*
app.config(function(uiGmapGoogleMapApiProvider) {
    uiGmapGoogleMapApiProvider.configure({
        key: 'AIzaSyDmhHXfXkoT-lGtvDQgqn3TRXqUiVdMcJY',
        v: '3.20', //defaults to latest 3.X anyhow
        libraries: 'weather,geometry,visualization'
    });
})*/

app.controller('RefugeeController', function ($scope, $sce) {
	$scope.map = {center: {latitude: 51.219053, longitude: 4.404418 }, zoom: 14, mapTypeId: google.maps.MapTypeId.ROADMAP };
    $scope.options = {scrollwheel: false};
});