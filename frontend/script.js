//a function that adds/removes display: hidden function of modal
const toggleModal = () => {
    document.querySelector(".modal") //selecting the modal element
    .classList.toggle("modal--hidden"); //call the classlist that hides the class
};

//eventlistener for when 'add contact' button is pressed
document.querySelector(".newProfile").addEventListener("click", toggleModal);

//another eventlistener for when "×" (close) button inside the modal is clicked
document.querySelector("#close").addEventListener("click", toggleModal);

//Object constructor for profile to-be-submitted
class Profile {
    constructor(firstName, lastInitial) {
        this.firstName = firstName; // e.g. "Fredrick"
        this.lastInitial = lastInitial; // e.g. "T."

    }
}

//profilesList is an array that will at once be populated by user input
//and later be saved to localStorage
let profilesList = [];

//initialising newProfile as an undefined variable on the global scope
//to be used locally in addProfileToList:
let newProfile;

//grabbing input values from 'add contact' form:
const addProfileToList = () => {
    //consoling out to debug function
    console.log("submitting new profile...");

    //firstname to be stored as a variable to be manipulated for formatting below
    let firstNameStr = document.getElementById("first-name").value;

    //firstname input to make sure formatted output is e.g. 'Firstname'
    this.firstName = firstNameStr[0].toUpperCase() + firstNameStr.substring(1).toLowerCase();
    //last initial input to be formatted to uppercase e.g. 'L'

    //stored as variable to check whether user has included a lastname or not
    //which will determine whether formatting is necessary or not
    let lastInitialStr = document.getElementById("last-name").value;

    //format the lastInitial from "c" to "C." if user inputs a lastInitial value
    if (lastInitialStr) {
        this.lastInitial = `${document.getElementById("last-name").value.toUpperCase()}.`
    //if user doesn't input a lastInitial, return empty str.
    } else {
        this.lastInitial = '';
    }

    //newProfile to be created and populated with the grabbed user input
    newProfile = new Profile(firstName, lastInitial);
    console.log(newProfile);

    //newly constructed profile to populate the profilesList array defined above
    profilesList.push(newProfile);

    //log profilesList array with the user input pushed as last index.
    console.log(profilesList);

    saveToLocalStorage();
    console.log("saved to local storage");
    render();
    form.reset();

    //final console.log to make sure function is working from top to bottom
    console.log("profile submitted successfully")
}

// event listener to add profile to list when form is submitted
const submitButton = document.getElementById("submit");

submitButton.addEventListener("click", (event) => {
    //preventDefault prevents the form from its default activity; adding to the root url with form input queries.
    event.preventDefault();
    addProfileToList();
    toggleModal();
});

//createProfile function enables user input to be displayed as profile cards.
const createProfile = (item) => {
    const cardContainer = document.getElementById("card-container");
    const profileDiv = document.createElement("div");
    const nameDiv = document.createElement("div");

    //eventlistener for when clear button is pressed
    clearBtn.addEventListener("click", () => {
        profilesList.splice(profilesList.indexOf(item),1);
        saveToLocalStorage();
        render();
    });

    //event listener for when checked in button is pressed
    checkedInBtn.addEventListener("click", () => {
        //when green pending btn is clicked, display the reverse state-- blue 'complete'
        item.checkedIn = !item.checkedIn;
        //making sure to save the new reversed logic to localStorage
        saveToLocalStorage();
        render();
    });
};


const restore = () => {
    if(!localStorage.profilesList) {
        render();
    }
    else {
        //get profilesList from localStorage in order to feed render() function with new profiles
        let objects = localStorage.getItem("profilesList");
        objects = JSON.parse(objects);
        profilesList = objects;
        render();
    }
}

restore();
