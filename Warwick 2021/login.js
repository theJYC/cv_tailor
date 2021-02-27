
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyCAlWxVrlsEraDPWjTjmvfTdOf1MBh5FRI",
    authDomain: "cv-tailor-2021.firebaseapp.com",
    projectId: "cv-tailor-2021",
    storageBucket: "cv-tailor-2021.appspot.com",
    messagingSenderId: "517913762495",
    appId: "1:517913762495:web:c56701dafe7ed4d6c1040a",
    measurementId: "G-ZGLEKWHNNX"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();

const auth =firebase.auth();

function signup(){
  var email = document.getElementById("email");
  var password = document.getElementById("password");

  const promise = auth.createUserWithEmailAndPassword(email.value, password.value);
  promise.catch (e => alert(e.message));

  alert("SignedIn");

}