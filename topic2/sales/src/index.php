<?php
error_reporting(E_ALL);
ini_set('display_errors', 'On');

$admin = false;

if (!isset($_COOKIE['metadata'])) {
    $str = base64_encode("admin=0");
    setcookie('metadata', $str);
    $_COOKIE['metadata'] = $str;
    $admin = false;
} else if (base64_decode($_COOKIE['metadata']) == "admin=1") {
    $admin = true;
}

if (!$admin) {
?>
    <!doctype html>
    <html lang="en">

    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <title>Sales dashboard - sign in</title>

        <!-- Bootstrap core CSS -->
        <link href="bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">


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
        <link href="signin.css" rel="stylesheet">
    </head>

    <body class="text-center">
        <form class="form-signin">
            <img class="mb-4" src="logo.svg" alt="" width="300" height="72" style="fill:#cecece;">
            <h1 class="mb-3 h3 font-weight-normal">Please sign in</h1>
            <label for="inputEmail" class="sr-only">Email address</label>
            <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
            <label for="inputPassword" class="sr-only">Password</label>
            <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
            <div class="mb-3 checkbox">
                <label>
                    <input type="checkbox" value="remember-me"> Remember me
                </label>
            </div>
            <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-muted">&copy; 1902-2020</p>
        </form>
    </body>

    </html>
<?php } else {
    // This block of code is for flag generation and is not part of the challenge.
    $jwt = file_get_contents('/run/secrets/flaganizer/sales/token');
    if ($jwt) {
        $opts = array(
            'http' => array(
                'method' => "GET",
                'header' => "Authorization: Bearer $jwt\r\n"
            )
        );
        $context = stream_context_create($opts);
        $params = http_build_query(array(
            'username' => $_SERVER["HTTP_X_MTLS_USERNAME"],
        ));
        $flaganizer = $_ENV['FLAGANIZER_URL'];
        $flag = json_decode(file_get_contents("$flaganizer/generate?$params", false, $context), true)["flag"];
    } else {
        $flag = "FLAG{sales}";
    }
?>

    <!doctype html>
    <html lang="en">

    <head>
        <title>Admin</title>

        <!-- Bootstrap core CSS -->
        <link href="bootstrap.min.css" rel="stylesheet">

        <!-- Custom styles for this template -->
        <link href="dashboard.css" rel="stylesheet">
    </head>

    <body>
        <nav class="p-0 navbar navbar-dark sticky-top bg-dark flex-md-nowrap">
            <a class="mr-0 navbar-brand col-sm-3 col-md-2" href="#">quoccacorp.</a>
            <input class="form-control form-control-dark w-100" type="text" placeholder="Search" aria-label="Search">
            <ul class="px-3 navbar-nav">
                <li class="nav-item text-nowrap">
                    <a class="nav-link" href="#">Sign out</a>
                </li>
            </ul>
        </nav>

        <div class="container-fluid">
            <div class="row">
                <nav class="col-md-2 d-none d-md-block bg-light sidebar">
                    <div class="sidebar-sticky">
                        <ul class="nav flex-column">
                            <li class="nav-item">
                                <a class="nav-link active" href="#">
                                    <span data-feather="home"></span>
                                    Sales Dashboard <span class="sr-only">(current)</span>
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="file"></span>
                                    Orders
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="shopping-cart"></span>
                                    Products
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="users"></span>
                                    Customers
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="bar-chart-2"></span>
                                    Reports
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="layers"></span>
                                    Integrations
                                </a>
                            </li>
                        </ul>

                        <h6 class="px-3 mt-4 mb-1 sidebar-heading d-flex justify-content-between align-items-center text-muted">
                            <span>Saved reports</span>
                            <a class="d-flex align-items-center text-muted" href="#">
                                <span data-feather="plus-circle"></span>
                            </a>
                        </h6>
                        <ul class="mb-2 nav flex-column">
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="file-text"></span>
                                    Current month
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="file-text"></span>
                                    Last quarter
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="file-text"></span>
                                    Social engagement
                                </a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">
                                    <span data-feather="file-text"></span>
                                    Year-end sale
                                </a>
                            </li>
                        </ul>
                    </div>
                </nav>

                <main role="main" class="px-4 pt-3 col-md-9 ml-sm-auto col-lg-10">
                    <div class="flex-wrap pb-2 mb-3 d-flex justify-content-between flex-md-nowrap align-items-center border-bottom">
                        <h1 class="h2">Sales Dashboard</h1>

                        <div class="mb-2 btn-toolbar mb-md-0">
                            <div class="mr-2 btn-group">
                                <button class="btn btn-sm btn-outline-secondary">Share</button>
                                <button class="btn btn-sm btn-outline-secondary">Export</button>
                            </div>
                            <button class="btn btn-sm btn-outline-secondary dropdown-toggle">
                                <span data-feather="calendar"></span>
                                This week
                            </button>
                        </div>
                    </div>
                    <h2 class="h4" style="color:#cecece;"><?php echo $flag; ?></h2>
                    <canvas class="my-4" id="myChart" width="900" height="380"></canvas>

                    <h2>Recent Orders</h2>
                    <div class="table-responsive">
                        <table class="table table-striped table-sm">
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>First</th>
                                    <th>Last</th>
                                    <th>Date</th>
                                    <th>Value</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>1,001</td>
                                    <td>Jane</td>
                                    <td>Caro</td>
                                    <td>12/1</td>
                                    <td>$5120</td>
                                </tr>
                                <tr>
                                    <td>1,002</td>
                                    <td>Bill</td>
                                    <td>Forth</td>
                                    <td>12/12</td>
                                    <td>$1220</td>
                                </tr>
                                <tr>
                                    <td>1,003</td>
                                    <td>Graham</td>
                                    <td>O'Neil</td>
                                    <td>10/10</td>
                                    <td>$2001</td>
                                </tr>
                                <tr>
                                    <td>1,003</td>
                                    <td>Jim</td>
                                    <td>Moland</td>
                                    <td>12/1</td>
                                    <td>$4012</td>
                                </tr>

                            </tbody>
                        </table>
                    </div>
                </main>
            </div>
        </div>

        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script>
            window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')
        </script>
        <script src="../../assets/js/vendor/popper.min.js"></script>
        <script src="../../dist/js/bootstrap.min.js"></script>

        <!-- Icons -->
        <script src="https://unpkg.com/feather-icons/dist/feather.min.js"></script>
        <script>
            feather.replace()
        </script>

        <!-- Graphs -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.1/Chart.min.js"></script>
        <script>
            var ctx = document.getElementById("myChart");
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
                    datasets: [{
                        data: [15339, 21345, 18483, 24003, 23489, 24092, 12034],
                        lineTension: 0,
                        backgroundColor: 'transparent',
                        borderColor: '#007bff',
                        borderWidth: 4,
                        pointBackgroundColor: '#007bff'
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: false
                            }
                        }]
                    },
                    legend: {
                        display: false,
                    }
                }
            });
        </script>
    </body>

    </html>
<?php } ?>