<?php
highlight_file(__FILE__);
error_reporting(0);

echo '第一枪 长相思兮长相忆，短相思兮无穷极。相思!<br>';
class Gotham{
    public $man1;
    public $man2;
    public $ohoh=false;
    public function __construct($man1,$man2){
        $this->man1 = $man1;
        $this->man2 = $man2;
    }
}

if(isset($_POST['man1']) && isset($_POST['man2'])){
    $man1 = $_POST['man1'];
    $man2 = $_POST['man2'];

    $who = new Gotham($man1,$man2);
    if(preg_match("/xiaohe/", $man2)){
        $serial_who = str_replace('xiaohe', 'menglei', serialize($who));
        $boom = unserialize($serial_who);
        if($boom->ohoh){
            echo '开!<br>';
            $spear1 = true;
        }
    }else{
    die("Don't leave");
    }
}else{
    die("jailjail~");
}

echo '第二枪 相思一夜情多少，地角天涯未是长。断肠!<br>';
$username = (String)$_POST['username'];
$password = (String)$_POST['password'];
$code = (String)$_POST['code'];
if($code === mt_rand(1,0x36D) && $password === $flag || $username ==="hanxin"){      
    if($code == 't0'){
        echo '开!<br>';
        $spear2 = true;
    }
}
else{
    die("眼见为虚，心听则实。");
}

echo '第三枪 盲龙!乾坤一簌天下游，月如钩，难别求。<br>';
$d = $_POST['d'];
if (intval('$d') < 4 && intval($d) > 10000) {
    $spear3 = true;
    echo "开！<br/>";
} else {
    die("看招！");
}

echo '第四枪 风流!书香百味有多少，天下何人陪白衣。<br>';
$num = $_POST['num'];
if (preg_match("/[0-9]/", $num)) {
    die("呵，我已看穿你的心！");
}
if (intval($num)) {
    $spear4 = true;
    echo "开！<br/>";
}

echo '第五枪 无双!枪似犹龙万兵手，命若黄泉不回头。<br>';
$mdmd1 = $_POST['mdmd1'];
$mdmd2 = $_POST['mdmd2'];
if ($mdmd1 !== $mdmd2 && md5($mdmd1) == md5($mdmd2)){
    $spear5 = true;
    echo "开！<br/>";
}
else{
    die('为何不避？');
}

echo '第六枪 白龙!有过痛苦方知众生痛苦，有过牵挂，了无牵挂。若是修佛先修心，一枪风雪一枪冰。<br>';
$mdmdmd1 = $_POST['mdmdmd1'];
$mdmdmd2 = $_POST['mdmdmd2'];
if ($mdmdmd1 !== $mdmdmd2 && md5($mdmdmd1) === md5($mdmdmd2)){
    $spear6 = true;
    echo "开！<br/>";
}
else{
    die('这枪如何呢？');
}

echo '第七枪 望穿!翻云起雾藏杀意，横扫千军几万里。<br>';
$mdmdmdmd1 = (string)$_POST['mdmdmdmd1'];
$mdmdmdmd2 = (string)$_POST['mdmdmdmd2'];
if ((string)$mdmdmdmd1 !== (string)$mdmdmdmd2 && md5((string)$mdmdmdmd1) === md5((string)$mdmdmdmd2)){
    $spear7 = true;
    echo "开！<br/>";
}
else{
    die('再来！');
}

echo '第八枪 鲲鹏!纵使韩信断了枪，也徒留我一人伤。<br>';
$xx = "test123";
$qq = $_POST['qq'];
@parse_str($qq);
if ($xx[0] != 'QNKCDZO' && md5($xx[0]) == md5('QNKCDZO')) {
   $spear8 = true;
   echo "开！<br/>";
}
else{
    die('不错不错，继续吧！');
}

echo '第九枪 百鬼夜行!我宁一枪闯天下，月下亮枪只为她。<br>';
$level =$_POST['pra'];

if(isset($level) && substr(md5($level),0,5)==='8031b')
{
    $spear9 = true;
    echo "开！<br/>";
}
else
{
    die('这一枪，千锤百炼！');
}

echo '第十枪 霸王！有爱有恨终难断，任流水，不相念。<br>';
if (!isset($time)) {
    $time = gmmktime();
}
$b = substr($time, 0, 7);
mt_srand($b);
echo "hint:" . (mt_rand()) . "<br />";
for ($i = 0; $i <= 100; $i++) {

    if ($i == 100) {
        $sui = mt_rand();
    } else {
        mt_rand();
    }
}

if ($_POST['many'] == $sui) {
    $spear10 = true;
    echo "开！<br/>";
} else {
    die("你很强，那就来试试我的100连击吧<br/>");
}

echo '第十一枪 释怀!七进七出无人挡，万军丛中取首级。一将终成万骨枯，回首看，尸横遍野。<br>';
$data = parse_url($_SERVER['REQUEST_URI']);
$han = basename($data['query']);
$a = $_GET['a'];
$b = $_GET['b'];
if (!preg_match('/[a-z0-9_]/i', $han)) {

    if (is_string($a) && is_numeric($b)) {
        if ($a != $b && md5($a) == md5($b)) {
            $spear11 = true;
            echo "开！<br/>";
        } else {
            die("看来你也就能到这里了");
        }
    } else {
        die("这可不行，得认真了");
    }  
} else {
    die('我的枪千变万化，可不能每次都用同一个方法接吧');
}

echo '第十二枪 抬头 百万将士再摇旗 将军韩信战无敌<br>';
if(isset($_POST['fin'])){
    $num = $_POST['fin'];
    if($num==4476){
        die("no no no!");
    }
    if(intval($num,0)==4476){
        $spear12 = true;
        echo "开！<br/>";
    }else{
        echo intval($num,0);
    }
}
else{
    die("坚持了这么久，你还有几分力气呢，还能接下吗");
}

if($spear1&&$spear2&&$spear3&&$spear4&&$spear5&&$spear6&&$spear7&&$spear8&&$spear9&&$spear10&&$spear11&&$spear12)
{
    echo '第十三枪 我命由我不由天！<br>';
    $flag1 = $_POST['flag1'];
    $flag2 = $_POST['flag2'];
    if (!preg_replace('/[a-z0-9_]/isD', '', $_POST['flag1'])) {
        echo "这样可不太好哦<br/>";
    } else {
        echo "可敬的对手，我认可你的实力了，去找到属于你的flag吧<br>";
        $flag1('', $flag2);
    }
}
else{
    die('你真的以为自己接下了所有招吗');
}