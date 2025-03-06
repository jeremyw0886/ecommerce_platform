"use strict";

// store/static/js/payment.js

document.addEventListener("DOMContentLoaded", function () {
  // Ensure that paymentData has been set in the template
  if (typeof window.paymentData !== "undefined") {
    var stripe = Stripe(window.paymentData.stripePublicKey);
    var elements = stripe.elements();
    var cardElement = elements.create("card");
    cardElement.mount("#card-element");

    var form = document.getElementById("payment-form");
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var submitBtn = document.getElementById("submit");
      submitBtn.disabled = true;
      submitBtn.textContent = "Processing...";
      stripe
        .confirmCardPayment(window.paymentData.clientSecret, {
          payment_method: { card: cardElement }
        })
        .then(function (result) {
          if (result.error) {
            document.getElementById("payment-message").innerText =
              result.error.message;
            submitBtn.disabled = false;
            submitBtn.textContent = "Pay";
          } else if (result.paymentIntent.status === "succeeded") {
            // Payment succeeded: redirect to process the order
            window.location.href = "/process-order/";
          }
        });
    });
  }
});
