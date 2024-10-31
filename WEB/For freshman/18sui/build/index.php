<?php
// 今年多大了？
// 刚满18岁~
if(isset($_GET['c'])){
    $c=$_GET['c'];
    if(!preg_match("/\;|[a-z]|[0-9]|\`|\|\#|\{|\'|\"|\`|\%|\x09|\x26|\x0a|\>|\<|\.|\,|\?|\*|\-|\=|\[/i", $c)){
        system("cat /".$c.".php");
    }
}else{
    highlight_file(__FILE__);
} 
