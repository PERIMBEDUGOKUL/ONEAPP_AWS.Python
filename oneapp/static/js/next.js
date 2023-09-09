var form_fields = document.getElementsByTagName('input')
	for (var field in form_fields){	
		form_fields[field].className += ' form-control'
	}