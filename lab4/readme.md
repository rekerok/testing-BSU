# Test cases

Preconditions:
* link - https://www.vans.com/en-us
* internet connection

## Test case 1
Name: **Checking the price range.**

Steps: 
1. Go to the https://www.vans.com/en-us/mens/featured/new-arrivals-c1000?icn=subnav
2. Click on the "+" icon near "Price" option.
3. Select "$0-$25" in the price filter.
4. Check if the prices of the items satisfy the condition of fiter.  

*Expected result:* On the page only items with price between $0 and $25 are shown.

---

## Test case 2
Name: **Adding item to the cart.**

Steps:
1. Go to the item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container .
2. Select the first available size.
3. Press "Add to cart".
4. Go to the cart https://www.vans.com/en-us/cart . 

*Expected result:* Chosen item is in the cart ("VANS TOASTED T-SHIRT", the size is the one you've chosen, quantity: 1, price: $24.50, total: $24.50).

---

## Test case 3
Name: Checking size guide.

Steps:
1. Go to the item: https://www.vans.com/en-us/shoes-c00081/old-skool-pvn0a4bw2rv2 .
2. Press "Size guide".
3. Select "29cm" option.
4. Press "Continue".  

*Expected result:* The message "WOMENS SIZE 12.5 / MENS SIZE 11" is shown in the dialog box.


---

## Test case 4
Name: Checking ability of writing review  

Steps:
1. Go to the item: https://www.vans.com/en-us/shoes-c00081/skate-sk8-hi-pvn0a5fccnav .
2. Press "Write a review" in the section "REVIEW SNAPSHOT".
  
*Expected result:* The page of review creating is shown.


---

## Test case 5
Name: **Deleting item from the cart.**  
Precondition: item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container is in the cart.

Steps:
1. Go to the cart: https://www.vans.com/en-us/cart .
2. Press "Remove".
  
*Expected result:* The message "THERE ARE NO ITEMS IN YOUR CART" appeared on the page of the cart.

---

## Test case 6
Name: **Adding item to the favourites.**

Steps:
1. Go to the item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container .
2. Click on the heart icon.
3. Go to the favourites: https://www.vans.com/en-us/favorites-public .
  
*Expected result:* Chosen item is in favourites ("Vans Toasted T-Shirt", price: $24.50).

---

## Test case 7
Name: **Paying with PayPal.**  
Precondition: item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container is in the cart.

Steps:
1. Go to the cart: https://www.vans.com/en-us/cart .
2. Press button "PayPal".
  
*Expected result:* The page "Log in to your PayPal account" is shown.

---

## Test case 8
Name: **Sharing my cart.**  
Precondition: item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container is in the cart.

Steps:
1. Go to the cart: https://www.vans.com/en-us/cart .
2. Press button "Share my cart".
  
*Expected result:* The dialog box is shown (with message "SHARE YOUR CART WITH OTHERS", link, buttons "Copy to clipboard" and "Close button").

---

## Test case 9
Name: **Changing quantity of item.**  
Precondition: item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container is in the cart (quantity: 1).

Steps:
1. Go to the cart: https://www.vans.com/en-us/cart .
2. Click on the down arrow near "Quantity" option.
3. Select option "2". 
  
*Expected result:* The item is in the cart ("VANS TOASTED T-SHIRT", the size is the same as in the precondition, quantity: 2, price: $24.50, total: $49.00).

---

## Test case 10
Name: **Changing size of item.**  
Precondition: item https://www.vans.com/en-us/clothing-c00082/vans-toasted-t-shirt-pvn0009sbwht#pr-container is in the cart (quantity: 1, size: Large).

Steps:
1. Go to the cart: https://www.vans.com/en-us/cart .
2. Press "Edit" near size info.
3. Select size "X Large". 
4. Press "Update".
  
*Expected result:* The item is in the cart ("VANS TOASTED T-SHIRT", size: X Large, quantity: 1, price: $24.50, total: $49.00).




