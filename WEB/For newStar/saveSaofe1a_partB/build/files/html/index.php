<!DOCTYPE html>  
<html lang="zh-CN">  
<head>  
    <meta charset="UTF-8">  
    <meta name="viewport" content="width=device-width, initial-scale=1.0">  
    <title>同学录查询系统</title>  
    <link rel="stylesheet" href="styles.css">  
</head> 
<style>
body { 
    font-family: Arial, sans-serif;  
    background-color: #f4f4f4;
    margin: 0;  
    padding: 0;  
    /* 添加背景图片 */  
    background-image: url('1.jpg');  
    /* 设置背景图片不重复 */  
    background-repeat: no-repeat;  
    /* 设置背景图片覆盖整个页面 */  
    background-size: cover;  
    /* 设置背景图片固定，不随页面滚动 */  
    background-attachment: fixed;  
    /* 可选：设置背景图片的位置，例如居中 */  
    background-position: center;  
    margin: 0;  
    padding: 0;  
}  
  
.container {  
    max-width: 600px;  
    margin: 50px auto;  
    padding: 200px;
}  
  
h1 {  
    text-align: center;  
    color: #333;  
}  
  
.search-form {
    display: flex;  
    flex-direction: column; 
    align-items: center;
    margin-bottom: 20px; 
}  
  
.search-input {  
    width: 50%;  
    padding: 10px;  
    box-sizing: border-box; /* 确保内边距不会增加总宽度 */  
    border: 1px solid #ccc;  
    border-radius: 4px;  
    margin-bottom: 10px; /* 在输入框和按钮之间添加垂直间距 */  
}  
  
.search-button {  
    width: 10%; /* 如果希望按钮宽度与输入框相同 */  
    padding: 10px;  
    border: none;  
    background-color: #007BFF;  
    color: #fff;  
    border-radius: 4px;  
    cursor: pointer;  
    text-align: center; /* 可选：使按钮内的文本居中 */  
}  
  
.search-button:hover {  
    background-color: #0056b3;  
}
.result {
    max-width: 600px;
    margin: 50px auto; 
    padding: 10px;  
    border: 1px solid #ddd;  
    border-radius: 4px;  
    background-color: #fafafa;  
}  
  
.result p {  
    margin: 5px auto;  
}

/* From Uiverse.io by krlozCJ */ 
button {
  border: none;
  outline: none;
  background-color: #056dfa;
  padding: 10px 20px;
  font-size: 12px;
  font-weight: 700;
  color: #fff;
  border-radius: 5px;
  transition: all ease 0.1s;
  box-shadow: 0px 5px 0px 0px #056bfa27;
}

button:active {
  transform: translateY(5px);
  box-shadow: 0px 0px 0px 0px #056bfa27;
}

</style>
<body>  
    <div class="container">  
        <h1>阳光一中高三一班同学录</h1>  
        <!-- sqlmap是没有灵魂的 -->
        <form class="search-form" method="get">  
            <input type="text" class="search-input" placeholder="请输入你在毕业班的学号(听说扣1送地狱火)" name="inject">  
            <button type="submit">
                <span>Search</span>
            </button>
        </form>
    </div>

<pre>
<?php
function waf($inject) {

    if(preg_match("/select|update|delete|drop|insert|where|\./i",$inject))
    {
        echo "<div id='result' class='result'>";
        echo '<h3>我给你查个蛋，我头都大了</h3>';
        echo "<br>";
        echo '这种小网站也要黑';
        echo "<br>";
        echo '让我想想除了insert、where、delete、select、drop、update和.你们大黑阔还有什么招';
        echo "<br>";
        echo "</div>";
        die();
    }
    if(preg_match("/execute|set|prepare|\./i",$inject))
    {
        echo "<div id='result' class='result'>";
        echo '<h3>别天天烦我了</h3>';
        echo "<br>";
        echo '嘻嘻，想起来了，set、prepare、execute也不行哦';
        echo "<br>";
        echo '小黑阔再不走我就报警咯';
        echo "<br>";
        echo "</div>";
        die();
    }
}

if(isset($_GET['inject'])) 
{
    $id = $_GET['inject'];
    waf($id);
    $mysqli = new mysqli("localhost","root","","student");
    $mysqli->set_charset("utf8mb3");
    $t = 1;

    //多条sql语句
    $sql = "select * from `class1` where id = '$id';";

    $res = $mysqli->multi_query($sql);
    echo "<div id='result' class='result'>";
    echo "<h3>查询结果如下</h3>";
    if ($res){//使用multi_query()执行一条或多条sql语句
        do{
          if ($rs = $mysqli->store_result()){//store_result()方法获取第一条sql语句查询结果
            if($t==1)
            {
                $row = $rs->fetch_row();
                echo '你的学号是：'.$row[0];
                echo "<br>";
                echo '你的名字是：'.$row[1];
                echo "<br>";
                echo '你的班级是：'.$row[2];
                echo "<br>";
                echo '你的爱好是：'.$row[3];
                echo "<br>";
            }
            else{
                while ($row = $rs->fetch_row()){
                    var_dump($row);
                    echo "<br>";
                  }
            }
            $rs->Close(); //关闭结果集
            if ($mysqli->more_results()){  //判断是否还有更多结果集
              $t = $t + 1;
              echo "<hr>";
            }
          }
        }while($mysqli->next_result()); //next_result()方法获取下一结果集，返回bool值
      } else {
        echo "error ".$mysqli->errno." : ".$mysqli->error;
      }
    echo "</div>";
    $mysqli->close();  //关闭数据库连接
}
?>
</pre>
</body>
</html>

