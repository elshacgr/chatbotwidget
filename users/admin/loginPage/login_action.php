<?php
include("../../setup/config.php");
include("../../setup/firebaseRDB.php");

$email = null;	
$password = null; 
$email_error = null;  
$password_error = null; 
$email_not_regist = null;
$password_not_match = null;

if(isset($_POST['log-in'])) {
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Next i will check for empty values so i have some kind of error to display.
    if(empty(trim($email))){
        // If there is an empty value i display an error message.
        $email_error = "Email is required";
    }else{
        // If the username has a value, then i move on to the password field.
        if(empty(trim($password))){
            $password_error = "Password is required";
        }
        else {
            $rdb = new firebaseRDB($databaseURL);
            $retrieve = $rdb->retrieve("/admin", "email", "EQUAL", $email);
            $data = json_decode($retrieve, 1);
  
            if(count($data) == 0) {
              $email_not_regist = "Sorry your not admin";
            }
            else{
              $id = array_keys($data)[0];
              if($data[$id]['password'] == $password) {
                  $_SESSION['admin'] = $data[$id];
                  header("location: ../../../evasbot/extractor/templates/php/historychat/index.php");
              } 
              else {
                  $password_not_match= "Please make sure your passwords match";
              }
            }
        }
    }
}