$(function(){
	var mapa = initialize(13.30272, -87.174107);

	function initialize(lat, lng)
	{
		var GLatLng = new google.maps.LatLng(lat, lng);

		var mapSettings = {
			center: GLatLng,
			zoom: 16,
			mapTypeId: google.maps.MapTypeId.ROADMAP
		}

		map = new google.maps.Map($('#mapa_ubicaciones').get(0), mapSettings);
		return map;	
	}

	$('.coords').each(function(){
		var latitud = $(this).attr('latitud');
		var longitud = $(this).attr('longitud');
		var nombre = $(this).attr('nombre');
		var id = $(this).attr('id');

		var GLatLng = new google.maps.LatLng(latitud, longitud);

		var marker = new google.maps.Marker({
			map: mapa,
			position: GLatLng,
			title: nombre
		});

		google.maps.event.addListener(marker, 'click', function(){
			document.location = '/sistema/mis_ubicaciones/'+id+'/';
		});
	});
});