<?php

$heading = "My Notes Page";
$current_user_id = 1;

$config = require 'config.php';
$db = new Database($config['database'], 'root', '');

$note = $db->query('SELECT * FROM notes where id= :id', ['id' => $_GET['id']])->findOrFail();

authorize($note['user_id'] !== $current_user_id);

require "views/note.view.php";