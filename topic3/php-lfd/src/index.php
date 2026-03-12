<html>

<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css" />

    <title>QuoccaCorp PHP LFD!</title>
</head>

<body>
    <main class="container">
        <nav>
            <ul>
                <li><strong>QuoccaCorp PHP LFD!</strong></li>
            </ul>
            <ul>
                <li><a href="/admin.php">Admin</a></li>
                <li><a href="/">Home</a></li>
            </ul>
        </nav>

        <h1>League of Fantastic Doodlers</h1>

        <?php
            $page = "1";

            if (isset($_GET["page"])) {
                $page = $_GET["page"];
            }

            echo file_get_contents("pages/" . $page);
        ?>
    </main>
</body>

</html>