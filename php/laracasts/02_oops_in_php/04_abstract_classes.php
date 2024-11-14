<?php


abstract class AchievementType
{
	public function name()
	{
		$class = (new ReflectionClass($this))->getShortName();
		return trim(preg_replace('/[A-Z]/', ' $0', $class));
	}

	public function icon()
	{
		return strtolower(str_replace(' ', '-', $this->name()) . '.png');
	}

	abstract public function qualifies($user);

}

class FirstThousandPoints  extends AchievementType
{
	public function qualifies($user)
	{

	}
}

class FirstBestAnswer extends AchievementType
{
	public function qualifies($user)
	{

	}
}

class ReachTop50 extends AchievementType
{

	public function qualifies($user)
	{
		return 'Reached Top 50';
	}

}

$achievementType = new FirstThousandPoints();
echo $achievementType->name() . PHP_EOL;
echo $achievementType->icon() . PHP_EOL;

$achievementType = new ReachTop50();
echo $achievementType->name() . PHP_EOL;
echo $achievementType->icon() . PHP_EOL;
echo $achievementType->qualifies('test_user');