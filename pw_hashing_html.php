<?php require 'script.php'; ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Tutorial</title>
</head>
<body>

    <h1>Please re-enter username and password</h1>

    <form action="" method="post" autocomplete="off">
        <label>Create a username</label>
        <input type="text" name="username">

        <label>Create a password</label>
        <input type="text" name="password">

        <button type="submit" name="record">Submit</button>

        <!-- Variable that displays if operation was successful -->
        <p class="error"><?php echo @$record_error; ?></p>
        <p class="success"><?php echo @$record_success; ?></p>
    </form>

</body>
</html>