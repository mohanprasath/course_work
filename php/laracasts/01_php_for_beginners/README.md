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

## 01 The Fundamentals

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

## 02 Dynamic Web Applications

- partials folder is used to store the partials of the web application
- `var_dump()` can be useful in debugging the code by printing the type and value of the variable
- `$_SERVER`is a super global in php
- html `<pre>` tag is used to preserve the formatting of the text in the browser followed by the `</pre>` tag
- try to do micro improvements always; Code readability will improve;
- `parseurl()` is used to parse the url in php. It separates the url into different parts: scheme, host, path, query, etc
- `http_response_code(404)` is used to set the response code to 404 in php to the client browser
- A class is a blueprint for creating objects in php
- `public` is an access modifier in php
- `new` keyword is used to create a new instance of the class
- `->` is used to access the properties and methods of the class
- declare function visibility in the class, its a good practice
- `_GET` is used to get the query parameters from the url

## 03 Notes Mini-Project

- Refresh SQL DDL, DML Basics
- Create a table in mysql: Refer the SQL folder for detailed code
- Authorization - prevents unauthorized access to the application; status code usually associated with this is 401, 403
- `404` is a status code for not found
- `Response.php` - increases the readability of the code by storing the response code and message in a separate file
- All the form inputs needs a name attribute to be sent to the server
- `get` method is used to get the data from the server and `post` method is used to send the data to the server
- `get` request is idempotent and `post` request is not idempotent
- Data Sanitization - prevents the sql injection attacks, also prevents the xss attacks, etc
- `htmlspecialchars()` is used to sanitize the data in php
- A pure function is a function that does not have any side effects or dependencies
- `filter_var` is used to filter the data in php based on the filter type

## 04 Project Organization

- move similar files (i.e. related topics) into a folder to organize the code. This improves readability
- `extract` function is used to extract the variables from the array in php. Check view function in functions.php
- `spl_autoload_register` is used to autoload the classes in php without using the require or include statements
- namespace is used to avoid the conflicts between the classes in php; Alternatively, we can use the `use` keyword to avoid the conflicts
- Service Container - used to store the instances of the classes in php that can be used throughout the application
- check the `routes.php` for the routes in the application and how they are configured to allow and handle different types of requests

