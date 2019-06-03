
#!/bin/bash

echo -e "Content-type: text/html\n\n"
echo "<h1> Rasberry Pi Alive: </h1>"
echo "<p>"
echo "<pre> $(./rpistatus) </pre>"
echo "</p>"
