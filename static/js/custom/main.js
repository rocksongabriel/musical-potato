let toggle_btn = document.getElementById("nav-toggle");
let mobile_nav = document.getElementById("mobile-nav");

toggle_btn.addEventListener("click", (event) => {
    mobile_nav.classList.toggle("hidden")
})