<?php

use Illuminate\Support\Facades\Route;

Route::get('/', \App\Http\Controllers\HomeController::class);

Route::get('/about', function () {
    return view('pages.about', [
        'greeting' => 'About Universe'
    ]);
});
