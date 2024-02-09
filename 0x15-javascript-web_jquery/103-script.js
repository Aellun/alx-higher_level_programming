// fetches and prints how to say “Hello” depending on the language
$(document).ready(function() {
    function fetchTranslation() {
        var languageCode = $('#language_code').val();

        $.ajax({
            url: 'https://www.fourtonfish.com/hellosalut/hello/',
            method: 'GET',
            data: { lang: languageCode },
            success: function(data) {
                $('#hello').text(data.hello);
            },
            error: function(error) {
                console.error('Error fetching translation:', error);
            }
        });
    }

    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            fetchTranslation();
        }
    });
});
