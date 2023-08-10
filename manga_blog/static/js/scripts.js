
const filterBlock = document.getElementById("filterBlock");
const toggleFilterBtn = document.getElementById("toggleFilterBtn");

toggleFilterBtn.addEventListener("click", function () {
    if (filterBlock.style.display === "none") {
        filterBlock.style.display = "block";
    } else {
        filterBlock.style.display = "none";
    }
});




