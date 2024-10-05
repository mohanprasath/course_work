<?php

$uri = $_SERVER['REQUEST_URI'];

$url = parse_url($uri, PHP_URL_PATH);

$routes = [
    '/about' => 'about.php',
    '/contact' => 'contact.php',
    '/' => 'index.php'
];

function abort($code) {
    http_response_code($code);
    require "controllers/{$code}.php";
    exit;
}

function routeToController($url, $routes) {
    if (array_key_exists($url, $routes)) {
        require "controllers/{$routes[$url]}";
    } else {
        abort(404);
    }
}

routeToController($url, $routes);