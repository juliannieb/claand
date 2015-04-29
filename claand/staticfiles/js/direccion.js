$('#id_estado').change(function() {
	$('#id_municipio').load('{% url get_municipios %}', {estado_id: $(this).value()})
});

$('#likes').change(function(){
    var catid;
    catid = $(this).value();
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});
