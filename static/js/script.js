$(function(){
	var LAT = 13.30272;
	var LNG = -87.174107;

	if (navigator.geolocation)
	{
		navigator.geolocation.getCurrentPosition(getPosition, getError);
	} else {
		initialize(LAT, LNG);
	}

	function getPosition(position)
	{
		var lat = position.coords.latitude;
		var lng = position.coords.longitude;

		initialize(lat, lng);
	}

	function getError(err)
	{
		initialize(LAT, LNG);
	}

	function initialize(lat, lng)
	{
		var GLatLng = new google.maps.LatLng(lat, lng);

		var mapSettings = {
			center: GLatLng,
			zoom: 16,
			mapTypeId: google.maps.MapTypeId.SATELLITE
		}

		map = new google.maps.Map($('#mapa').get(0), mapSettings);

		var marker = new google.maps.Marker({
			position: GLatLng,
			map: map,
			draggable: true,
			title: 'Arrastrame!'
		});

		google.maps.event.addListener(marker, 'position_changed', function(){
			getMarkerCoords(marker);
		});
	}

	function getMarkerCoords(marker)
	{
		var markerCoords = marker.getPosition();
		$('#id_lat').val( markerCoords.lat() );
		$('#id_lng').val( markerCoords.lng() );
	}
});