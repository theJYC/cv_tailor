
  var firebaseConfig = {
    apiKey: "AIzaSyCAlWxVrlsEraDPWjTjmvfTdOf1MBh5FRI",
    authDomain: "cv-tailor-2021.firebaseapp.com",
    projectId: "cv-tailor-2021",
    storageBucket: "cv-tailor-2021.appspot.com",
    messagingSenderId: "517913762495",
    appId: "1:517913762495:web:9f4ac3a65dd391c8c1040a",
    measurementId: "G-X4HJHWK20N"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);


const auth =firebase.auth();

function signUp(){
  var email = document.getElementById("email");
  var password = document.getElementById("password");

  const promise = auth.createUserWithEmailAndPassword(email.value, password.value);
  promise.catch (e => alert(e.message));

  alert("Signed Up!!");

}

function signIn(){

  var email = document.getElementById("email");
  var password = document.getElementById("password");

  const promise = auth.signInWithEmailAndPassword(email.value, password.value);
  promise.catch (e => alert(e.message));

  alert("Welcome " + email.value);

}

function signOut(){
  
  auth.signOut();
  alert("Signed Out !!!");
}


firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    var email = user.email;
    alert("Active User" + email);
  } else {
    alert("No Active User");
  }
});