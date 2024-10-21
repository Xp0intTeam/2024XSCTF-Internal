<!doctype html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    </head>
    <body>
        <img src="./images/people.jpg" class="bg" width="20%" height="auto">
    </body>
    <!-- did u find the location of flag? -->
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
        if (preg_match('/(\<\!DOCTYPE|\<\!ENTITY)/gis', $xmlfile))
        {
            die('not this way, sir');
        }
        if (preg_match('/php|filter|expect|glob|phar|host|encode|decode|conf|\%/is',$xmlfile))
        {
            die("bad word!");
        }
    }
    $dom = new DOMDocument();
    $dom->loadXML($xmlfile, LIBXML_NOENT | LIBXML_DTDLOAD); 
    $creds = simplexml_import_dom($dom);
    echo $creds;
?>