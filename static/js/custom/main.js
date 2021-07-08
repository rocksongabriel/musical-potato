// Prevent the form from getting submitted if the user hasn't voted
let form = document.getElementById("vote-form");

form.addEventListener("submit", (event) => {
    let all_checked = false;
    for (checkbox of document.getElementsByClassName("input-checkbox")) {
        all_checked = checkbox.checked || all_checked;
    }
    if (all_checked === true) {
        form.submit(); // submit the form if one checkbox has been checked
    } else {
        event.preventDefault(); // if the person hasn't voted for anyone, don't submit
        alert("You haven't voted for anyone");
    }
})


// Check if the user has clicked on a vote button
// If he has, disable all the buttons
