document.addEventListener("DOMContentLoaded", function() {
    const carousel = document.querySelector('.carousel');
    let scrollAmount = 0;
    setInterval(() => {
        scrollAmount += 2;
        carousel.scrollTo({
            left: scrollAmount,
            behavior: 'smooth'
        });
        if (scrollAmount >= carousel.scrollWidth - carousel.clientWidth) {
            scrollAmount = 0;
        }
    }, 50);
});
