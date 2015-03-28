//not needed now
function getCoord(){
  lat=document.getElementById("getlat").value;
  lon=document.getElementById("getlon").value;
  alert(lat);
  var myCenter=new google.maps.LatLng(lat,lon);
  initialize(myCenter);
}
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