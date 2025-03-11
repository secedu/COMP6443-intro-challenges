<html>

<head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css" />

    <title>QuoccaCorp PHP Up!</title>
</head>

<body>
    <main class="container">
        <nav>
            <ul>
                <li><strong>QuoccaCorp PHP Up!</strong></li>
            </ul>
            <ul>
                <li><a href="/admin.php">Admin</a></li>
                <li><a href="/">Home</a></li>
            </ul>
        </nav>

        <h1>Here at Quoccacorp, we love writing PHP servers that let you upload files! Try it now!</h1>

        <form action="upload.php" method="POST" enctype="multipart/form-data">
            <label for="file">Choose file:</label>
            <input type="file" name="file" id="file" required>
            <br><br>
            <input type="submit" value="Upload File">
        </form>
    </main>
</body>

</html>