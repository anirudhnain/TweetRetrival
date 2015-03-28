var x = document.getElementById("demo");
var lon;
var lat;
getLocation()
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.watchPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";}
    }
    
function showPosition(position) {
    lat=position.coords.latitude;
    lon=position.coords.longitude;
    x.innerHTML="Latitude: " + lat + "<br>Longitude: " + lon;
    var myCenter=new google.maps.LatLng(lat,lon);
    document.getElementById("coord").elements.item(0).value = lat+' '+lon; 
    document.getElementById("coord").submit();
}

//not needed now
function initialize(myCenter)
{
var mapProp = {
  center:myCenter,
  zoom:15,
  mapTypeId:google.maps.MapTypeId.ROADMAP
  };

var map=new google.maps.Map(document.getElementById("googleMap"),mapProp);

var marker=new google.maps.Marker({
  position:myCenter,
  });

marker.setMap(map);
}