$(document).ready(function() {
    // Function to handle item updates
    function updateItems() {
        var itemsData = {};
        // Extract item data from the page
        $('.item').each(function(index) {
            var itemId = $(this).find('.item-price').attr('id').replace('item-price', '');
            var itemName = $(this).find('.item-title').text();
            var itemQuantity = parseInt($(this).find('.item-price').text().replace('Price: ', ''));
            itemsData[itemId + '-' + itemName] = itemQuantity;
        });

        // Make an AJAX POST request to update the items
        $.ajax({
            type: 'POST',
            url: '/update-items',
            data: itemsData,
            success: function(response) {
                console.log('Items updated successfully.');
            },
            error: function(xhr, status, error) {
                console.error('Error updating items:', error);
            }
        });
    }

    // Handle button click to update items
    $('#updateItemsBtn').click(function() {
        updateItems();
    });
});
