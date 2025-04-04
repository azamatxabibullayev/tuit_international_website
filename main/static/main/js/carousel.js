document.addEventListener("DOMContentLoaded", function() {
  const carousel = document.querySelector('.carousel');
  const leftBtn = document.querySelector('.carousel-nav.left');
  const rightBtn = document.querySelector('.carousel-nav.right');
  const itemWidth = document.querySelector('.carousel-item').clientWidth;

  rightBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: itemWidth, behavior: 'smooth' });
  });

  leftBtn.addEventListener('click', () => {
    carousel.scrollBy({ left: -itemWidth, behavior: 'smooth' });
  });
});
