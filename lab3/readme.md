# Test cases

Preconditions:
* link - https://www.vans.com/en-us
* internet connection

## Test case 1
Name: Checking the price range.

Steps: 
1. Choose "Mens" in the upper-menu.
2. Choose "New Arrivals" in the list.
3. Select "$0-$25" in the price filter
4. Check if the prices of the items satisfy the condition of fiter.
Expected result: on the page only items with price between $0 and $25 are shown.

## Test case 2
Name: Adding item to the cart.

Steps: 
1. Choose "Mens" in the upper-menu.
2. Choose "New Arrivals" in the list.
3. Select the first item.
4. Select the first available size.
5. Press "Add to cart".
6. Press "Checkout" at the pop-up menu.
Expected result: the chosen item is in the cart.

## Test case 3
Name: Checking geolocation.

Steps:
1. Scroll page till the end.
2. Press button "Find a store"
3. Check if the shown location is nearest to you.
Expected result: The shown location is coreect (the nearest).

## Test case 4
Name: Checking valid email address.

Steps:
1. Scroll page till the end.
2. Enter "abcdef" in the text field "Email Address" in the block "Subscribe".
3. Press "Send".
Expected result: The message "A valid email address is required".