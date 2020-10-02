const url_backend = 'http://127.0.0.1:5000/add_equipment/';

$(function(){  
    get_info();

    $('#add_equipment').click(function(){
        post_info();
    });
});

function get_info(){
    var url = url_backend;
    var timeout = 10000;
    var error_timeout = 'Внимание! Время ожидания ответа сервера истекло';
    var error_default = 'Внимание! Произошла ошибка, попробуйте отправить информацию еще раз';
    
    $.ajax({
        type: 'GET',
        url: url,
        dataType: 'JSON',
        timeout: timeout,
        success: function(data){
            $.each(data, function(key, value) {
                $('.type_equipment').append('<option value="' + key + '">' + value + '</option>');
            });
        },
        error: function(request, error){
            if (error == "timeout") {
                alert(error_timeout);
            }
            else {
                alert(error_default);
            }
        }
    });
    
}

function post_info(){
    var url = url_backend;
    var timeout = 10000;
    var error_timeout = 'Внимание! Время ожидания ответа сервера истекло';
    var error_default = 'Внимание! Произошла ошибка, попробуйте отправить информацию еще раз';
    data = { 
        'type_equipment': $('.type_equipment').val(),
        'textarea' : $('#textarea').val()
    };
    $.ajax({
        type: 'POST',
        url: url,
        dataType: 'JSON',
        timeout: timeout,
        contentType:"application/json",
        data: JSON.stringify(data),
        success: function(data){
            if(data['error'] === '')
            {
                alert('Все оборудование записано!');
            }   
            else
            {
                alert('Возникла ошибка в записи серийных номеров: ' + data['error']);
            }
        },
        error: function(request, error){
            if (error == "timeout") {
                alert(error_timeout);
            }
            else {
                alert(error_default);
            }
        }
    });
    
}
