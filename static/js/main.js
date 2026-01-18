function get_carousels() {
    const rc = document.getElementById("residential_carousel");
    const cc = document.getElementById("commercial_carousel");
    return [rc, cc];
}
function update_carousels_button() {
    const btn = document.getElementById("carousel_button");
    get_carousels().forEach(x => {
        const css = getComputedStyle(x);
        if (css.display === "none") {
            var banner = x.getElementsByClassName("banner")[0];
            btn.innerHTML = "View " + banner.innerHTML;
            btn.style.backgroundColor = getComputedStyle(banner).backgroundColor;
        }
    });
};
function swap_carousels() {
    get_carousels().forEach(x => {
        const css = getComputedStyle(x);
        if (css.display === "block") {
            x.style.display = "none";
        } else {
            x.style.display = "block";
        }
    });
    update_carousels_button();
}

window.addEventListener("load", function(){
    update_carousels_button();
    document.getElementById("carousel_button").addEventListener("click", swap_carousels);
});
