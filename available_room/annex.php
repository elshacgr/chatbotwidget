<?php
include("firebaseRDB.php");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto|Varela+Round">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

    <title>Document</title>
</head>
<body style="background:linear-gradient(to right, #7F53AC, #647DEE); max-width:100%; position:fix; overflow: -moz-scrollbars-horizontal; overflow-y: auto; overflow-x: hidden;">
    <div id="content" style="background:linear-gradient(to right, #7F53AC, #647DEE);"class="p-4 p-md-5 pt-5">
    <h5 style="color: white; transform: translate(30%, 5%); font-size:50px;"><b>Annex's Availability Room</b></h5>
        <div class="container"  style="background:white; height:3050px; transform: translate(0%, 1%); border-radius:5px">
        <div style="height:50%">
            <table class="table table-bordered"  border="1" width="500" style="transform: translate(0%, 1%);">
                <thead class="text-center" style="background-color: white; color:black ">
                    <tr>
                        <th>Asrama</th>
                        <th>Room Number</th>
                        <th>Bed Position</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="table-intent">
                    <?php
                        $databaseURL = "https://availabilitydb-default-rtdb.firebaseio.com";
                        $db = new firebaseRDB($databaseURL);

                        // tarik data dari firebase chats
                        $data = $db->retrieve("available/annex");

                        $data = json_decode($data,1);
                        if(is_array($data)){
                            $i=0;
                            $new_var=0;
                            foreach($data as $id => $chat){
                                $i = 0;

                                if ($i < 4)
                                {
                                    $y= $chat['1 a'];

                                    $default_color = "table-success";

                                    if($y['status'] == "not avail"){
                                        $default_color = "table-danger";}
                                    echo "
                                    <tr class={$default_color}>
                                        <td>{$y['asrama']}</td>
                                        <td>{$y['no_kamar']}</td>
                                        <td>{$y['no_bed']}</td>
                                        <td>{$y['status']}</td>
                                    
                                    </tr> ";
                                    $i = $i+1;
                                }
                                if ($i < 4)
                                {
                                    $y = $chat['1 b'];
                                    $default_color = "table-success";

                                    if($y['status'] == "not avail"){
                                        $default_color = "table-danger";}
                                    echo "
                                    <tr class={$default_color}>
                                        <td>{$y['asrama']}</td>
                                        <td>{$y['no_kamar']}</td>
                                        <td>{$y['no_bed']}</td>
                                        <td>{$y['status']}</td>
                                    
                                    </tr> ";
                                    $i = $i+1;
                                }
                                if ($i < 4)
                                {
                                    $y = $chat['2 a'];
                                    $default_color = "table-success";

                                    if($y['status'] == "not avail"){
                                        $default_color = "table-danger";}
                                    echo "
                                    <tr class={$default_color}>
                                        <td>{$y['asrama']}</td>
                                        <td>{$y['no_kamar']}</td>
                                        <td>{$y['no_bed']}</td>
                                        <td>{$y['status']}</td>
                                    
                                    </tr> ";
                                    $i = $i+1;
                                }

                                if ($i < 4)
                                {
                                    $y = $chat['2 b'];
                                    $default_color = "table-success";

                                    if($y['status'] == "not avail"){
                                        $default_color = "table-danger";}
                                    echo "
                                    <tr class={$default_color}>
                                        <td>{$y['asrama']}</td>
                                        <td>{$y['no_kamar']}</td>
                                        <td>{$y['no_bed']}</td>
                                        <td>{$y['status']}</td>
                                    
                                    </tr> ";
                                    $i = $i+1;
                                }
                                $j = 0;
                                if ($j < 4)
                                {
                                    $y = $chat['3 a'];
                                    $default_color = "table-success";

                                    if($y['status'] == "not avail"){
                                        $default_color = "table-danger";}
                                    echo "
                                    <tr class={$default_color}>
                                        <td>{$y['asrama']}</td>
                                        <td>{$y['no_kamar']}</td>
                                        <td>{$y['no_bed']}</td>
                                        <td>{$y['status']}</td>
                                    
                                    </tr> ";
                                    $i = $i+1;
                                }
                            }                                                                
                        }
                    ?>
                </tbody>
            </table>
                </div>
        </div>
    </div>
</body>
</html>
