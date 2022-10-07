importScripts("https://www.gstatic.com/firebasejs/7.16.1/firebase-app.js");
importScripts(
    "https://www.gstatic.com/firebasejs/7.16.1/firebase-messaging.js",
);
// For an optimal experience using Cloud Messaging, also add the Firebase SDK for Analytics.
importScripts(
    "https://www.gstatic.com/firebasejs/7.16.1/firebase-analytics.js",
);

// Initialize the Firebase app in the service worker by passing in the
// messagingSenderId.
firebase.initializeApp({
    apiKey: "AIzaSyD688MiH0zCmR8E4Eai9h9AGHR1tmFPdVI",
    authDomain: "sample-devinhouse-eb8a8.firebaseapp.com",
    databaseURL: "https://sample-devinhouse-eb8a8-default-rtdb.firebaseio.com",
    projectId: "sample-devinhouse-eb8a8",
    storageBucket: "sample-devinhouse-eb8a8.appspot.com",
    messagingSenderId: "801260524042",
    appId: "1:801260524042:web:e9aa66e44cb2be7a2b85f3",
    measurementId: "G-W42PEXWTCF"
});

// Retrieve an instance of Firebase Messaging so that it can handle background
// messages.
const messaging = firebase.messaging();

messaging.setBackgroundMessageHandler(function (payload) {
    console.log(
        "[firebase-messaging-sw.js] Received background message ",
        payload,
    );
    // Customize notification here
    const notificationTitle = "Background Message Title";
    const notificationOptions = {
        body: "Background Message body.",
        icon: "/itwonders-web-logo.png",
    };

    return self.registration.showNotification(
        notificationTitle,
        notificationOptions,
    );
});

let enableForegroundNotification = true;
messaging.onMessage(function (payload) {
    console.log('Message received. ', payload);
    notisElem.innerHTML = notisElem.innerHTML + JSON.stringify(payload);

    if (enableForegroundNotification) {
        let notification = payload.notification;
        navigator.serviceWorker
            .getRegistrations()
            .then((registration) => {
                registration[0].showNotification(notification.title);
            });
    }
});