<?php

function dd($data){
    echo '<pre>';
    die(var_dump($data));
    echo '</pre>';
}

function urlIs($value){
    return $_SERVER['REQUEST_URI'] === $value;
}