<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>First PHP Document #1</title>
    <style>
        body {
            display:grid;
            place-items: center;
            height: 100vh;
            margin: 0;
            font-family: sans-serif;
        }
    </style>
</head>
<body>
<!-- <h1> Hello World! </h1> -->
<!-- <h2> <?php

?> </h2> -->

<h2> <?php

    ?>
    <p><?php echo "The book $book was written by $author"; ?></p>
    <p><?= $message ?></p>

    <? # arrays in PHP ?>
    <!-- <h3>Books</h3> -->
    <ul>

    </ul>

    <? # associative arrays ?>
    <p><? # $books[2] ?></p>
    <?php

    ?>
    <h3>Books</h3>
    <ul>
        <?php
        foreach ($books as $book) {
            echo "<li><a href='$book[purchaseUrl]'>$book[title]</a> by $book[author]</li>";
        }
        ?>
    </ul>

    <? # Functions and Filters ?>
    <h3>Functions and Filters</h3>
    <ul>

        <? # Functions and Filters ?>
        <?php
        # if book is written by ANdy Weir, then print the hyper link
        /* foreach ($books as $book) {
            if ($book['author'] === 'Andy Weir') { # = is assignment, == is comparison, === is strict comparison
                echo "<li><a href='$book[purchaseUrl]'>$book[title]</a> by $book[author]</li>";
            }
        } */
        ?>
        <?php


        foreach ($booksByAndyWeir as $book) {
            echo "<li><a href='$book[purchaseUrl]'>$book[title]</a> by $book[author]</li>";
        }
        ?>
    </ul>

    <? # Lambda Functions ?>
    <h3>Lambda Functions</h3>
    <?php
    /* $filterByAuthor = function ($books, $author) { # is an anonymous function or a lambda function
        return array_filter($books, function($books) use ($author){
            return $books['author'] === $author;
        });
    };
    $booksByAndyWeir = $filterByAuthor($books, 'Andy Weir');
    foreach ($booksByAndyWeir as $book) {
        echo "<li><a href='$book[purchaseUrl]'>$book[title]</a> by $book[author]</li>";
    }*/


    foreach ($booksBy2021 as $book) {
        echo "<li><a href='$book[purchaseUrl]'>$book[title]</a> by $book[author]</li>";
    }

    foreach ($booksByAndyWeir as $book) {
        echo "<li><a href='$book[purchaseUrl]'>$book[title]</a> by $book[author]</li>";
    }
    ?>
</body>
</html>