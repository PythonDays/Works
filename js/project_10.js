let map;
let markers = [];
let polylines = [];

function loadGoogleMapsScript() {
  const script = document.createElement("script");
  script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyB6bRbu7plrXP8WkclcAWCpHKAuDYzgY9I&callback=initMap&v=weekly";
  script.defer = true;

  document.head.appendChild(script);
}

function initMap() {
  const coordinates = { lat: 40.689, lng: -74.044 };
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 13,
    center: coordinates,
  });
  // Call your functions here
  displayInfoWindow(coordinates.lat, coordinates.lng);
  placeMarker(coordinates.lat, coordinates.lng);
  clearMarkers();
  // getPath(origin, destination); // Make sure to provide values for origin and destination
  placeCircle(coordinates.lat, coordinates.lng, 100); // Example radius: 100 meters
  placeRectangle(coordinates.lat, coordinates.lng, 0.02, 0.01); // Example width: 0.02, height: 0.01 (degrees)
  placePolygon("40.689 -74.044, 40.691 -74.043, 40.688 -74.041"); // Example polygon coordinates

  // For testing the alert, you can uncomment the following line:
  // map.addListener("click", showCoordinatesAlert);
}

function displayInfoWindow(lat, lng) {
  const infoWindow = new google.maps.InfoWindow({
    content: `Latitude: ${lat}, Longitude: ${lng}`,
  });

  const marker = new google.maps.Marker({
    position: { lat, lng },
    map: map,
  });

  marker.addListener("click", () => {
    infoWindow.open(map, marker);
  });

  markers.push(marker);
}

function placeMarker(lat, lng) {
  clearMarkers();

  const marker = new google.maps.Marker({
    position: { lat, lng },
    map: map,
  });

  markers.push(marker);
  map.setCenter(marker.getPosition());
}

function clearMarkers() {
  markers.forEach((marker) => {
    marker.setMap(null);
  });

  markers = [];
}

function getPath(origin, destination) {
  const directionsService = new google.maps.DirectionsService();
  const directionsRenderer = new google.maps.DirectionsRenderer({
    map: map,
  });

  directionsService.route(
    {
      origin: origin,
      destination: destination,
      travelMode: google.maps.TravelMode.DRIVING,
    },
    (response, status) => {
      if (status === "OK") {
        directionsRenderer.setDirections(response);
      } else {
        alert("Directions request failed due to " + status);
      }
    }
  );
}

function placeCircle(lat, lng, radius) {
  const circle = new google.maps.Circle({
    strokeColor: "blue",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#FFF",
    fillOpacity: 0.5,
    map: map,
    center: { lat, lng },
    radius: parseFloat(radius),
  });

  map.setCenter(circle.getCenter());
}

function placeRectangle(lat, lng, width, height) {
  const bounds = {
    north: lat + parseFloat(height) / 2,
    south: lat - parseFloat(height) / 2,
    east: lng + parseFloat(width) / 2,
    west: lng - parseFloat(width) / 2,
  };

  const rectangle = new google.maps.Rectangle({
    strokeColor: "blue",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#FFF",
    fillOpacity: 0.5,
    map: map,
    bounds: bounds,
  });

  map.setCenter(rectangle.getBounds().getCenter());
}

function placePolygon(coords) {
  const coordinates = coords
    .split(",")
    .map((coord) => {
      const [lat, lng] = coord.trim().split(" ");
      return { lat: parseFloat(lat), lng: parseFloat(lng) };
    });

  const polygon = new google.maps.Polygon({
    paths: coordinates,
    strokeColor: "blue",
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: "#FFF",
    fillOpacity: 0.5,
    map: map,
  });

  const bounds = new google.maps.LatLngBounds();
  coordinates.forEach((coordinate) => {
    bounds.extend(coordinate);
  });
  map.fitBounds(bounds);
}
// Place Marker form submission
document.getElementById("markerForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const lat = parseFloat(document.getElementById("markerLat").value);
  const lng = parseFloat(document.getElementById("markerLng").value);
  placeMarker(lat, lng);
});

// Get Path form submission
document.getElementById("pathForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const origin = document.getElementById("origin").value;
  const destination = document.getElementById("destination").value;
  getPath(origin, destination);
});

// Place Circle form submission
document.getElementById("circleForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const lat = parseFloat(document.getElementById("circleLat").value);
  const lng = parseFloat(document.getElementById("circleLng").value);
  const radius = parseFloat(document.getElementById("circleRadius").value);
  placeCircle(lat, lng, radius);
});

// Place Rectangle form submission
document.getElementById("rectangleForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const lat = parseFloat(document.getElementById("rectangleLat").value);
  const lng = parseFloat(document.getElementById("rectangleLng").value);
  const width = parseFloat(document.getElementById("rectangleWidth").value);
  const height = parseFloat(document.getElementById("rectangleHeight").value);
  placeRectangle(lat, lng, width, height);
});

// Place Polygon form submission
document.getElementById("polygonForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const coords = document.getElementById("polygonCoords").value;
  placePolygon(coords);
});

// Place Polylines form submission
document.getElementById("polylineForm").addEventListener("submit", function (event) {
  event.preventDefault();
  const coords1 = document.getElementById("polylineCoords1").value;
  const coords2 = document.getElementById("polylineCoords2").value;
  placePolyline(coords1, coords2);
});

loadGoogleMapsScript();
