<html>

<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css" />

    <title>QuoccaCorp PHP Testimonials</title>
</head>

<body>
    <main class="container">
        <nav>
            <ul>
                <li><strong>QuoccaCorp PHP Testimonials</strong></li>
            </ul>
            <ul>
                <li><a href="/admin.php">Admin</a></li>
                <li><a href="/">Home</a></li>
            </ul>
        </nav>

        <h1>Take a look at our testimonials!</h1>

        <?php
            if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                echo "<p>Here is the testimonial!</p>";
                echo "<code>";
                system("cat testimonials/" . $_POST["t"] . " 2>&1 | sed -z 's/\\n/<br>/g'");
                echo "</code>";
            }
        ?>


        <p>Here are the available testemonials:</p>

        <code>
            <?php
                system("ls -l testimonials | sed -z 's/\\n/<br>/g'");
            ?>
        </code>

        <form action="/" method="POST">
            <label for="t">Enter testimonial:</label>
            <input type="text" name="t" id="t" required>
            <br><br>
            <input type="submit">
        </form>
    </main>
</body>

</html>