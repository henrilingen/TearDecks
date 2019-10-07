
$('button').on('click', funtion(event){
    event.preventDefault();
    var element = $(this);
    $.ajax({
        url : '/like_deck/',
        type : 'GET',
        data : { treasure_id : element.attr('data-id')},

        success : function(response){
                    element.html(' ' + response);
        }
    });
});
