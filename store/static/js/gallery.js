"use strict";
/**
 * Class representing a gallery.
 */
class Gallery {
  /**
   * Create a gallery.
   */
  constructor() {
    this.images = document.querySelectorAll(".gallery-wrapper img");
    this.currentIndex = 0;
    this.initGallery();
    this.initDots();
    this.initNavButtons();
    this.startAutoPlay();
  }

  /**
   * Initialize the gallery by setting data attributes and active class.
   */
  initGallery() {
    this.images.forEach((img, index) => {
      img.dataset.index = index;
      if (index === 0) img.classList.add("active");
    });
  }
  

  /**
   * Initialize the dots for navigation and add event listeners.
   */
initDots() {
  const dotsContainer = document.querySelector(".gallery-dots");
  if (!dotsContainer) {
    console.error("Gallery dots container not found!");
    return;
  }
  this.images.forEach((_, index) => {
    const dot = document.createElement("div");
    dot.classList.add("dot");
    if (index === 0) dot.classList.add("active");
    dot.addEventListener("click", () => this.goToSlide(index));
    dotsContainer.appendChild(dot);
  });
  this.dots = dotsContainer.querySelectorAll(".dot");
}

  /**
   * Initialize the navigation buttons and add event listeners.
   */
  initNavButtons() {
    document
      .querySelector(".prev-btn")
      .addEventListener("click", () => this.prevSlide());
    document
      .querySelector(".next-btn")
      .addEventListener("click", () => this.nextSlide());
  }

  /**
   * Go to a specific slide.
   *
   * @param {number} index - The index of the slide to go to.
   */
  goToSlide(index) {
    this.images[this.currentIndex].classList.remove("active");
    this.dots[this.currentIndex].classList.remove("active");
    this.currentIndex = index;
    this.images[this.currentIndex].classList.add("active");
    this.dots[this.currentIndex].classList.add("active");
  }

  /**
   * Go to the next slide.
   */
  nextSlide() {
    let nextIndex = (this.currentIndex + 1) % this.images.length;
    this.goToSlide(nextIndex);
  }

  /**
   * Go to the previous slide.
   */
  prevSlide() {
    let prevIndex =
      (this.currentIndex - 1 + this.images.length) % this.images.length;
    this.goToSlide(prevIndex);
  }

  /**
   * Start the autoplay functionality for the gallery.
   */
  startAutoPlay() {
    setInterval(() => this.nextSlide(), 5000);
  }
}

/**
 * Initialize the gallery once the DOM content is fully loaded.
 */
document.addEventListener("DOMContentLoaded", () => {
  const galleryWrapper = document.querySelector(".gallery-wrapper");
  if (galleryWrapper) {
    new Gallery();
  } else {}
});

