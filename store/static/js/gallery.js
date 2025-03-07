"use strict";
/**
 * gallery.js
 *
 * This script manages the image slider gallery.
 * It initializes the gallery by:
 *   - Cloning the single image if needed (to ensure multiple slides exist)
 *   - Setting up data attributes and the active class
 *   - Creating dot navigation
 *   - Attaching event listeners to previous/next buttons
 *   - Enabling autoplay functionality
 *
 * Expected HTML structure:
 * <div class="gallery-wrapper">
 *   <!-- Initially one image (via Django template) -->
 *   <img src="..." alt="..." class="thumbnail active">
 *   <div class="gallery-nav">
 *     <button class="prev-btn"><i class="fas fa-chevron-left"></i></button>
 *     <button class="next-btn"><i class="fas fa-chevron-right"></i></button>
 *   </div>
 *   <div class="gallery-dots"></div>
 * </div>
 */

class Gallery {
  /**
   * Create a Gallery instance.
   */
  constructor() {
    // Select all images within the gallery wrapper
    this.images = document.querySelectorAll(".gallery-wrapper img");

    // If only one image exists, clone it a couple of times so the slider works
    if (this.images.length < 2) {
      const galleryWrapper = document.querySelector(".gallery-wrapper");
      if (this.images.length === 1) {
        const originalImg = this.images[0];
        // Clone the image two times (adjust the number if needed)
        for (let i = 1; i <= 2; i++) {
          const clone = originalImg.cloneNode(true);
          // If using a placeholder, change the src to create variation
          if (originalImg.src.indexOf("picsum.photos") !== -1) {
            clone.src = `https://picsum.photos/800/400?random=${i + 1}`;
          }
          // Remove the active class from clones (only the original should be active)
          clone.classList.remove("active");
          galleryWrapper.appendChild(clone);
        }
      }
      // Update the images NodeList after cloning
      this.images = document.querySelectorAll(".gallery-wrapper img");
    }

    this.currentIndex = 0;
    this.initGallery();
    this.initDots();
    this.initNavButtons();
    this.startAutoPlay();
    console.log("Gallery initialized with", this.images.length, "images");
  }

  /* --------------------------------------------------------------------------
     Initialize Gallery
     - Sets data-index for each image.
     - Ensures the first image is active.
  -------------------------------------------------------------------------- */
  initGallery() {
    this.images.forEach((img, index) => {
      img.dataset.index = index;
      if (index === 0) {
        img.classList.add("active");
      } else {
        img.classList.remove("active");
      }
    });
  }

  /* --------------------------------------------------------------------------
     Initialize Dot Navigation
     - Creates a dot for each image.
     - Adds click event listeners to navigate to the corresponding slide.
  -------------------------------------------------------------------------- */
  initDots() {
    const dotsContainer = document.querySelector(".gallery-dots");
    if (!dotsContainer) {
      console.error("Gallery dots container not found!");
      return;
    }
    // Clear any existing dots (in case of reinitialization)
    dotsContainer.innerHTML = "";
    this.images.forEach((_, index) => {
      const dot = document.createElement("div");
      dot.classList.add("dot");
      if (index === 0) dot.classList.add("active");
      dot.addEventListener("click", () => {
        console.log("Dot clicked, navigating to slide", index);
        this.goToSlide(index);
      });
      dotsContainer.appendChild(dot);
    });
    this.dots = dotsContainer.querySelectorAll(".dot");
  }

  /* --------------------------------------------------------------------------
     Initialize Navigation Buttons
     - Attaches event listeners to the previous and next buttons.
  -------------------------------------------------------------------------- */
  initNavButtons() {
    const prevButton = document.querySelector(".prev-btn");
    const nextButton = document.querySelector(".next-btn");

    if (prevButton) {
      prevButton.addEventListener("click", () => {
        console.log("Previous button clicked");
        this.prevSlide();
      });
    } else {
      console.error("Previous button (.prev-btn) not found!");
    }

    if (nextButton) {
      nextButton.addEventListener("click", () => {
        console.log("Next button clicked");
        this.nextSlide();
      });
    } else {
      console.error("Next button (.next-btn) not found!");
    }
  }

  /* --------------------------------------------------------------------------
     Navigate to a Specific Slide
     - Removes "active" class from current slide and dot.
     - Updates the currentIndex.
     - Adds "active" class to the new slide and corresponding dot.
     @param {number} index - The index of the slide to display.
  -------------------------------------------------------------------------- */
  goToSlide(index) {
    this.images[this.currentIndex].classList.remove("active");
    if (this.dots && this.dots[this.currentIndex]) {
      this.dots[this.currentIndex].classList.remove("active");
    }
    this.currentIndex = index;
    this.images[this.currentIndex].classList.add("active");
    if (this.dots && this.dots[this.currentIndex]) {
      this.dots[this.currentIndex].classList.add("active");
    }
    console.log("Navigated to slide", this.currentIndex);
  }

  /* --------------------------------------------------------------------------
     Navigate to the Next Slide
     - Advances to the next slide, wrapping to the first if at the end.
  -------------------------------------------------------------------------- */
  nextSlide() {
    const nextIndex = (this.currentIndex + 1) % this.images.length;
    this.goToSlide(nextIndex);
  }

  /* --------------------------------------------------------------------------
     Navigate to the Previous Slide
     - Moves to the previous slide, wrapping to the last if at the beginning.
  -------------------------------------------------------------------------- */
  prevSlide() {
    const prevIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
    this.goToSlide(prevIndex);
  }

  /* --------------------------------------------------------------------------
     Start Autoplay
     - Automatically advances the gallery every 5000 milliseconds.
  -------------------------------------------------------------------------- */
  startAutoPlay() {
    setInterval(() => this.nextSlide(), 5000);
    console.log("Autoplay started, advancing slides every 5000ms");
  }
}

/* ==========================================================================
   INITIALIZE GALLERY ON DOM CONTENT LOADED
   ========================================================================== */
document.addEventListener("DOMContentLoaded", () => {
  const galleryWrapper = document.querySelector(".gallery-wrapper");
  if (galleryWrapper) {
    new Gallery();
  } else {
    console.error("Gallery wrapper (.gallery-wrapper) not found!");
  }
});
