<?php

function dd($data){
    echo '<pre>';
    die(var_dump($data));
    echo '</pre>';
}

function abort($code=404) {
    http_response_code($code);
    require "controllers/{$code}.php";
    exit;
}

function urlIs($value){
    return $_SERVER['REQUEST_URI'] === $value;
}

function authorize($condition, $status = Response::HTTP_FORBIDDEN){
    if ($condition) {
        abort($status);
    }
}