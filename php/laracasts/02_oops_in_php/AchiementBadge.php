<?php
class AchiementBadge{

    public $title;
    public $description;
    public $points;

    public function __construct($title, $description, $points){
        $this->title = $title;
        $this->description = $description;
        $this->points = $points;
    }

    public function awardedTo($user){ // behaviour in the class
        // Give the badge to the user

    }


}