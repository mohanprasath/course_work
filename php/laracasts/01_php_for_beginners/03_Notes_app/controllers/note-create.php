<?php

require 'Validator.php';

$heading = "Create Note";

$config = require 'config.php';
$db = new Database($config['database'], 'root', '');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $body = htmlspecialchars($_POST['body']);

    $errors = [];

    if (!Validator::string($body, 1, 1000)) {
        $errors['body'] = 'Body must be between 1 and 1000 characters';
    }

    if (empty($errors)) {
        $db->query('INSERT INTO notes (body, user_id) VALUES (:body, :user_id)', [
            'body' => $body,
            'user_id' => 1
        ]);
        header('Location: /notes');
    }
}

require "views/note-create.view.php";