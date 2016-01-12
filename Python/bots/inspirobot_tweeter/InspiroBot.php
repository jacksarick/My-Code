<?php
	$img_src = file_get_contents("http://inspirobot.me/api?generate=true");
	$image = file_get_contents($img_src);
	file_put_contents('./image.jpg', $image);
	echo $img_src;
	echo "\n";
?>