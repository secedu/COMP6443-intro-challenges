<?php
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    if (isset($_FILES['file']) && $_FILES['file']['error'] == 0) {
        $file = $_FILES['file'];
        
        $fileName = $file['name'];
        $fileTmpName = $file['tmp_name'];
        $fileSize = $file['size'];
        $fileError = $file['error'];
        $fileType = $file['type'];
        
        $uploadDirectory = 'uploads/';

        $newFilePath = $uploadDirectory . basename($fileName);

        if (move_uploaded_file($fileTmpName, $newFilePath)) {
            echo "File uploaded successfully! <a href='" . $newFilePath . "'>Access it here</a>";
        } else {
            echo "There was an error uploading your file.";
        }
    } else {
        echo "File upload required";
    }
} else {
    echo "Wrong method";
}
?>
