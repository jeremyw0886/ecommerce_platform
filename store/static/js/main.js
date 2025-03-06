"use strict";

/**
 * Initializes event listeners and intersection observer for project card animations
 * once the DOM content is fully loaded.
 */
document.addEventListener("DOMContentLoaded", function () {
  const projectCard = document.querySelector(".project-card");
  const thumbnail = document.querySelector(".thumbnail");
  const projectOverlay = document.querySelector(".project-overlay");

  /**
   * Intersection Observer to animate project card when it comes into view.
   */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  });
  if (projectCard) {
    observer.observe(projectCard);
  }

  /**
   * Adds event listeners to project card for hover effects on thumbnail and overlay.
   */
  if (projectCard && thumbnail && projectOverlay) {
    projectCard.addEventListener("mouseenter", () => {
      thumbnail.style.transform = "scale(1.05)";
      projectOverlay.style.opacity = "1";
    });
    projectCard.addEventListener("mouseleave", () => {
      thumbnail.style.transform = "scale(1)";
      projectOverlay.style.opacity = "0";
    });
  }

  /**
   * Adds a load event listener to the thumbnail for fade-in animation.
   */
  if (thumbnail) {
    thumbnail.addEventListener("load", function () {
      this.style.animation = "fadeIn 0.5s ease-in";
    });
  }
});
