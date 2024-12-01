<!DOCTYPE html>
<html>
<head>
<title>
    <?php echo("PHP Program #1"); ?>
</title>
</head>
<body>
<?php 
  
  # program #1
  echo "<h3>Program 1:</h3>";
  echo("Yay!");
  echo "<hr>";
 
  # program #2
  echo "<h3>Program 2:</h3>";
  $year = 2021; # number variable
  $month = "February"; # string variable
  echo "The current month and year(probably) are $month and $year";
  echo "<hr>";

  # program #3
  echo "<h3>Program 3:</h3>";
  $number = 2021;
  $string = "February";
  $decimal = 2021.0;
  $isLeapYear = false;
  echo "$number $string $decimal";
  echo $isLeapYear ? 'true':'false';
  echo "<hr>";

  # program #4
  echo "<h3>Program 4:</h3>";
  $phrase = "a string variable";
  echo $phrase;
  echo "<br/>";
  $phrase[0] = 'A'; 
  echo $phrase;
  echo "<br/>";
  echo str_replace("string", "String", $phrase);
  echo "<br/>";
  echo substr($phrase, 2, 6);
  echo "<hr>";
 ?>

</body>
</html>