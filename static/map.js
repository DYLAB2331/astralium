mapboxgl.accessToken = 'pk.eyJ1IjoiZHlsYW5uZ3V5ZW4yMzMxIiwiYSI6ImNsa3d4dHVsczAyemszc282Y3Z0cmNkMTAifQ.ZEakIyBGFJDAcowB9oi6WA';

function initMap(lon, lat) {
    var map = new mapboxgl.Map({
        container: 'map',
        style: 'mapbox://styles/mapbox/satellite-v9',
        center: [lon, lat],
        zoom: 4
    });

    var marker = new mapboxgl.Marker()
        .setLngLat([lon, lat])
        .addTo(map);
}

