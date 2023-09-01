// Function to play the audio associated with a specific ID
function playAudio(audioId) {
    var audio = document.getElementById(audioId);
    if (audio) {
        audio.play();
    }
}

// Handle audio playback errors
document.querySelector('audio').addEventListener('error', function (e) {
    console.error('Audio playback error:', e);
});

// Add a click event listener to the button with the id "principito-button-1"
document.getElementById("principito-button-1").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-1";
});

// Add a click event listener to the button with the id "principito-button-2"
document.getElementById("principito-button-2").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-2";
});

// Add a click event listener to the button with the id "principito-button-3"
document.getElementById("principito-button-3").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-3";
});

// Add a click event listener to the button with the id "principito-button-4"
document.getElementById("principito-button-4").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-4";
});

// Add a click event listener to the button with the id "principito-button-5"
document.getElementById("principito-button-5").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-5";
});

// Add a click event listener to the button with the id "principito-button-6"
document.getElementById("principito-button-6").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-6";
});

// Add a click event listener to the button with the id "principito-button-7"
document.getElementById("principito-button-7").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route
    window.location.href = "/p-book-7";
});

// Add a click event listener to the button with the id "stella-button"
document.getElementById("stella-button").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route for Stella
    window.location.href = "/stella-audio-book";
});

// Add a click event listener to the button with the id "les-miserables-button"
document.getElementById("les-miserables-button").addEventListener("click", function() {
    // No need to prevent default behavior
    // Make a simple link to your Flask route for Les Miserables
    window.location.href = "/les-m-book";
});
