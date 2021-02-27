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
    constructor(firstName, lastInitial, notes, checkInBy, checkInTime, daysLeft, checkedIn) {
        this.firstName = firstName; // e.g. "Fredrick"
        this.lastInitial = lastInitial; // e.g. "T."
        this.notes = notes; // e.g. working in taiwan. check in about fulbright cohort!
        this.checkInBy = checkInBy; // e.g. "01/22/21" (MM/DD/YY)
        this.checkInTime = checkInTime; // e.g. "3:00pm"
        this.daysLeft = daysLeft; // e.g. "3 days left"
        this.checkedIn = checkedIn; // e.g. boolean; default is false (pending) and toggled to true (complete)
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

    //notes input will have no additional formatting; just plain string data e.g. 'sample note'
    this.notes = document.getElementById("notes-input").value;
    //checkInBy will also be displayed as is inputted (via calendar widget or manual entry) e.g. 'YYYY-MM-DD'
    this.checkInBy = document.getElementById("check-in-by").value;

    this.checkInTime = document.getElementById("check-in-time").value;

    //set checkedIn default value to false (i.e. "pending")
    //and staged for 'click' eventlistener that will convert it "complete"
    this.checkedIn = false;
    //adding custom variable to count days left till assigned check-in date:
    this.daysLeft = `${calculateDueDate(this.checkInBy)}`;

    //newProfile to be created and populated with the grabbed user input
    newProfile = new Profile(firstName, lastInitial, notes, checkInBy, checkInTime, daysLeft, checkedIn);
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


const saveToLocalStorage = () => {
    localStorage.setItem(`profilesList`, JSON.stringify(profilesList));
}

//preventing user from selecting past date on date input (further info. in COMMENTS)
const today = new Date().toISOString().split("T")[0];
document.getElementsByName("checkinby")[0].setAttribute("min", today);


const render = () => {
    const cardContainer = document.getElementById("card-container");
    const profiles = document.querySelectorAll(".profile");

    profiles.forEach(profile => cardContainer.removeChild(profile));

    //earmark for debug item-- sorting by checkInDate (and possibly checkInTime)
    let profilesListSorted = [];



    for (i = 0; i < profilesList.length; i++) {
        createProfile(profilesList[i]);
    }
}

//createProfile function enables user input to be displayed as profile cards.
const createProfile = (item) => {
    const cardContainer = document.getElementById("card-container");
    const profileDiv = document.createElement("div");
    const nameDiv = document.createElement("div");
    const dateTextDiv = document.createElement("div");
    const dateDiv = document.createElement("div");
    const timeDiv = document.createElement("div");
    const notesSpan = document.createElement("span");
    const daysLeftDiv = document.createElement("div");
    const btnWrapper = document.createElement("div");
    const checkedInBtn = document.createElement("button");
    const clearBtn = document.createElement("button");

    //shaping the profile with .card & indexing each profile

    //if the contact is past-due on CheckedIn, paint the card container red!
    if ((dayjs(item.checkInBy).diff(dayjs(), "days", true)) <= -1) {
        profileDiv.classList.add("profile");
        profileDiv.classList.add("overdue");
        nameDiv.classList.add("name");
        nameDiv.classList.add("nameOverDue")
    } else {
        profileDiv.classList.add("profile");
        nameDiv.classList.add("name")
    }
    //populating the name div with user-input contact name
    nameDiv.textContent = `${item.firstName} ${item.lastInitial}`
    //indexing each contact for ease-of-reference
    profileDiv.setAttribute("id", profilesList.indexOf(item));

    profileDiv.appendChild(nameDiv)

    //then the dateText (a.k.a. "check-in by:" string)
    dateTextDiv.classList.add("datetext");
    dateTextDiv.textContent = "check in by:"
    profileDiv.appendChild(dateTextDiv);

    //next comes date
    dateDiv.classList.add("date");
    dateDiv.textContent = `${dayjs(item.checkInBy).format("MMM D")}`;
    profileDiv.appendChild(dateDiv);

    //next, the time of CheckIn
    timeDiv.classList.add("time");
    console.log(item.checkInTime);

    //firstly, checking that item.checkInTime input exists;
    //this is the debug solution to item.checkInTime.slice() method throwing an error on undefined
    //when no profile has been added to localstorage.
    if (!item.checkInTime) {
        return;
    }
    //formatting the time input raw value (e.g. "23:30")
    //to more palatable format (e.g. "11:30pm")
    let checkInHourStr = item.checkInTime.slice(0,2); //grabbing hour (00 to 23)
    //converting hour to int in order to perform int calculations for am/pm determination
    let checkInHourInt = parseInt(checkInHourStr);
    let checkInMinutes = item.checkInTime.slice(3); // grabbing minutes (00 to 59)

    let formattedTime = "";
    console.log(checkInHourInt); //str "00" to "12"
    console.log(typeof checkInHourInt)
    console.log(checkInMinutes);

    if (checkInHourInt == 0) {
        checkInHourInt = 12;
        formattedTime = `${checkInHourInt}:${checkInMinutes}am`;
    }
    else if (checkInHourInt < 13) {
        checkInHourInt.toString();
        formattedTime = `${checkInHourInt}:${checkInMinutes}am`;
    } else {
        checkInHourInt -= 12; //format "23" to "11"
        formattedTime = `${checkInHourInt}:${checkInMinutes}pm`;
    }

    timeDiv.textContent = formattedTime;
    profileDiv.appendChild(timeDiv);

    //next, display text for daysLeft
    daysLeftDiv.classList.add("daysLeft");
    daysLeftDiv.textContent = calculateDueDate(item.checkInBy);
    console.log(daysLeftDiv.textContent);
    profileDiv.appendChild(daysLeftDiv);

    //next, add the notes display ('↠ notes ↞', with content available on mouseover)
    notesSpan.classList.add("notes");
    notesSpan.textContent = "↠note↞";
    if (item.notes) {
        //setting the aria-label attribute will display note text when mouse-hovered
        notesSpan.setAttribute("aria-label", item.notes);
    }
    else {
        notesSpan.setAttribute("aria-label", "n/a");
    }
    profileDiv.appendChild(notesSpan);

    //add button wrapper to encapsulate the two btns and have them aligned side-by-side
    btnWrapper.classList.add("btnwrapper");
    profileDiv.appendChild(btnWrapper);

    //next, format the checkedInBtn
    checkedInBtn.classList.add("checkedinbtn");
    if (!item.checkedIn) {
        checkedInBtn.textContent = "pending"
        checkedInBtn.style.backgroundColor = "#768a80";
    } else {
        checkedInBtn.textContent = "complete";
        checkedInBtn.style.backgroundColor = "#607bbd";
    }
    btnWrapper.appendChild(checkedInBtn);

    //lastly, format the clearBtn
    clearBtn.classList.add("clearbtn");
    clearBtn.textContent = "clear";
    clearBtn.setAttribute("id", "clearBtn")
    btnWrapper.appendChild(clearBtn);

    //finally, adding the fully-done profileDiv to the list (#card-container)
    cardContainer.appendChild(profileDiv);

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
