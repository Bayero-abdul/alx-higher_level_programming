$(document).ready(function () {
	// Add click event handler for INPUT#btn_translate
	$('INPUT#btn_translate').click(function () {
		const languageCode = $('INPUT#language_code').val();
		console.log(languageCode);
	
		$.ajax({
			url: 'https://cors-anywhere.herokuapp.com/https://www.fourtonfish.com/hellosalut/hello/',
			type: 'GET',
			dataType: 'json',
			data: { lang: languageCode },
			success: function(response) {
				$('DIV#hello').text(response.hello);
			},
			error: function () {
				$('DIV#hello').text('Translation not available');
			}
		});
	});
});
