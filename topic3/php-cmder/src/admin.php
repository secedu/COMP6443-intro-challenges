<?php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if(md5($_POST["pass"]) === trim(file_get_contents("/.password.txt.md5"))) {
        $url = getenv("FLAGANIZER_URL") . "/generate?username=" . urlencode($_SERVER['HTTP_X_MTLS_USERNAME']);

        $ch = curl_init($url);

        $headers = [
            "Authorization: Bearer " . file_get_contents("/run/secrets/flaganizer/php-cmder/token"),
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

<p>To prove you are the admin of this server, submit the password that is printed when you run the <code>/getpassword</code> binary on the disk</p>

<form action="admin.php" method="POST">
    <input type="password" name="pass">
    <input type="submit">
</form>