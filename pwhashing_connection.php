/* Connecting mysql to database */
/* DATABASE CONNECTION ================================================ */
$cann = new mysqli('localhost', 'admin', 'admin_pass', 'tutorials');
/* Checking post request */
/* PASSWORD ENCODING =================================================== */
if (isset($_POST['record'])) {
    /* Checking that empty values have been entered */
    if (!empty(trim($_POST['password'])) && !empty(trim($_POST['username']))) {
        /* When both fields have values, storing username & password in variables */
        $password = $_POST['password'];
        $username = $_POST['username'];
        /* Once values have been entered, password hash is created for the database */
        $enc_password = password_hash($password, PASSWORD_DEFAULT);
        /* Executing query, inserting password into the database */
        $cann->query("INSERT INTO users (username, password) VALUES('$username', '$enc_password')");
        /* Checking if the operation was successful */
        if ($cann->affected_rows != 1) {
            $record_error = 'Oops, something went wrong.';
        } else {
            $record_success = 'Password created and stored successfully.';
        }
    } else {
        $record_error = 'Please enter values in both fields.';
    }
}
/* Checking that empty values have been entered */
if (!empty(trim($_POST['password']))) {
    /* PASSWORD VALIDATION =================================================== */
}
?>
