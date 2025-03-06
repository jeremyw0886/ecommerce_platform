"use strict";

// store/static/js/checkout.js

document.addEventListener("DOMContentLoaded", function () {
  const checkoutBtn = document.getElementById("checkout-btn");
  if (checkoutBtn) {
    checkoutBtn.addEventListener("click", function (e) {
      checkoutBtn.disabled = true;
      checkoutBtn.textContent = "Processing...";

      const spinner = document.createElement("span");
      spinner.className = "spinner-border spinner-border-sm ms-2";
      spinner.setAttribute("role", "status");
      spinner.setAttribute("aria-hidden", "true");
      checkoutBtn.appendChild(spinner);
    });
  }
});
