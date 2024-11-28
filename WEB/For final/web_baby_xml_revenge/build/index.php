<!doctype html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><!-- zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~zaku~ seCr3t.php -->
    </head>
    <body>
        <img src="./people.jpg" class="bg" width="20%" height="auto">
    </body>
    <!-- did u find the location of flag again? -->
</html>
<?php
    libxml_disable_entity_loader (false);
    $xmlfile = file_get_contents('php://input');
   if(empty($xmlfile))
    {
        echo "need xmlfile to post";
    }
    else
    {
        if (preg_match('/\<\!DOCTYPE/is', $xmlfile))
        {
            die('<!DOCTYPE is detected, hacker!');
        }
        if (preg_match('/\<\!ENTITY/is', $xmlfile))
        {
            die('<!ENTITY is detected, hacker!');
        }
        if (preg_match('/index|utf-8|expect|glob|phar|host|decode|conf|\%/is',$xmlfile))
        {
            die("bad word!");
        }
    }
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD); 
    $creds = simplexml_import_dom($dom);
    echo $creds;
?>