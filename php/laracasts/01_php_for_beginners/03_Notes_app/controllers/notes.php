<?php

$heading = "My Notes Page";


$config = require 'config.php';
$db = new Database($config['database'], 'root', '');

$notes = $db->query('SELECT * FROM notes where user_id=1;')->get();

# dd($notes);

require "views/notes.view.php";