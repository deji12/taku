const recipientUsername = 'tak'; // replace this with the actual recipient username

const websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";

const wsEndpoint = `${websocketProtocol}://${window.location.host}/ws/video_call/${recipientUsername}/`;

const socket = new WebSocket(wsEndpoint);

socket.onmessage = function(event) {
    const notification = JSON.parse(event.data);

    if (notification.type === 'video_call_request') {
        const roomName = notification.room_name;
        const caller = notification.caller;

        // Display a dialog to accept or reject the video call request
        // If the user accepts the call, call the acceptVideoCall function with the caller's username
        // If the user rejects the call, call the rejectVideoCall function with the caller's username
    }
};

function initiateVideoCall(recipientUsername) {
    fetch(`/initiate_video_call/${recipientUsername}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data =>{
        const roomName = data.room_name;

        // Initialize Agora SDK and join the channel with the generated roomName
    })
    .catch(error => console.error(error));
}

function acceptVideoCall(callerUsername) {
    fetch(`/accept_video_call/${callerUsername}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => {
        const roomName = data.room_name;

        // Initialize Agora SDK and join the channel with the generated roomName
    })
    .catch(error => console.error(error));
}

function rejectVideoCall(callerUsername) {
    fetch(`/reject_video_call/${callerUsername}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': '{{ csrf_token }}'
        }
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
}