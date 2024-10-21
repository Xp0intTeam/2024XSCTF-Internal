<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>水平居中的页面</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            width: 100%;
            text-align: center;
        }

        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }

        textarea {
            width: 90%;
            height: 150px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        table {
            width: 90%;
            border-collapse: collapse;
            margin: 0 auto 20px auto;
            background-color: #f9f9f9;
        }

        th, td {
            border: 1px solid #ccc;
            padding: 8px 12px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }

        input[type="submit"] {
            padding: 8px 16px;
            border: none;
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
            border-radius: 4px;
            font-size: 14px;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <!-- 页面内容容器 -->
    <div class="content">

    <h2>Onliner sql runner</h2>
<form action="" method="POST">
    <label for="text">Please input: </label><br>
    <textarea id="text" name="sql" rows="10" cols="30"></textarea>
    <input type="submit" value="submit">
</form>
        <?php
        // 1. 连接数据库
        $servername = "localhost"; // 数据库服务器
        $username = "root";        // 数据库用户名
        $password = "123456";            // 数据库密码
        $dbname = "xsctf_company"; // 数据库名称

        // 创建连接
        $conn = new mysqli($servername, $username, $password, $dbname);

        // 检查连接是否成功
        if ($conn->connect_error) {
            die("连接失败: " . $conn->connect_error);
        }

        $sql = $_POST['sql'];
        if(isset($sql)){
            // 3. 使用 mysqli_multi_query 执行堆叠查询
            if ($conn->multi_query($sql)) {
                do {
                    // 检查当前结果集是否有结果
                    if ($result = $conn->store_result()) {
                        echo "<table border='1' cellpadding='10' cellspacing='0'>";
                        echo "<thead><tr>";
        
                        // 获取字段名称并生成表头
                        $field_count = $result->field_count;
                        $fields = $result->fetch_fields();
                        foreach ($fields as $field) {
                            echo "<th>" . htmlspecialchars($field->name) . "</th>";
                        }
        
                        echo "</tr></thead>";
                        echo "<tbody>";
        
                        // 遍历并输出结果
                        while ($row = $result->fetch_row()) {
                            echo "<tr>";
                            foreach ($row as $cell) {
                                echo "<td>" . htmlspecialchars($cell) . "</td>";
                            }
                            echo "</tr>";
                        }
        
                        echo "</tbody>";
                        echo "</table><br><br>"; // 输出表格结束标记
                        $result->free(); // 释放结果集
                    }
                    // 检查是否有更多的结果集
                } while ($conn->more_results() && $conn->next_result());
            } else {
                echo "查询错误: " . $conn->error;
            }
        }
        

        $conn->close();
        ?>


    </div>
</body>
</html>


