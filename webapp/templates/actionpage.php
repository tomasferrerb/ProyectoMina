<html>
<body>
   
	
	Su mensaje : <?php echo htmlspecialchars($_POST['txtmensaje']); ?> Ha sido enviado
<?php

echo phpinfo();

$message = exec("/var/www/scripts/monitor.py --message hola 2>&1");
print_r($message);
?>	 
<!--
<?php
echo '<pre>';
// Outputs all the result of shellcommand "ls", and returns
// the last output line into $last_line. Stores the return value
// of the shell command in $retval.
$last_line = system('./monitor.py --message hola', $retval);
// Printing additional info
echo '
</pre>
<hr />Last line of the output: ' . $last_line . '
<hr />Return value: ' . $retval;
?>


<?php 
$command = escapeshellcmd("'sudo ../../.././home/pi/ProyectoMina/monitor.py --message \'hola\' --color blue'");
$output = shell_exec($command);
var_dump($output);
echo $command;
?>
-->
</body>
</html>
		
		
				


