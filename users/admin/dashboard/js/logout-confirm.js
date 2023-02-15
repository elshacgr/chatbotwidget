$(doocument).ready(function() {
    // function to view modal
    function showMessageDialog(title, body) {
		document.getElementById('title-modal').innerHTML = ""+title;
		document.getElementById('body-modal').innerHTML = ""+body;
		var mes_diag = new bootstrap.Modal(document.getElementById('message-dialog'))
		mes_diag.show();
	}	
})