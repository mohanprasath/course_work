<?php

$greeting = "Hello";
# echo "$greeting World!"; # new method without needing a concatenation operator dot - ALERT only "" will work for this format

# checking conditionals in PHP
$book = "PHP for Beginners";
$author = "John Doe";
$read = false;
if ($read) {
    $message = "I have read the book $book";
} else {
    $message = "I have not read the book $book";
}

$books = [
    'Do Androids Dream of Electric Sheep?',
    'The Langoilers',
    'Hail Mary'
];
foreach ($books as $book) {
    # echo "<li>$book</li>";
}



$books = [
    [
        'title' => 'Do Androids Dream of Electric Sheep?',
        'author' => 'Philip K',
        'purchaseUrl' => 'https://www.amazon.com/Androids-Dream-Electric-Sheep-Blade/dp/0345404475',
        'read' => true,
        'year' => 1968
    ],
    [
        'title' => 'The Langoilers',
        'author' => 'Margaret Atwood',
        'purchaseUrl' => 'https://www.amazon.com/Langoliers-Stephen-King/dp/1501143805',
        'read' => false,'year' => 1980
    ],
    [
        'title' => 'Hail Mary',
        'author' => 'Andy Weir',
        'purchaseUrl' => 'https://www.amazon.com/Hail-Mary-Andy-Weir/dp/0593135202',
        'read' => true, 'year' => 2021
    ],
];




function filterByAuthor($books, $author) { # is a named functions
    return array_filter($books, function($books) use ($author){
        return $books['author'] === $author;
    });
}

function filter($array, $value, $key){ // Named generically
    return array_filter($array, function($array) use ($value, $key){
        return $array[$key] === $value;
    });
}
$booksBy2021 = filter($books, 1980, 'year');
$booksByAndyWeir = filter($books, 'Andy Weir', 'author');
$booksByAndyWeir = filterByAuthor($books, 'Andy Weir'); # extracted variable

require 'index.view.php'; # this is the view file