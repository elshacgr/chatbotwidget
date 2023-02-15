<?php
include("../../setup/config.php");
include("../../setup/firebaseRDB.php");

if(isset($_SESSION['admin'])) {
    unset($_SESSION['admin']);
} 

header("location: ../loginPage/login.php");