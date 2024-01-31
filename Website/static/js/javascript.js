const cookieContainer = document.querySelector(".cookie-container");
const cookieButton = document.querySelector(".cookie-btn");
const modalPopup = document.getElementById("myModal");

cookieButton.addEventListener("click", () => {
    cookieContainer.classList.remove("active");
    localStorage.setItem("cookieBannerDisplayed", "true")
});

setTimeout(() => {
    if (!localStorage.getItem("cookieBannerDisplayed"))
        cookieContainer.classList.add("active");
}, 1000);

modalPopup.addEventListener("click", () => {
    localStorage.setItem("ModalDisplayed", "true")
});




