<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>QRコード作成サイト</title>
<style>
body {
  text-align: center;
}
</style>
</head>
<body>
<p>生成されたQRコード</p>
<?php
$name = $_GET["name"];
$sex = $_GET["sex"];
$day = $_GET["day"];

//文字をエンコードする関数
$keywordurl = urlencode($name,$sex,$day);
$url="http://chart.apis.google.com/chart?chs=300x300&cht=qr&chl=$keywordurl";
#$img = file_get_contents($url);

#$imginfo = pathinfo($url);

#$img_name = $imginfo['basename'];

#file_put_contents('C:/Users/HN4-00012/Desktop/upload/' . $img_name, $img);

#echo '<img src="img.php?img_name=' . $img_name . '" />';
?>
<!--画像として出力する-->
<img src="<?php echo $url; ?>">


</body>
</html>