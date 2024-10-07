<?php

require 'functions.php';
// require 'Router.php';
require 'Database.php';

$config = require 'config.php';
$db = new Database($config['database'], 'root', '');

$id = $_GET['id'];
$query = "select * from posts where id = :id";

$posts = $db->query($query, [':id' => $id])->fetchAll(PDO::FETCH_ASSOC);

dd($posts);