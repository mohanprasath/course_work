# PHP For Beginners

## Intro

Pick any langauge and then learn the concepts. Expand it from there.

## Installation - mac

- browser, editor, etc
- homebrew
- brew install wget
- brew install php
- current version 8.3.11
- brew install mysql
- brew install composer

## Demo Project 1

- `php -h` for getting help info on php
- `php -S localhost:8888` loads the index.html file in the web browser
- change the url to `http://localhost:8888/index.php` if you want to load the php directly
- `.` is the concantenation operator in php
- `var_dump()` is used to print the type and value of a variable
- `<?= ?>` is the shorthand for `<?php echo ?>`
- `$books = ['book1', 'book2', 'book3'];` is an array in php
- `foreach ($books as $book) { echo $book; }` is a loop in php
- Index numbering starts from zero in php
- In PHP filters, `=` is used for assignment and `==` is used for comparison and `===` is used for strict comparison
- Functions in php starts with the keyword `function`
- `array_filter()` is used to filter the array based on the condition. Example `array_filter($books, fn($book) => $book === 'book1')` 
- require and include are used to include the files in php. For example, `require 'index.view.php';` loads the index.view.php file