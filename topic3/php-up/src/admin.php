<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if($_POST["pass"] === file_get_contents("/password.txt")) {
        $url = getenv("FLAGANIZER_URL") . "/generate?username=" . urlencode($_SERVER['HTTP_X_MTLS_USERNAME']);

        $ch = curl_init($url);

        $headers = [
            "Authorization: Bearer " . file_get_contents("/run/secrets/flaganizer/php-up/token"),
            "User-Agent: pyquocca"
        ];

        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($ch, CURLOPT_HEADER, false);

        $response = curl_exec($ch);

        if($response === false) {
            echo "cURL Error: " . curl_error($ch);
        } else {
            echo "Response: " . json_decode($response, true)["flag"];
        }

        curl_close($ch);
    } else {
        echo "WRONG!";
    }
}
?>

<p>To prove you are the admin of this server, submit the password stored at <code>/password.txt</code> on the disk</p>

<form action="admin.php" method="POST">
    <input type="password" name="pass">
    <input type="submit">
</form>