'use strict';
/**
 * Initializes event listeners for tooltips and modal functionality
 *  once the DOM content is fully loaded.
 */
document.addEventListener('DOMContentLoaded', () => {
  const features = document.querySelectorAll('.feature-list li');
  
  /**
   * Adds event listeners to each feature list item for showing and hiding tooltips.
   */
  features.forEach(feature => {
    feature.addEventListener('mouseenter', (e) => {
      const tooltip = e.target.querySelector('.feature-tooltip');
      if (tooltip) {
        tooltip.style.opacity = '1';
        tooltip.style.transform = 'translateY(0)';
      }
    });
    feature.addEventListener('mouseleave', (e) => {
      const tooltip = e.target.querySelector('.feature-tooltip');
      if (tooltip) {
        tooltip.style.opacity = '0';
        tooltip.style.transform = 'translateY(10px)';
      }
    });
  });

  const modal = document.getElementById('caseStudyModal');
  const btn = document.querySelector('.case-study-btn');
  const closeBtn = document.querySelector('.close-modal');

  /**
   * Adds event listeners for opening and closing the case study modal.
   */
  if (btn && modal && closeBtn) {
    btn.addEventListener('click', () => {
      modal.style.display = 'block';
      loadCaseStudy();
    });
    closeBtn.addEventListener('click', () => {
      modal.style.display = 'none';
    });
    window.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.style.display = 'none';
      }
    });
  }

  /**
   * Loads the case study content into the modal if it hasn't been loaded already.
   */
  function loadCaseStudy() {
    const modalContent = modal.querySelector('.modal-content');
    if (!modalContent.querySelector('.case-study-content')) {
      const content = `
        <div class="case-study-content">
          <section class="challenge">
            <h3>The Challenge</h3>
            <p>Details about the project challenges...</p>
          </section>
          <section class="solution">
            <h3>The Solution</h3>
            <p>How we solved the challenges...</p>
          </section>
          <section class="results">
            <h3>The Results</h3>
            <p>Measurable outcomes and improvements...</p>
          </section>
        </div>
      `;
      modalContent.insertAdjacentHTML('beforeend', content);
    }
  }
});
