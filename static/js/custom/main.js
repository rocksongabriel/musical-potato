// Prevent the form from getting submitted if the user hasn't voted
let form = document.getElementById("vote-form");
let checkboxes = document.getElementsByClassName("input-checkbox");
let vote_buttons = document.getElementsByClassName("checkbox-btn");
let labels = document.getElementsByClassName("checkbox-label");
voted_labels = document.getElementsByClassName("voted-label");

form.addEventListener("submit", (event) => {
    let all_checked = false;
    for (checkbox of checkboxes) {
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
for (checkbox of checkboxes) {
    checkbox.addEventListener("change", (event) => {
        for (button of vote_buttons) {
            button.classList.add("pointer-events-none");
        }
        for (label of labels) {
            label.classList.add("opacity-80");
        }

        for (checkbox of checkboxes) {
            if (checkbox.checked) {
                identifier_class = checkbox.classList[0]; // the classname to get he voted label to display
                for (voted_label of voted_labels) {
                    if (voted_label.classList.contains(identifier_class)) {
                        voted_label.classList.remove("hidden");
                    }
                }
            }
        }
    })
}

