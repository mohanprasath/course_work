<?php

use Core\Validator;

it('validates a string', function () {
    $result = \Core\Validator::string('foobar');

    expect($result)->toBeTrue();
    expect(Validator::string(false))->toBeFalse();
    expect(Validator::string(''))->toBeFalse();
});

it('Validates a string with a minimum length', function () {
    expect(Validator::minLength('foobar', 20))->toBeFalse();
});

it('Validates a email', function () {
    expect(Validator::email('foobar'))->toBeFalse();
    expect(Validator::email('foobar@gmail.com'))->toBeTrue();
});

it('Validates a number greater than', function () {
    expect(Validator::greaterThan(10, 5))->toBeTrue();
    expect(Validator::greaterThan(5, 10))->toBeFalse();
})->only();