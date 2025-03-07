'use strict';

document.addEventListener('DOMContentLoaded', function() {
  const sameAsMailing = document.getElementById('sameAsMailing');
  const billingStreet = document.getElementById('billingStreet');
  const billingState = document.getElementById('billingState');
  const billingZip = document.getElementById('billingZip');

  // Get mailing address values from hidden fields
  const mailingStreet = document.getElementById('mailingStreet').value;
  const mailingState = document.getElementById('mailingState').value;
  const mailingZip = document.getElementById('mailingZip').value;

  if (sameAsMailing) {
    sameAsMailing.addEventListener('change', function() {
      if (this.checked) {
        billingStreet.value = mailingStreet;
        billingState.value = mailingState;
        billingZip.value = mailingZip;
      } else {
        billingStreet.value = '';
        billingState.value = '';
        billingZip.value = '';
      }
    });
  }
});
