<?php

class CoffeeMaker 
{
	public function brew(){
		var_dump('Brewing the coffee');
	}

	public function brewLatte(){

	}
}

class SpecialtyCoffeeMaker extends CoffeeMaker{
	public function brewLatte(){
		var_dump('Brewing a Latter');
	}
}

class Collection{
	protected array $items;

	public function __construct(array $items){
		$this->items = $items;
	}

	public function sum($key){
		return array_sum(array_column($this->items, $key));
	}
}

class Video{
	public $title;
	public $length;

public function __construct($title, $length){
	$this->title = $title;
	$this->length = $length;
}

}

class VideosCollection extends Collection{
	public function length(){
		return $this->sum('length');
	}
}



$videos = new VideosCollection([
	new Video('Some Video 1', 100),
	new Video('Some Video 2', 200),
	new Video('Some Video 3', 300),
]);

var_dump($videos->length('length'));


(new SpecialtyCoffeeMaker())->brew();
(new SpecialtyCoffeeMaker())->brewLatte();