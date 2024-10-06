<?php

class Database
{

    protected $conenction;
    protected $statement;

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

        $this->statement = $this->conenction->prepare($query);
        $this->statement->execute($parameters);

        return $this;

    }

    public function get(){
        return $this->statement->fetchAll();
    }

    public function find(){
        return $this->statement->fetch();
    }

    public function findOrFail(){
        $result = $this->find();
        if(!$result){
            abort(Response::HTTP_NOT_FOUND);
        }
        return $result;
    }



}
