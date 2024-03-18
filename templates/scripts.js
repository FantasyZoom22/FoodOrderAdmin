  $(document).ready(function() {
    // Sample existing items (you can replace it with dynamic data from your server)
    const existingItems = [
      { id: 1, name: "Tako", price: 150, image: "https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470283/TG-Foods/Tako_148_qb6ayw.png" },
      { id: 2, name: "Hotdog", price: 120, image: "https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470281/TG-Foods/Hotdog_148_iddyls.png" },
      { id: 3, name: "Burger", price: 200, image: "https://res.cloudinary.com/dsjjtnudl/image/upload/v1692470282/TG-Foods/Burger_148_vm6adu.png" },
      // Add more items as needed
    ];

    // Function to display existing items
    function displayItems() {
      $("#itemList").empty();
      existingItems.forEach(item => {
        $("#itemList").append(`
          <div class="item-panel">
            <div class="row">
              <div class="col-md-4">
                <img src="${item.image}" alt="${item.name}">
              </div>
              <div class="col-md-4">
                <h3>${item.name}</h3>
                <p>Price: دج ${item.price}</p>
              </div>
              <div class="col-md-4">
                <div class="form-group">
                  <label for="itemPrice_${item.id}">New Price:</label>
                  <input type="number" class="form-control" id="itemPrice_${item.id}" value="${item.price}">
                </div>
                <button class="btn btn-info btn-block mt-3" onclick="updatePrice(${item.id})">Update Price</button>
                <button class="btn btn-danger btn-block mt-3" onclick="confirmDelete(${item.id})">Delete</button>
              </div>
            </div>
          </div>
        `);
      });
    }

    displayItems();

    // Function to handle form submission for adding a new item
    $("#addItemForm").submit(function(event) {
      event.preventDefault();
      const itemName = $("#itemName").val();
      const itemPrice = $("#itemPrice").val();
      const itemImage = $("#itemImage").val();
      // Add validation if needed

      // Add the new item to the existing items list
      const newItem = {
        id: existingItems.length + 1, // Generate a unique ID (you may handle this differently)
        name: itemName,
        price: parseFloat(itemPrice),
        image: itemImage
      };
      existingItems.push(newItem);
      displayItems();
      // Clear the form fields
      $("#itemName").val("");
      $("#itemPrice").val("");
      $("#itemImage").val("");
    });

    // Function to confirm deletion of an item
    window.confirmDelete = function(itemId) {
      $("#deleteItemModal").modal("show");
      $("#confirmDeleteBtn").off("click").click(function() {
        deleteItem(itemId);
        $("#deleteItemModal").modal("hide");
      });
    };

    // Function to delete an item
    function deleteItem(itemId) {
      const index = existingItems.findIndex(item => item.id === itemId);
      if (index !== -1) {
        existingItems.splice(index, 1);
        displayItems();
      }
    }

    // Function to update the price of an item
    window.updatePrice = function(itemId) {
      const newPrice = $(`#itemPrice_${itemId}`).val();
      const index = existingItems.findIndex(item => item.id === itemId);
      if (index !== -1) {
        existingItems[index].price = parseFloat(newPrice);
        displayItems();
      }
    };

    // Function to handle update items button click
    $("#updateItemsBtn").click(function() {
      // Submit the form to update items
      $("#addItemForm").submit();
    });
  });
