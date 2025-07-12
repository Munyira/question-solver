<?php
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $text = $_POST["text"] ?? "";
    $ch = curl_init("http://localhost:5000/ask");
    curl_setopt_array($ch, [
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_POST => true,
        CURLOPT_HTTPHEADER => ["Content-Type: application/json"],
        CURLOPT_POSTFIELDS => json_encode(["text" => $text])
    ]);
    $response = curl_exec($ch);
    curl_close($ch);
    echo $response;
}
?>
