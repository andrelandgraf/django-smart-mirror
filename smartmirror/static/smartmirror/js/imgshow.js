window.images = [];
window.current = 0;
window.imageCount = document.getElementById("imgcount").innerHTML;

function loadNextImage(i, callback) {
    // https://wiki.selfhtml.org/wiki/JavaScript/XMLHttpRequest/
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            window.images.push("data:image/jpeg;base64," + xmlhttp.responseText);
            callback.call();
        }
    };
    xmlhttp.open('GET', "http://127.0.0.1:8000/mirror/img/"+i);
    xmlhttp.send(null);
}

// Increments the image counter and loads the image if needed.
function stepImage() {
    // If we have reached the end of the images, restart.
    if(window.current >= window.imageCount){
        window.current = 0;
    }
    // Make sure that the image is loaded in the images array,
    // if not, load the image, then show it.
    if(window.images.length <= window.current) {
        loadNextImage(window.current, showImage);
    }
    // If it's already loaded, just show it.
    else showImage();
}

// Displays an image onto the page.
function showImage() {
  document.getElementById('imgshow').src = window.images[window.current];
  // The counter is not incremented until the image is shown!
  window.current++;
}

// Set a timer to render future images.
setInterval(stepImage, 3000);

// Render the first image.
stepImage();

