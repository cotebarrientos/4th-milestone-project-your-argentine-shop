![logotype](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/logo_project_transparent_500px.png?raw=true)
# Your Argentine Shop - Testing Details
#### <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/README.md" target="_blank">Main README.md file</a>
#### <a href="https://your-argentine-shop.herokuapp.com/" target="_blank">View Website</a>
---

A thorough manual testing has been carried out in the construction of this project. In addition to the tests performed, I also validated all the files online and checked the compatibility of this one on various browsers and mobile devices. 

---
## Testing Contents
1. [**Validation Services**](#validation-services)
    * [HTML 5](#html-5)
    * [CSS 3](#css-3)
    * [Javascript](#javascript)
    * [Python](#python)
2. [**Browser Compatibility**](#browser-compatibility)
3. [**Responsiveness**](#responsiveness)
4. [**Manual Testing**](#manual-testing)
    * [Links Functionality](#links-functionality)
    * [User Stories Functionality](#user-stories-functionality)
    * [Defensive Design](#defensive-design)
    * [Issues during project development](#issues-during-project-development)
    * [Tested devices](#tested-devices)
---
## Validation Services

### HTML 5

I used <a href="https://validator.w3.org/" target="_blank">W3C HTML Validator</a> to validate my HTML files by direct input.
 - All the **.html** files were checked.
 - **profile.html** has an **error** attributed to the crispy forms, due to duplicate IDs. This happens because the **attribute lazyload**.
 
 ![error 1](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/html_error2.jpg?raw=true)

 - **cart.html** has an **error** attributed to the input quantity field, due to duplicate IDs. This error is to be expected 
 because the project uses jinja template.

 - **checkout.html** has a **warning** attributed to an empty heading. This warning is to be expected 
 because the project uses jinja template.

![warning 1](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/html_warnings1.jpg?raw=true)

 - the following html files present an **error** about duplicate IDs. This error is to be expected due to the crispy form 
 and custom widget templates files.

![error 2](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/html_error1.jpg?raw=true)

 - All the .html files present a **warning** related to the *type attribute is unnecessary for JavaScript resources*.

![warning 2](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/html_warnings2.jpg?raw=true)

### CSS 3

I used <a href="https://jigsaw.w3.org/css-validator/validator.html.en" target="_blank">W3C CSS Validator</a> to validate my CSS files by direct input.
- All the **.css** files were checked.
- All the **.css** passed without an **error**.
- **checkout.css**  has a **warning**.

 ![css warning 1](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/css_warnings.jpg?raw=true)

- **base.css** has 14 **warnings**.

 ![css warning 2](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/css_warnings2.jpg?raw=true)

### Javascript

I used <a href="https://jshint.com/" target="_blank">JShint</a> to validate my JS files by direct input.
- All the **.js** files were checked.
- **stripe_elements.js** has the following:
    - **Metrics:** 
        - There are 5 functions in this file. 
        - Function with the largest signature take 1 arguments, while the median is 1.
        - Largest function has 10 statements in it, while the median is 5. 
        - The most complex function has a cyclomatic complexity value of 3 while the median is 1.
    - **Two Warnings:**
        - 'template literal syntax' is only available in ES6 (use 'esversion: 6').
    - **Two undefined variables:**
        - $ (JQuery)
        - Stripe (Stripe API)

- **quantity_input_script.html** has the following:
    - **Metrics:**
        -  There are 4 functions in this file.
        - Function with the largest signature take 1 arguments, while the median is 1.
        - Largest function has 6 statements in it, while the median is 5.5.
        - The most complex function has a cyclomatic complexity value of 1 while the median is 1.
    - **Three Warnings:**
        - 'template literal syntax' is only available in ES6 (use 'esversion: 6').
    - **One undefined variables:**
        - $ (JQuery)

- **countryfield.js** has the following:
    - **Metrics:**
        - There is only one function in this file.
        - It takes no arguments.
        - This function contains 4 statements.
        - Cyclomatic complexity number for this function is 2.
    - **One Warning:**
        - 'let' is available in ES6 (use 'esversion: 6') or Mozilla JS extensions (use moz).
    - **One undefined variables:**
        - $ (JQuery)

### Python

I used <a href="http://pep8online.com/" target="_blank">PEP8 Online</a> to validate my python files by direct input.
- All the **.py** files were checked.
- **blog/widgets.py** has 1 exception:
    - Line 9: line too long (83 > 79 characters)
    - This line contains the path to a template, so I decided not to modify it.
- **checkout/webhook_handler.py** has 2 exception:
    - Line 74: line too long (80 > 79 characters)
    - Line 75: line too long (80 > 79 characters)
    - I decided not modify those lines, since when I tried to do it, the code was broken.
- **checkout/webhooks.py** has 1 exception:
    - Line 42: 	line too long (86 > 79 characters)
    - I decided to leave this line unchanged, in order not to break the code.
- **ms4/settings.py** has 4 exception:
    - Line 148: line too long (91 > 79 characters)
    - Line 151: line too long (81 > 79 characters)
    - Line 154: line too long (82 > 79 characters)
    - Line 157: line too long (83 > 79 characters)
    - I didn't change these lines of code, because these are part of `AUTH_PASSWORD_VALIDATORS` so as to avoid forcing a break in the code.
- **products/widgets.py** has 1 exception:
    - Line 9: line too long (87 > 79 characters)
    - As with the widgets.py file above, this line contains the path to a template, so I decided not to change it.
- **profiles/widgets.py** has 1 exception:
    - Line 9: line too long (87 > 79 characters)
    - This line contains the path to a template, so I decided not to change it.
- I haven't modified any files inside the **migrations folders**, in order to not break the code or cause problems to the database. 
In general the **.py** files follow all the rules, only with some exceptions where some lines are too long.
- The rest of the **.py** files are fully compliant with the **PEP8** requirements. 

##### [Back to top](#testing-contents)
---
## Browser Compatibility

In order to ensure that the website would work properly in the following browsers, responsiveness tests, button and link checks were done, as well 
as tests on the look of the website to ensure that the colors, images and fonts used would display correctly.

| Browser       | Responsiveness | Appearance    | Performance   |
| :-----------: | :-----------:  | :-----------: | :-----------: |
| Chrome        | Good | Good | Good |
| Firefox       | Good | Good | Good |
| Avast Secure  | Good | Good | Good |
| Edge          | Good | Good | Good |  
| Safari        | Fair | Fair | Fair |
| IE            | Poor | Poor | Poor |

* **Chrome:** The website works very well, and it was the main browser I used during the development of this project. 
The website elements adapt perfectly to the different screen sizes, the fonts and images look pretty good, and all 
the functionalities of the online store are working properly.

* **Mozilla Firefox:** This browser behaves very well in general. This was the secondary browser I used during the 
development of this online store, and it served as a point of comparison with the Chrome browser. Some of the most 
noticeable differences with Chrome is that the fonts used look slightly larger and thicker, changing the appearance 
of the website, this difference forced me to further adapt the css classes used.

* **Avast Secure:** Of all the browsers used, this is the one that gave the best appearance to the website. The 
images look very high quality, and the fonts used look perfect. In general all the functions of the website work 
correctly, the only drawback is that it loads the website content much slower than *Chrome* and *Mozilla Firefox*.

* **Edge:** The website in this browser looks pretty good, and in addition to all the browsers used, in this one 
the online store contents loaded faster, especially the images that are one of the most demanding elements in the 
browser performance. On the other hand, Stripe elements take a little longer to load compared to *Chrome* and *Mozilla 
Firefox*. The web page works correctly in this browser.

* **Safari:** The website works, but it has a fair performance, and it doesn't stand out from the rest. First of all, 
this browser takes longer than usual to load the website, it doesn't take some css classes well either, and the images 
and fonts used don't look as good compared to browsers like *Chrome* or *Mozilla Firefox*.

* **Internet Explorer (IE):** The website is **completely broken** in this browser. Stripe doesn't work, it doesn't allow 
to update the items in the shopping cart, and it doesn't allow to delete items in it either. In the website's physical 
appearance, the elements within it are completely disassembled, and the appearance of both images and fonts used, look 
terrible, the performance of this browser is pretty poor and *it's not recommended to use it* because of everything 
described above.

**Chrome's DevTools Lighthouse Report**

**1.** *Desktop*

| Performance   | Accessibility | Best Practices| SEO  |
| :-----------: | :-----------: | :-----------: | :-----------: |
| 77% | 88% | 93% | 90% |

 ![Lighthouse Report for Desktop](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/lighthouse_desktop.jpg?raw=true)

**2.** *Mobile*

| Performance   | Accessibility | Best Practices| SEO  |
| :-----------: | :-----------: | :-----------: | :-----------: |
| 66% | 88% | 93% | 92% |

![Lighthouse Report for mobile](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/lighthouse_mobile.jpg?raw=true)

**Note:** Website performance drops during testing with Chrome's DevTools Lighthouse because it takes a while for the online store 
images to load. Another factor that influenced during the tests was the speed of my home internet provider (especially with GoMo 
the performance of the website was very slow). These tests were performed with Three's internet provider.

##### [Back to top](#testing-contents)
---
## Responsiveness

I made the following responsiveness tests in order to ensure that the website operates correctly and at the same time that its components 
are seen harmoniously arranged in different screen sizes, so that I used the following tools to help me.

* **Mozilla Firefox DevTools**: This browser was used to check the behavior of the web page in different screen sizes using the Developer Tools. 
Tests consisted in testing the appearance of the fonts used, the aspect of colors and backgrounds, the order and space used by the different 
elements that make up the web page.

* **Google Chrome DevTools**: This browser was used to check the behavior of the web page in different screen sizes using the Developer Tools. 
As in the previous browser, different tests were performed checking the aspect of the font used, colors and backgrounds, and finally, the space 
used by the elements of the website. In addition, a contrast was made between both browsers, checking for any existing differences.

* **Xiaomi Mi A1**: This mobile device was used to test the behavior of the website, using browsers such as *Chrome, Mozilla Firefox* and *DuckDuckGo*.

* **Xiaomi Poco x3**: This mobile device was used to test the behavior of the website, using browsers such as Chrome, Mozilla Firefox and DuckDuckGo.

* **Iphone S20**: This mobile device was used to test the behavior of the website, using browsers such as *Chrome* and *Safari*.

* **Ipad Mini 2**: This device was used to test the behavior of the website, using browsers such as *Chrome* and *Safari*.


| Device            | Responsiveness | Type           |
| :---------------: | :------------: | :------------: |  
| Desktop >1200px   | Good | Virtual |
| Desktop 1024px    | Good | Virtual |
| Ipad PRO          | Good | Virtual |
| Ipad              | Good | Virtual |
| Ipad Mini         | Good | Virtual |
| Iphone 6/7/8 plus | Good | Virtual |
| Iphone 6/7/8      | Good | Virtual |
| Iphone 5          | Good | Virtual |
| Xiaomi Mi A1      | Good | Physical Device |
| Xiaomi Poco x3 NFC   | Good | Physical Device |
| Iphone S20        | Good | Physical Device |
| Ipad Mini 2       | Good | Physical Device |


##### [Back to top](#testing-contents)
---
## Manual Testing

### Links Functionality

The following tests were performed to verify that all links responded as expected:

* Menu bar items were clicked on from each page to make sure that they navigate to the correct page.
* Clicking on the logo in the menu bar leads the user back to the home page.
* The search bar, user profile and shopping cart icons work correctly on different screen sizes.
* All links within the website lead you to the assigned page.
* All buttons (e.g. buttons to return to home page) have been clicked to check that these
 buttons return the user to the correct page.
* The back to top button on all pages works correctly.

**Test Outcome**: PASSED

### User Stories Functionality

The tests performed in this section were mainly focused on checking that all the expected functions 
within the user stories worked correctly.

#### Home Page

1. The home page displays images with different buttons that invite the user to buy a product related 
to the image itself. The user when clicking on the **"shop now"** button should be redirected to the selected 
product category.
    * **First slide image**: The button inside this image redirects the user to a page showing *all the 
    website's products*.
    * **Second slide image**: The button inside this image redirects the user to a page which displays 
    products with the *"Yerba Mate"* category.
    * **Third slide image**: The button inside this image redirects the user to a page which displays 
    products with the *"Empanadas"* category.
    * **Fourth slide image**: The button inside this image redirects the user to a page which displays 
    products with the *"Alfajores"* category.
    * **Fifth slide image**: The button inside this image redirects the user to a page which displays 
    products with the *"Dulce de leche"* category.

2. The Home page, every time that it is reloaded, should show random products, which when pressed, redirect 
the user to the selected product, and these are:
    * **Featured products:** It shows a total of 8 random products, except for the "combos" category.
    * **Combos:** It displays a total of 4 products that only belong to this category.

**Test Outcome**: PASSED

#### Products page view

To access the products page, the user can do it from the navigation bar by selecting the **"shop"** nav link 
(which has products sorted by categories) or select the **"All products"** nav link, which shows all products 
according to the selected order (by price, by category and all products). Explained this, the following 
tests were made to the products page.

1. Select the different sorting options from the top dropdown box one by one, confirm that the products are 
sorted with the selected option.
2. Select the different sorting options in the **"Shop"** navigation menu one by one, and confirm that the products 
are sorted in the selected category. For example, clicking on *"Alfajores"* selects all products related to this 
category. Check that each category is displayed and that these indeed show the related products.
3. Select the different sorting options in the **"All Products"** navigation menu one by one, and confirm that the products 
are sorted in the selected option. For example, clicking on *"By Price"* will display all products in the online store 
sorted by price. As a bonus, you can select in the dropdown box to sort the products by low to high price or by high 
to low price.
4. Select a product of your interest from the product page. The expected result should be effectively a detailed view 
of the selected product.

**Test Outcome**: PASSED

#### Search for products by keyword in the search bar.

1. Type a word related to the website's products (e.g. "milk"), the search bar should be able to display all products related 
to your query.
2. Type any word in the search bar and which doesn't relate to any product on the website (e.g. "vegetarian snack"), 
the expected behavior is that a special message is shown indicating that there are no results for your search.

**Test Outcome**: PASSED

#### product detail view 

1. Select a product by clicking on the image from the product page.
2. Once inside the page that allows you to see the product in detail, select the desired product quantity (for example 2) 
from the input quantity field and verify that this quantity appears in the shopping cart icon.
3. Then go to the product page, select another item and add the desired quantity (e.g. 1). Then check that this product with 
the selected quantity appears in the shopping cart icon.
4. Once this is done, press the button that says "Go to checkout" (which is inside the message that is displayed once you have 
pressed the "Add to Cart" button), to access the shopping cart. The expected result is that the user can in fact access the 
shopping cart.

**Test Outcome**: PASSED

#### Shopping cart functionality

1. Check inside the shopping cart to make sure that all the selected products are in the shopping cart.
2. Increase the quantity of any product that is in the shopping cart from the input quantity field, then click on the *"update"* 
link whose function is to update the selected item's quantity. The expected result is that the selected product's quantity will 
be effectively updated.
3. Decrease the quantity of any product in the shopping cart from the input quantity field, then click on the *"update"* link. 
The expected result is that effectively the selected product quantity  will be updated.
4. To calculate the delivery price, 10% of the total quantity is calculated, but after 60 euros, the delivery is free. For products 
in the shopping cart, be sure to make more than 60 euros to check that the promotion is fulfilled.
5. Delete all the products in the shopping cart by clicking on the link that says *"remove"*, then check that the items in the 
shopping cart have been removed. The expected result is that the items in the shopping cart are removed and at the same time a 
special message appears when the shopping cart is empty.
6. Again add more products into the shopping cart and adjust it to your needs, then press the button that says *"Proceed to Checkout"* 
and verify that you can indeed access the checkout page. The expected result is that the user can indeed access the checkout page 
and start finalizing his/her order.

**Test Outcome**: PASSED

#### Checkout page functionality

In order to perform the tests corresponding to this functionality, you must take in consideration the following:

- The payment method used by the online store is **Stripe API**, but in its **TEST** version (only for development). 
- To make the payments, you must enter the following card number: **4242 4242 4242 4242 424 242 42424**
- Filling out this information should look something like this:

![Card number example](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/card_example.jpg?raw=true)

The following tests have been performed:

1. Verify that the form is displayed.
2. Check that all items added to the shopping cart appear on this page.
3. Try to checkout without filling out some of the required fields. The expected result is that the user will not 
be allowed to proceed with the purchase and messages will appear prompting the user to fill out these form fields.
4. Fills the email field with an invalid one (e.g. anything without the @). The expected result is that it won't 
allow the user to complete the purchase and a message will appear telling the user to fill in that field correctly.
5. Fill out the form with all the required information.
6. Try to make the purchase with an invalid card, for example: **2424 2424 2424 2424**. The expected result would be 
a message below the Stripe field saying *"Your card number is invalid"*.
7. Make the purchase with the test card data at the top of this section, also check that a message appears in red 
letters that says *"Your card will be charged €(order total)"* making sure that the total shown is correct, and 
then finish by pressing the button that says *"Complete Order"*. The expected outcome is that the user is redirected 
to the checkout success page, which shows a purchase summary, also the shopping cart should be reset (no items in it) 
and most importantly the user **should receive a confirmation email**.

Order confirmation example:

![Order confirmation example](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/order_confirmation_email_example.jpg?raw=true)

**Test Outcome**: PASSED

#### Create an account

1. Go to the user icon, click on it and choose the option that says *"Register"*.
2. Check that the registration form is displayed.
3. Fill in the form with a username already existing in the database (for example **Manu1992**), confirm that the user 
is informed that the username already exists. The expected result is the user cannot register.
4. Fill in the form with an email already existing in the database by typing the following: **pesaro8770@relumyx.com**, then confirm 
that the user is informed of someone already registered with that email. The expected result results with the user be unable to register.
5. Fill in the email entry with an address which is invalid in this form field (which doesn't have the @), then confirm the user is informed 
of an error message saying he/she has typed an invalid email address. The expected result is that the user won't be able to register.
6. Complete the form with 2 different passwords, and check that the user is informed of the error. The result of this is that the 
user cannot register.
7. Try to type a password that is as follows: **12345678**. By doing this the user will be informed that his/her password is too weak and that he/she 
should type another one. The expected result is that the user will fail to register.
8. Complete the registration form with all the required data correctly. When doing this the expected result is that the user must confirm his/her 
email, for that he/she will receive a confirmation email in which he/she will find a link that will redirect him/her to confirm it. After that, 
the user must click on the button that says *"confirm"*, he/she will get to the sign in page.
Here is an example of an email received by the user when registering to the website.

![Email confirmation example](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/email_confirmation_link.jpg?raw=true)

**Test Outcome**: PASSED

#### Log in

1. Go to the user icon, click on it and choose the option that says *"Login"*.
2. Check that the sign in form is displayed.
3. Attempt to log in with an incorrect username or email address. The expected result is that a special message appears warning that 
the username, email or password is incorrect.
4. Try to log in with the newly created account and type an incorrect password. The expected result is a message warning the user that 
he/she could not log in.
5. Type the username or email of the newly created account, and also type the correct password. The expected result is that the user will be 
able to log in and will be redirected to the home page, and a message will appear warning that the user has been able to log in.

**Test Outcome**: PASSED

#### User profile functionality

The user profile has the following elements:
- A cover image with a card containing a welcome message to the user and a profile avatar image.
- A Bio section to write anything relevant to the user.
- A form with the user's data about the deliveries.
- A section with the orders placed historically.

Having explained this, the tests performed are as follows:

**Reviewing the user's profile**

1. Click on the user icon and select the option *"My profile"*.
2. Once inside the user profile, check that all the elements described above are present on the page.
3. Click on the *"Edit my profile"* button and only edit the following fields:
    - Select an image for your profile
    - Write a little bit about yourself in the bio field.
4. Then click on the button that says *"Update information"*.
5. Check that the image appears next to what you wrote in the bio section.
6. Then go back to the website and start shopping like any other user (important note, do not fill in 
the other data to test the autocompletion using the user registration data in the checkout form).

**Test Outcome**: PASSED

**Make a purchase without filling the data before in the user profile.**

1. Add all the desired items into the shopping cart, then go to checkout. Check that the form pre-fills the 
fields for the user's full name and email address used at the time of registration. The expected result is that 
those fields are indeed filled in.
2. Then start filling in the other data inside the checkout form and make sure that the checkbox that allows you 
to save the desired data is selected. When you have selected that checkbox the expected result is that after the 
purchase, those data will be saved in the user's profile.
3. Complete the card data with the test card and finalize the purchase. Once this is done the expected result is 
that the user is lead to the success checkout page and the order is saved in the user profile.
4. Go to the user profile and check that the order is indeed placed and that the data entered has been saved. 
The expected result is indeed displayed and the user can access it to check what was purchased and also the purchase 
data has been saved.

**Test Outcome**: PASSED

**Some more tests within the user profile**

1. Press the *"Edit my profile"* button and start editing the user profile again, for example remove the profile 
picture or simply upload another one of your choice. Also edit the bio and some fields inside the form with the 
delivery details, and finish by pressing the *"Update Information"* button. The expected result is that all the 
changes made within the user's profile will appear.

2. Click on the order number to access the purchase made. The expected result is that the user can effectively 
check the content of the order made.

**Test Outcome**: PASSED

#### Log out

1. Click on the user icon and select the option *"Logout"*.
2. A message will appear asking if you as a user want to log out, for testing purposes click on the *"Cancel"*
button. The expected result is that the user remains logged in and is redirected to the home page.
3. Again, click on the user icon, and select the *"Logout"* option.
4. When the message appears again asking if the user wants to logout, now press the *"Logout"* button. The expected 
result is that the user will effectively be logged out and will be redirected to the home page.

**Test Outcome**: PASSED

#### Reset account password

1. Try to log in again with the created account, but pretend you have forgotten the password. To do this, click on the link 
that says *"Forgot Password?"* in order to recover the account. The expected result is that the user will be redirected to a 
form to perform this action.
2. Inside the reset password form enter the email with which you registered to the website, then click on the *"reset my password"* 
button. The expected result is that the user receives an email with a link to create a new password, and that email looks like 
the following:

![Reset password link example](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/reset_password_link.jpg?raw=true)

3. Once the link to reset the password is clicked, you must enter a new password 2 times in the form that appears. The expected 
result is that the user has indeed changed the password.
4. Finish trying to log in again with the new password. The expected result is that the user will indeed be able to log in to 
his/her created account using the newly created password.

**Test Outcome**: PASSED

#### Read a Blog post and comment on it

All website users can read the blog posts published on there, the difference resides in the fact that **only users who have a profile 
account created** and are **logged in** can write a comment within the blog posts. Explained this the technical tests consist of the following:

1. Go to the nav bar and click on the **"Blog"** nav link. The expected result is that the user should be able to access the blog page and 
see all the published blog posts.
2. Browse into the blog page and click on the *"Read more"* button on the selected blog post. The expected result is indeed the user will 
be redirected to a page that displays the selected blog post in detail.
3. Once inside the blog post in detail, check that it has an image, the blog post content, 2 buttons at the bottom (one to go back to the 
blog page and another to go to the home page), comments (if this blog post has any), and if there are no comments, a message should appear 
warning the user that there are no comments. The expected result is that all the mentioned elements appear on this page.
4. Then check that indeed the form to write a comment is displayed, and also has autocomplete 2 fields of the form that would be the user's 
name and email. The expected result is that the logged in user has access to the form to leave comments. If a user is not logged in, only a 
message will appear inviting the customer to create an account to leave a comment on the blog post.
5. Now type something in the comment form field. Once done, click on the *"Submit"* button to leave your comment inside the blog post. The 
expected result is that a message will appear with a green background indicating to the user that his/her comment is awaiting moderation 
by the online store.

**Note:** to activate the newly published comment, is necessary to *log in as a super user* and activate it from the administration panel. 

**Test Outcome**: PASSED

#### Read website reviews and write a review

All online store users have access to read the reviews about the service provided by the website, the difference is that **only users who have 
an account created** and are **logged in** can write a review evaluating the service of the e-commerce website. Having explained this, the tests 
performed are the following:

1. Go to the navigation bar and click on the nav link **"Reviews"**. The expected result is that the user can access all posted reviews 
in the online store.
2. Check that the following elements are present: 
    - A cover image should appear at the top of the page.
    - All the reviews written by users should appear, and should indicate the total number of reviews.
    - Each review must have a user profile image (or upload a default image if the user hasn't uploaded any image yet), the user's name, date of 
    publication, number of stars given and finally a comment evaluating the quality of the service offered.
3. Once you have checked the above, you must now click on the *"write my review"* button. The expected result if the user is logged in is being 
redirected to the review form, but in case the user is not logged in or doesn't have an account created, he/she will be redirected to the 
sign in page.
4. After the above, check that the form to write a review is indeed displayed. The expected result is that the page to write a review has a 
cover image, and a form is displayed to perform the task of writing a review.
5. Check the form fields of name and email are autofilled with the data provided by the user at the time of registration. The expected result 
is that the form fields are effectively pre-filled.
6. Attempts to leave a review without completing a form field. The expected result is that a message appears indicating that the user must 
fill in that field and cannot leave the review on the website.
7. Write a review about the service provided and also select the number of stars you want to give (the scale is from 1 to 5 stars). 
Then click on the *"Add my review"* button. The expected result is that the user will be redirected to the reviews page, and a message 
will appear telling the user that his/her review is being moderated by the website administrators.

**Note:** to activate the newly published review, is necessary to *log in as a super user* and activate it from the administration panel. 

**Test Outcome**: PASSED

#### Contact page functionality

The contact page can be used as a method of direct communication between the website users and the online store administrators. This page has 
a contact form that the customer must fill in in order to send a message to the website administrators. Having explained that, the tests performed 
are the following:

1. Go to the navbar and click on the nav link **Info** and select the option of **Contact**. The expected result is that the user can access to the
contact page.
2. Check that the contact page has a cover image at the top and that the contact form is displayed. The expected result is that it effectively 
has the elements described above and also if the user is logged in, 2 fields of the form must be pre-filled, which are the full name and email, 
since these fields use the data provided by the user at the time of registration.
3. Try to send a message without filling any of the form fields. The expected result is that the form warns that some form fields are missing and 
the user is not allowed to send a message.
4. Fill in all the form fields and then press the *"Send message"* button. The expected result is that the message is indeed sent, and is received 
by the website administrators in the website email. In addition the user will be redirected to the home page and a message will appear advising the 
user that his/her message was successfully sent and that the website administrators will contact him/her within 48 hours at the latest.

**Note:** In order to check that indeed the website email receives the messages sent by the users I've taken the following screenshots:

Contact form screenshot

![Contact form example](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/contact_email_example_form.jpg?raw=true)

Contact email screenshot

![Contact email example](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/contact_email_example.jpg?raw=true)

For security reasons, **I cannot give any sensitive data** such as the password of the email address used by the website, therefore the screenshot 
above is a reliable proof that the contact form is indeed working properly.

**Test Outcome**: PASSED

#### Products Management

This is a feature that only members of the online store staff can use. This functionality is CRUD compliant and in order to access this feature, 
**the person must be logged in as a super user**. Explained this, the tests consist of the following:

**Add a new product**

1. Click on the user profile icon and select the **"Product Management"** option. The expected result is that the Admin user will be taken 
to a page containing a form to enter a new product.
2. Check the Add Product form is indeed displayed. The expected result is that the administrator user can see the form and it contains some 
placeholders giving some examples of how to fill in each form field.
3. Start filling the form and leave some required fields uncompleted. The expected result is that the form warns that some missing fields 
must be completed and at the same time it won't be possible to add a new product.
4. Try to modify the form field for *"Weight Unit"*. The expected result is that it cannot be modified since all products on the website are 
stored in kilograms (this also includes products containing liquids).
5. Complete the form to add a new product, but with the exception that you must not upload any picture. The reason to do this is to test 
if indeed in the case of no image is uploaded, the website will display a default image. Once this is done, click on the *"Add product"* 
button to add the new product. The expected result is that the product will indeed be saved in the database and the super user will be 
redirected to the page that hosts the new product.
6. Search for the newly added product within the category you selected when you added it, or simply search for it by its name in the search bar. 
The expected result is that the new product will indeed be found with the other products and that the default image will have the same 
dimensions as the products with custom images.

**Test Outcome**: PASSED

**Edit a product**

The products can be edited from the product page, which contains 2 links (to edit or delete the product) or from the product detail page 
itself which contains 2 additional buttons (one to edit and another to delete the product itself) and which only appear if the super user is 
logged in. That explained, the tests to be performed are the following:

1. From the product page, click on the *"edit"* link to modify the product. The expected result is that the administrator will be redirected 
to a page containing the form to edit the product.
2. Check that the form is indeed displayed and contains the data you entered when adding the product. The expected result is that the form 
actually loads the data previously entered.
3. Modify a little the field of the form that is for the product description and also add an image for the newly created product. Then click 
on the *"Update product"* button. The expected result is that the user will be redirected to the page containing the product itself and the 
modifications made should be saved.
4. Search again for the product within the category or using the search bar, in order to check if indeed the newly saved image looks good and
has the same size as the images of the rest of the products in the online store.

**Test Outcome**: PASSED

**Delete a product**

1. Click on the product image of your recently added product, and go to view the product in detail. The expected result is that inside the 
page containing the product itself 2 buttons will appear, one to edit and another to delete the product.
2. Click on the *"Delete product"* button. The expected result is that a modal window will appear asking the website administrator if 
he/she wants to delete the selected product.
3. Click on the *"Delete"* button. The expected result is that the product will be deleted and at the same time the administrator will be 
redirected to the product page, and a message will appear warning that the product has been deleted.

**Test Outcome**: PASSED

#### Blog Management

This is a feature that only members of the online store staff can use. This functionality is CRUD compliant and in order to access this feature, 
**the person must be logged in as a super user**. Explained this, the tests consist of the following:

**Add a blog post**

1. Click on the user profile icon and select the **"Blog Management"** option. The expected result is that the Admin user will be taken 
to a page containing a form to enter a new blog post.
2. Check that the form to add a blog post is indeed displayed. The expected result is that the administrator user can see the form and it 
contains some placeholders that give some examples of how to fill in each form field and also there is a special field with a text editor 
for the content form field.
3. Try to add a blog entry without completing one of the required fields. The expected result is that an error message will appear advising 
the website administrator that you have not completed a field or that you have completed one incorrectly. 
4. Select *"Admin"* as the author (you can select any website user, but it would look odd to select another user), and also complete the other 
fields leaving the image field blank. The reason for this is to test that the website will display a default image in case no image is uploaded 
to the published post, also select the *"Publish"* option in the status field. Then press the "Add post" button. The expected result is that the 
new blog post will be added and the administrator will be redirected to the page containing the new blog post.
5. Look for the newly published post within the blog page. The expected result is that the new blog post will indeed appear and the default 
image will be displayed and will have the same dimensions as the custom images of each blog.

**Test Outcome**: PASSED

**Edit a blog post**

The blog posts can be edited from the blog page, which contains 2 links (to edit or delete a post) or from the blog post detail page 
itself which contains 2 additional buttons (one to edit and another to delete the post itself) and which only appear if the super user is 
logged in. That explained, the tests to be performed are the following:

1. From the blog page, click on the *"edit"* link to modify the blog post. The expected result is that the administrator will be redirected 
to a page containing the form to edit the blog post.
2. Check that the form is indeed displayed and contains the data you entered when adding the new blog post. The expected result is that the form 
actually loads the data previously entered.
3.  Modify a little the form field that contains the content and also add an image for the newly created blog post. Then click 
on the *"Update post"* button. The expected result is that the user will be redirected to the page containing the blog post itself and the 
modifications made should be saved.
4.  Search the blog post inside the blog page, in order to check if indeed the newly saved image looks good and
has the same size as the images of the rest of the blog posts in the online store.

**Test Outcome**: PASSED

**Delete a blog post**

1. Click on the blog post image of your recently added post, and go to view the blog post in detail. The expected result is that inside the 
page containing the blog post itself 2 buttons will appear, one to edit and another to delete the post.
2. Click on the *"Delete post"* button. The expected result is that a modal window will appear asking the website administrator if 
he/she wants to delete the selected post.
3. Click on the *"Delete"* button. The expected result is that the blog post will be deleted and at the same time the administrator will be 
redirected to the blog page, and a message will appear warning that the blog post has been deleted.

**Test Outcome**: PASSED

#### Moderation functionality

This is a feature that **only the super user can access from the administration panel**. In order to enable or disable comments or reviews, the 
tests consist of the following: 

**Comments Moderation**

1. Login to the administration panel, and go to the Blog section. Click on the "comments" link in order to check if there are new comments 
posted. The expected result is that new comments will appear as inactive.
2. Select the comment to moderate and select the *"approve comments"* option in the action field. then press the *"Go"* button. The expected 
result is that the comment has indeed been activated and therefore should appear within the blog post that was commented.
3. Go to the blog post that contains the comment you just activated, and check that it is indeed displayed. The expected result is that the 
new comment appears within the corresponding blog post.

**Test Outcome**: PASSED

**Reviews Moderation**

1. Login to the administration panel, and go to the Reviews section. Click on the *"reviews"* link in order to check if there are new reviews 
posted. the expected result is that new reviews will appear as inactive.
2. Select the review to moderate and select the *"approve reviews"* option in the action field. then press the *"Go"* button. The expected 
result is that the review has been activated and should appear on the reviews page.
3. Go to the reviews page, and check that the new review is indeed displayed. The expected result is that the new review appears on 
the review page.

**Test Outcome**: PASSED

### Defensive Design

### Issues during project development

### Tested devices

The following devices were used to perform different tests throughout the development of this project:

* Lenovo Ideapad S410p (Laptop)
* My Custom PC (Desktop)
* Asus FX505D (Laptop)
* Xiaomi Mi A1 (Mobile)
* Xiaomi Poco x3 NFC (Mobile)
* Iphone S20 (Mobile)
* Ipad Mini 2 (Tablet)

##### [Back to top](#testing-contents)
---
> Note: in order to be able to test features related to the website's super user or admin, essential information 
such as username and password will be given along with the submission form for this project. 