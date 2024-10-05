<?php

class Database
{

    protected $conenction;

    public function __construct($config, $username, $password)
    {

        $dsn = 'mysql:' . http_build_query($config, '', ';');

        // connect to our MySQL database
        $this->conenction = new PDO($dsn, $username, $password, [
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
    }

    public function query($query, $parameters = [])
    {

        $statement = $this->conenction->prepare($query);
        $statement->execute($parameters);

        return $statement;

    }

}
