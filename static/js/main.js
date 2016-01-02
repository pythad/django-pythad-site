function getCookie(name) {
	var matches = document.cookie.match(new RegExp(
		"(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
	));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}

$(document).ready(function() {
	$('#subscribe-form').on('submit', function(event) {
		event.preventDefault();
		var csrftoken = getCookie('csrftoken')
		var email = $('#subscriber-email').val()
		$.ajax({
			url: GLOBAL_VARS['subscribeUrl'],
			type: "POST",
			data: {
				'email': email,
				'csrfmiddlewaretoken': csrftoken
			},
			success: function(json) {
				if (json['status'] == 'ok') {
					toastr.success('You have successfully signed up for the newsletter');
				} else {
					toastr.warning('It seems that this email is already in our database');
				};
			},
			error: function(xhr, errmsg, err) {
				toastr.error(xhr.status + ": " + xhr.responseText);
			}
		});
	});
})