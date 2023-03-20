<script type="module">
  // Import the functions you need from the SDKs you need
  import { initializeApp } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/9.18.0/firebase-analytics.js";
  // TODO: Add SDKs for Firebase products that you want to use
  // https://firebase.google.com/docs/web/setup#available-libraries

  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  const firebaseConfig = {
    apiKey: "AIzaSyDJwvBBRzfmhjNsSEzd6OSedWkV_2cWfUY",
    authDomain: "internalmark-fec41.firebaseapp.com",
    projectId: "internalmark-fec41",
    storageBucket: "internalmark-fec41.appspot.com",
    messagingSenderId: "448216047277",
    appId: "1:448216047277:web:51d5aead05173f11cb7024",
    measurementId: "G-ZW9RJD703M"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);
</script>