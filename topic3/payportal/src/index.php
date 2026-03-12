<?php

$servername = $_ENV["MYSQL_HOST"];
$username = $_ENV["MYSQL_USER"];
$password = $_ENV["MYSQL_PASS"];
$dbname = $_ENV["MYSQL_DB"];

try {
  $conn = new PDO("mysql:host=$servername;dbname=$dbname;charset=utf8mb4", $username, $password);
  // set the PDO error mode to exception
  $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
  //echo "Connected successfully";
} catch(PDOException $e) {
  echo "Connection failed: " . $e->getMessage();
  die;
}

$id = "3332654";

if (!empty($_GET["id"])) {
  $id = $_GET["id"];
}

$search = $_GET["period"];
$error = "";

try {
  $databaseTest = null;
  if (empty($search)) {
    $databaseTest = ($conn->query('SELECT * FROM payportal WHERE id = "' . $id . '"'))->fetchAll(PDO::FETCH_OBJ);
  } else {
    $databaseTest = ($conn->query('SELECT * FROM payportal WHERE id = "' . $id . '" AND period LIKE "%' . $search . '%"'))->fetchAll(PDO::FETCH_OBJ);
  }
  if (!$databaseTest) $error = $databaseTest->error;
} catch (Exception $e) {
  $error = $e->getMessage();
}

?>

<!doctype html>
<html lang="en">
  <head>
    <title>Employee Portal - Pay Summary</title>

    <!-- Bootstrap core CSS -->
<link href="bootstrap.min.css" rel="stylesheet" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="pricing.css" rel="stylesheet">
  </head>
  <body>
    <div class="p-3 mb-3 bg-white shadow-sm d-flex flex-column flex-md-row align-items-center px-md-4 border-bottom">
  <h5 class="my-0 mr-md-auto font-weight-normal">Pay Summary Portal</h5>
  <nav class="my-2 my-md-0 mr-md-3">
    <a class="p-2 text-dark" href="#">Intranet</a>
    <a class="p-2 text-dark" href="#">HR Home</a>
    
</div>


<div class="px-3 py-3 mx-auto text-center pricing-header pt-md-5 pb-md-4">
  <h1 class="display-4">Pay Portal</h1>
  <h2 class="display-6">Mark Qwocco</h2>

  <p class="lead"></p>

  <form method="get" action="/">
  <div class="input-group">
   <!-- <input class="form-control"  type="text" name="id"> -->
   <input class="form-control"  type="text" name="period" placeholder="Filter by Period">
   <span class="input-group-btn">
        <button class="btn btn-primary" type="submit">Search</button>
   </span>
  </div>
  </form>
</div>
  
<?php if ($error != "") { ?>
<div class="container">
  <div class="mb-12">
    <div class="alert alert-danger" role="alert">
      <?php echo $error; ?>
    </div>
  </div>
</div>
<?php } ?>

<div class="container">
 <div class="mb-12">
  <table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Staff ID</th>
      <th scope="col">First</th>
      <th scope="col">Last</th>
      <th scope="col">Title</th>
      <th scope="col">Period</th>
      <th scope="col">Gross</th>
      <th scope="col">Net</th>
    </tr>
  </thead>
  <tbody>
    <?php foreach($databaseTest as $row): ?>
            <tr>
              <th scope="row" name='id'><?= $row->id ?></th>
              <td name='first'><?= $row->first ?></td>
              <td name='last'><?= $row->last ?></td>
              <td name='title'><?= $row->title ?></td>
              <td name='period'><?= $row->period ?></td>
              <td name='gross'><?= $row->gross ?></td>
              <td name='net'><?= $row->net ?></td>
            </tr>
    <?php endforeach; ?>

  </tbody>
</table>
	</div>
</div>

<div class="container">
  
  <footer class="pt-4 my-md-5 pt-md-5 border-top">
  </footer>
</div>
</body>
</html>
