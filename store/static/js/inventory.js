document.addEventListener("DOMContentLoaded", function () {
  // Check for an element that indicates inventory updates should be active.
  // For example, this could be a hidden element added to pages that use inventory.
  const inventoryIndicator = document.querySelector("#inventory-indicator");
  if (!inventoryIndicator) {
    return;
  }

  let ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
  let inventorySocket = new WebSocket(ws_scheme + "://" + window.location.host + "/ws/inventory/");

  inventorySocket.onopen = function () {
    console.log("Inventory WebSocket connection established.");
  };

  inventorySocket.onmessage = function (e) {
    const data = JSON.parse(e.data);
    console.log("Inventory update received:", data.message);
  };

  inventorySocket.onclose = function () {
    console.log("Inventory WebSocket connection closed.");
  };

  // Optionally, send a subscription message to the server:
  // inventorySocket.send(JSON.stringify({action: 'subscribe_inventory_updates'}));
});
