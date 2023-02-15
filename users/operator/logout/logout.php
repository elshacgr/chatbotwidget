<?php
include("../../setup/config.php");
include("../../setup/firebaseRDB.php");

if(isset($_SESSION['operator'])) {
    unset($_SESSION['operator']);
} 

header("location: ../loginPage/login.php");