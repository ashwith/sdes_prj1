file=$1
vid=$2
(echo "<!DOCTYPE html>"
echo "<html>"
echo "<body>"
echo 
echo "<video height="360" controls>"
echo   "<source src=\"$vid\" type=\"video/ogg\">"
echo   "Your browser does not support HTML5 video."
echo "</video>"
echo 
echo "</body>"
echo "</html>") > $file
