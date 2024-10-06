<?php

$routes = require 'routes.php';

$uri = $_SERVER['REQUEST_URI'];

$url = parse_url($uri, PHP_URL_PATH);

function routeToController($url, $routes) {
    if (array_key_exists($url, $routes)) {
        require "controllers/{$routes[$url]}";
    } else {
        abort(404);
    }
}

routeToController($url, $routes);