<?php require("./login_action.php") ?>

<!DOCTYPE html>
<html lang="en">
<head>
    <title>Operator Login</title>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="../css/login.css">
    <?php
	 	if($email_error != null){
	 		?> <style>.email-error{display:block}</style> <?php
	 	}
	 	if($password_error != null){
	 		?> <style>.password-error{display:block}</style> <?php
	 	}
        if($email_not_regist != null){
            ?> <style>.email-not-regist{display:block}</style> <?php
        }
        if($password_not_match != null){
            ?> <style>.password-not-match{display:block}</style> <?php
        }
	 ?>
</head>
<body style="background:linear-gradient(to right, #7F53AC, #647DEE)  !important;">
    <section class="vh-100">
    <div class="container-fluid h-custom">
    <img src="../../logo.png" class="img" height="60" weight="60" style="background-color:white; border-radius:8px; box-shadow: 1px 1px; transform: translate(3%, 32%);">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-md-9 col-lg-6 col-xl-5">
            <img src="../../img/logo.svg"
            class="img-fluid" alt="Sample image">
        </div>
        <div class="col-md-8 col-lg-6 col-xl-4 offset-xl-1" style="background-color:white; border-radius:15px; box-shadow: 1px 1px;">
            <form  method="post" action="" autocomplete="off">
                <div class="d-flex flex-row align-items-center justify-content-center justify-content-lg-start">
                    <p class="lead fw-normal mb-0 me-3"><b>Login Page for Operator</b></p>
                </div>

                <br>
              
                 <!-- Pills navs -->
                 <ul class="nav nav-pills nav-justified mb-3" id="ex1" role="tablist">
                <li class="nav-item" role="presentation">
                    <a class="nav-link " id="tab-login" data-mdb-toggle="pill" href="../../admin/loginPage/login.php" role="tab"
                        aria-controls="pills-login" aria-selected="true"
                        style="background-color: #ece4fc; border-radius: 5px 0 0 5px; color:black">
                        Admin
                    </a>
                </li>
                <li class="nav-item" role="presentation">
                    <a class="nav-link active" id="tab-register" data-mdb-toggle="pill" href="./login.php" role="tab"
                        aria-controls="pills-register" aria-selected="false"
                        style="background-color: #866ec7;
                                        border-color: white;
                                        color: white;
                                        text-align: center;
                                        border-radius: 0 5px 5px 0;
                                        text-decoration: none;
                                        display: inline-block;
                                        font-size: 16px;">
                        Operator
                    </a>
                </li>
                </ul>

                <div class="divider d-flex align-items-center my-4"></div>

                <!-- Email input -->
                <div class="form-outline mb-4">
                    <label class="form-label" for="form3Example3">Email address</label>
                    <input 
                            type="email"
                            name="email"
                            id="form3Example3" 
                            class="form-control form-control-lg"
                            placeholder="Enter email address" 
                            value="<?php echo $email; ?>"
                    />
                    <p class="error email-error">
                        <?php echo $email_error; ?>
                    </p>
                    <p class="error email-not-regist">
                        <?php echo $email_not_regist; ?>
                    </p>
                </div>

                <!-- Password input -->
                <div class="form-outline mb-3">
                    <label class="form-label" for="form3Example4">Password</label>
                    <input 
                            type="password"
                            name="password" 
                            id="form3Example4" 
                            class="form-control form-control-lg"
                            placeholder="Enter password" 
                            value="<?php echo $password; ?>"
                    />
                    <p class="error password-error">
                            <?php echo $password_error; ?>
                    </p>
                    <p class="error password-not-match">
                            <?php echo $password_not_match; ?>
                    </p>
                </div>

                <!-- Log In -->
                <div class="text-center text-lg-start mt-4 pt-2">
                    <button 
                            type="submit" 
                            value="LOGIN"
                            name="login"
                            class="btn_save_train"
                            style="background-color: #866ec7;
                                    border: 15;
                                    border-color: white;
                                    color: white;
                                    padding: 10px 25px;
                                    text-align: center;
                                    transform: translate(125%, -10%); 
                                    border-radius: 5px;
                                    text-decoration: none;
                                    display: inline-block;
                                    font-size: 16px;">
                            LOGIN
                    </button>
                </div>
            </form>
        </div>
        </div>
    </div>
    </section>
</body>
</html>