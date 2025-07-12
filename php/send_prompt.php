<?php
$prompt = $_POST['prompt'] ?? '';

if (!empty($prompt)) {
    file_put_contents('../python/prompt.txt', $prompt);

    $response_file = '../python/response.txt';
    while (!file_exists($response_file)) {
        usleep(500000); // wait 0.5 sec
    }

    $response = file_get_contents($response_file);
    unlink($response_file);

    echo "<h2>ChatGPT Response:</h2><pre>$response</pre>";
}
?>

<form method="post">
    <textarea name="prompt" rows="4" cols="50" placeholder="Enter your prompt here..."></textarea><br>
    <button type="submit">Send</button>
</form>
