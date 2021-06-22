![Mockups](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/mockups.jpg?raw=true)
# Your Argentine Shop
## Code Institute: Milestone Project 4

This website aims to be a 100% **E commerce Platform**, where shoppers can buy a **wide variety of Argentine products in Ireland**, whose main purpose is to make 
users feel of that nationality at home, offering quality products and providing a great service through a friendly user interface.

This project is part of my **Code Institute Full Stack Software Development** studies, and at the same time is my last project of this, so I decided to make a 
website 100% E commerce with Argentine products, using all the knowledge acquired throughout this course, hoping to bring this great idea to reality in the future.

<a href="https://your-argentine-shop.herokuapp.com/" target="_blank">Click here to view the project live</a>

---
## Contents

1. [**UX**](#ux)
   * [Main Aims](#main-aims)
   * [Ideal User](#ideal-user)
   * [User Stories](#user-stories)
   * [Design Process](#design-process)
       * [Strategy Plane:](#strategy-plane)
       * [Scope](#scope)
       * [Structure](#structure)
       * [Skeleton](#skeleton)
       * [Surface](#surface)
    * [Wireframes](#wireframes)
2. [**Features**](#features)
   * [Existing Features](#existing-features)
   * [Features Left to Implement](#features-left-to-implement)
   * [Future Features Ideas](#future-features-ideas)
3. [**Technologies Used**](#technologies-used)
    * [Languages](#languages)
    * [Databases](#databases)
    * [Libraries](#libraries)
    * [Django Libraries](#django-libraries)
    * [Tools Used](#tools-used)
4. [**Testing**](#testing)
5. [**Deployment**](#deployment)
    * [Clone Project from GitHub](#clone-project-from-github)
    * [Local Deployment](#local-deployment)
    * [Remote Deployment](#remote-deployment)
6. [**Credits**](#credits)
    * [Content](#content)
    * [Media](#media)
    * [Code](#code)
    * [Acknowledgements](#acknowledgements)

---
## UX

### Main Aims

**1.** To Provide a 100% E Commerce Platform with a wide variety of Argentine products in Ireland.

**2.** To make the website interactive and easy to navigate for prospective shoppers.

**3.** To make the website simple to use for potential shoppers, allowing easy checkout, in which the shopper will be able to create their shopping list, 
review it, edit it or remove items. At the same time allow customers to shop with or without a user account.

**4.** To make a platform that allows potential customers to create a user account, where they can save their data for future purchases, facilitating the 
purchase time.

**5.** To make a website that has a good payment system, secure and bug free.

**6.** To create a design that would be fully responsive on all devices and screen sizes.

### Ideal User

#### The Ideal User for this website is:

**1.** Who is Argentinean or South American and likes to consume the products offered by the website.

**2.** Who lives in the Republic of Ireland.

**3.** Who likes to shop online.

#### The Occasional User:

**1.** Who is not Argentinean or South American, but would like to try the products offered on the web site.

#### This Project is the best way to help them achieve these things because:

**1.** This is a great platform to buy Argentine products, because it shows the items in an orderly way and this one is simple to use.

**2.** This platform allows customers to create their shopping lists, review the items within it, edit or delete them as appropriate, in an intuitive 
and user-friendly way.

**3.** This platform allows customers to create a user account in a simple way, allowing them to save their shopping lists and personal data, resulting 
in less time spent making a purchase.

**4.** The website contains a wide variety of products, as well as a secure payment system.

**5.** The website has a beautiful design, very intuitive and easily adapts to any mobile device and screen size.

### User Stories

#### “As a Shopper, I would like to .....”

* View the website from any device (mobile phone, tablet or desktop)
* View a list of products and select one to buy.
* View an individual product details, being able to see its price, description and product image.
* Select the quantity of a product.
* View the total of my purchases at any time.
* Sort the list of available products by price.
* Sort the list of available products by category.
* Search for a product by name or description.
* Be able to update or delete an item from the shopping cart.
* Receive an email confirmation after my purchase.
* Create my own account.
* Be able to log in and log out.
* Receive an email confirmation after registering.
* Be able to recover my password in case I forget it.
* Have my own profile.
* Be able to read a blog post or comment on it.
* Be able to leave a review about the service offered.
* View information about the platform (About us and shipping)
* Be able to send a message from the Contact page.
* View information about website policies (Privacy Policy, Refund Policy and Terms of service)

#### “As a Store Owner , I would like to .....”

* Add a new product.
* Edit/update a product.
* Delete a product.
* Add a blog post.
* Edit/update a blog post.
* Delete a blog post.
* Moderate comments on the blog posts or on the review page.

### Design Process
---

#### Strategy Plane

Use agile design to lay the foundations of an E commerce website that is attractive to users who want to buy a product. The strategy is to 
allow users to find the products in a fast and attractive way for the customer by searching by category, price, name, etc.

Offer a variety of Argentinean products, which are not easy to find within the Republic of Ireland, but which are required or desired by
users of that nationality.

The strategy is to create an easy and intuitive to use online store, in which users can browse and find a variety of Argentinean products without problems 
or effort. In addition, the user is offered the possibility to create a profile within the website, which allows to save his/her personal data, facilitating 
the purchase through the E commerce website. It also allows to save the orders placed historically. In addition, the online store has a secure payment system.

In order to make the online store more interesting, we have also implemented a page with blog posts, with really interesting topics about the Argentinean culture.

In addition, to enhance the quality of the service offered, a review page has been implemented, where users can evaluate the service offered.

#### Scope

The scope will be to attract users by offering them simplicity and a quick search of the products offered in the online store with a fast and reliable payment, 
it will also allow them to create a profile in which they can save their personal data, orders made historically, while allowing them to access extra features 
of the website such as commenting on blog posts or leave a review evaluating the service offered.

The business user will be able to add his/her products quickly and easily, edit them or delete them when necessary. In addition the business user will be able 
to add blog posts, edit them or delete them as many times as required. He/she will also be able to moderate comments from blog posts or reviews written by the 
users of the E commerce website.

#### Structure

The site is structured to assist the user in the search for the desired product. Your Argentine Shop is an E commerce website set with the theme of the Argentine 
people, for it takes colors of the flag of this country as well as the most emblematic products and loved by all Argentine people. It also has a blog page, which 
provides interesting information about the argentine culture, arousing interest to learn more about it by users who don't necessarily belong to this country.

The website has a navigation bar with different links, it also has a logo of the website, a search bar on it, 2 icons, one for the users account and another for 
the shopping cart, and a footer that has some information and website copyright, these are the basic structures of the platform. The website has a home page, whose 
purpose is to welcome users, and every time the website is reloaded, it changes the products it displays. The online store is created to generate the desire to buy 
any product offered to the user, for this the importance of showing many images and play with nostalgia in users, since many consumers have been away from Argentina 
for a long period of time and wish to consume the products offered on the website.

#### Skeleton

The link options and drop down buttons guide the user intuitively from the home page to the product purchase stored in the database. Products stored in the database 
will drive all searches in the search bar. In addition the user will be able to sort his search by category, price, names, etc. In addition to product links, the navbar 
also contains information about the website (About Us, Shipping), a Contact page, blog and reviews.

The architecture of this website is user friendly and intuitive at the moment the client decides to make the purchase, selects a product, adjusts the shopping cart 
until the user reaches the checkout and makes the purchase. The information architecture is designed to allow rapid completion of all user objectives.

The images are stored in the AWS S3 bucket, providing a wide variety of images for the online store, and users can also add profile images, creating more identity 
when commenting on blog posts or leaving a review about the service provided.

#### Surface

In order to design the website we used elements related to the argentine culture as a reference, such as products, patriotic symbols or colors that make allusion to 
this country.

During the development process we tried to make the logo design as representative and faithful to the argentine culture as possible. For this purpose, an arduous 
research was done resulting in the creation of the current logo.

The bootstrap button and text colors were respected, signifying success, alert, warning, secondary and muted. Other colors  were also incorporated, looking to make 
the online store more diverse.

The forms were kept very simple (crispy forms were used), in some cases only with placeholders. The focus was on the information provided and required.

A modern and easy to read font was chosen, creating a user-friendly interface that was pleasing to the eye.

The most popular and loved products by Argentineans were chosen, and the most representative images were selected to create a great experience when making a purchase.

**Color Scheme**

*Palette for Header*

| First Header | Second Header | Navbar | Text 1  | Text 2 | Links | Icons |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |:-----------: |:-----------: |
|  ![#317ece](https://via.placeholder.com/15/317ece/000000?text=+)| ![#fafafa](https://via.placeholder.com/15/fafafa/000000?text=+) |![#001c40](https://via.placeholder.com/15/001c40/000000?text=+)|![#fafafa](https://via.placeholder.com/15/fafafa/000000?text=+)|![#000000](https://via.placeholder.com/15/000000/000000?text=+)|![#ffc107](https://via.placeholder.com/15/ffc107/000000?text=+)|![#ffc107](https://via.placeholder.com/15/ffc107/000000?text=+) |
| #317ECE  | #FAFAFA | #001C40  | #FAFAFA | #000000 | #FFC107 | #FFC107 |

*Palette for Information Boxes*

| Box 1  | Box 2 | Text 1  | Text 2 |
| :-----------: | :-----------: | :-----------: | :-----------: |
| ![#cae1ec](https://via.placeholder.com/15/cae1ec/000000?text=+)|![#ececec](https://via.placeholder.com/15/ececec/000000?text=+)| ![#183153](https://via.placeholder.com/15/183153/000000?text=+)| ![#000000](https://via.placeholder.com/15/000000/000000?text=+)|
| #CAE1EC  | #ECECEC | #183153 | #000000 |

*Palette for Footer*

| Color 1  | Color 2 | Text 1  | Text 2 | Links | Icons |
| :-----------: | :-----------: | :-----------: | :-----------: | :-----------: | :-----------: |
| ![#183153](https://via.placeholder.com/15/183153/000000?text=+)|![#001c40](https://via.placeholder.com/15/001c40/000000?text=+)|![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+)|![#fafafa](https://via.placeholder.com/15/fafafa/000000?text=+) |![#ffc107](https://via.placeholder.com/15/ffc107/000000?text=+) |![#ffc107](https://via.placeholder.com/15/ffc107/000000?text=+)|
| #183153  | #001C40  | #FFFFFF | #FAFAFA | #FFC107 | #FFC107 |

**Typography**

 2 Google fonts were used across of this website:
- Roboto
- Oswald 

**Logotype**

![logotype](https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/logo_project_transparent_500px.png?raw=true)

### Wireframes

To make the wireframes for this project, I used Pencil software version 3.1.0. They were made as part of the design process and were saved as a pdf document 
and stored in separate folder; wireframes. All pages are shown how the project would look like on different screen sizes (desktop, tablets and mobiles).

* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/001-home-page.pdf" target="_blank">Home Page</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/002-products.pdf" target="_blank">Products</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/003-product_detail.pdf" target="_blank">Product Detail</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/004-empty_shopping_cart.pdf" target="_blank">Empty Shopping Cart</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/005-shopping_cart.pdf" target="_blank">Shopping Cart</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/006-checkout.pdf" target="_blank">Checkout</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/007-checkout_user_logged.pdf" target="_blank">Checkout / User logged</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/008-order_confirmation.pdf" target="_blank">Order Confirmation</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/009-signup.pdf" target="_blank">Sign Up</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/010-signin.pdf" target="_blank">Sign In</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/011-reset_password.pdf" target="_blank">Reset Password</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/012-profile.pdf" target="_blank">Profile</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/013-superuser_profile.pdf" target="_blank">Super User Profile</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/014-product_management.pdf" target="_blank">Product Management</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/015-blog_management.pdf" target="_blank">Blog Management</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/016-blog.pdf" target="_blank">Blog</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/017-blogpost.pdf" target="_blank">Blogpost Detail</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/018-blogpost_user_logged.pdf" target="_blank">Blogpost Detail / User Logged</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/019-reviews.pdf" target="_blank">Reviews</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/020-add_a_review.pdf" target="_blank">Add a Review</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/021-contact.pdf" target="_blank">Contact Page</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/022-about_us.pdf" target="_blank">About Us Page</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/023-shipping.pdf" target="_blank">Shipping</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/024-privacy_policy.pdf" target="_blank">Privacy Policy</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/025-refund_policy.pdf" target="_blank">Refund Policy</a>
* <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/wireframes/026-terms_of_service.pdf" target="_blank">Terms of Service</a>


##### [Back to top](#contents)
---
## Features
The E commerce website has a variety of features designed to create a great shopping experience for the user.This project complies with all the features 
required in order to complete the latest milestone project, while I have added some extra features in order to create a better experience when shopping 
or visiting this website.
### Existing Features

#### 1. Header and Navbar

The header has a bar at the top of the website, which contains some online store data, such as phone number, email, and 4 icons with some social networks.

Inside the navigation bar, the first part of the navigation bar contains on the left side the website logo, in the central sector there is a search bar 
and on the right side there are 2 icons, one for the user profiles (which is drop down), which shows the *"Register"* and *"Login"* information, when the 
user is not logged in and the second icon is a shopping cart, which shows the amount of items added to it.

The second part of the navigation bar contains the following navigation links:

* **Home**
* **Info**
    - About Us
    - Contact
    - Shipping
* **Shop**
    - Dulce de Leche
    - Yerba Mate
    - Alfajores
    - Cookies
    - Candies
    - Empanadas
    - Accessories
    - Misc
    - Combos
* **All Products**
    - By Price
    - By Category
    - All Products
* **Blog**
* **Reviews**

In addition, when the website is viewed from mobile devices or tablets, the navbar is fully responsive, adapting all elements to the new 
screen size. The website logo appears in the middle and the information bar is above it. The search bar is compressed into a magnifying 
glass icon, which when pressed by a user will show the entire search bar. The user profile and shopping cart icons will appear next to 
the search bar icon. Navigation links will appear in a toggle button on the left side of the navigation bar.

#### 2. Footer

The footer is composed of 2 parts of different blue shades. The first part consists of 3 components which are:

* **Information**
    - Privacy Policy
    - Refund Policy
    - Terms of Service
* **About Us**: Contains a brief description of the website.
* **Contact Us**: Provides information such as address, phone number and email address of the website.

Also, when the footer is viewed from mobile devices or tablets, it is responsive, and the same components can be 
viewed with accordion folding buttons.

The second part consists of 2 components, the left part contains the website copyright and the right part contains 4 icons 
with some social networks which are: *YouTube, Facebook, Instagram* and *Twitter*. 

#### 3. Home Page

It is responsible for welcoming future users. It is divided into 4 sections:

* **Carrousel Images:** It is located at top of the page, this has 5 images, which invite customers to buy products from 
the online store and are changing from time to time.

* **Featured Products:** This section displays 8 random products (except for the combos category products), and these 
products change every time the website is reloaded.
* **Combos:** This section shows 4 random products that only belong to the combos category. These products change every 
time the website is reloaded.
* **An info bar:** This section contains 3 elements whose purpose is to provide some information to the user, and also 
aims to motivate customers to continue browsing through the online store.

#### 4. Info

* **About Us:** This page shows information about the online store, such as company goals and business vision.
* **Contact:** The contact page is designed to create direct communication between customers and the company, 
for this the user must fill out a contact form with his/her data such as name and email, also he/she must write 
the subject and the message he/she wants to write. If the user is logged in, the name and email text fields are 
automatically filled with the data provided at the time of registering with the online store. Once the message 
is sent, it will be received by the company's email, and the web site staff must answer the messages within 48hrs.
* **Shipping:** This page is responsible to provide information about the shipping system that has the online store. 
Here you will find information such as how long it takes to process the shipments, how the shipping price is calculated, 
how much the user has to spend to get free delivery, among other useful information.

#### 5. Blog

On the **Blog page** you will find a variety of **blogposts** related to interesting topics about Argentine culture. Each blogpost 
has an image, date of publication and a brief description truncated in 195 characters, and in oder to read this blogpost, 
the user will have to press the button that says *"Read more"*.

Once inside the selected blogpost, the user will find a title, date of publication, an image, and the content itself. In 
the final part of the blogpost appears the name of the user who wrote it, and 2 buttons that will take you back to the 
*blog page* or *home page*.

Each blogpost has a **comments section**, where only users who have an account created, can leave a comment on it. 

#### 6. Reviews

On the Reviews page you will find the rating that users have made about the quality of service offered by the online store. 
The ratings range from 1 to 5 stars. Each review shows the user's profile picture, full name, date of publication, number 
of stars given, and finally, the comment written by the user.

In order to leave a review, the user must have created an account with the website, otherwise, when clicking on the 
*"write my review"* button, the user will be redirected to the login page.

To write a review, the user must fill out a form, which will ask the full name and email (which are autocompleted with 
the data provided at the time of registering on the website), comment and finally rate with stars.

Once the comment is written, **it must wait to be moderated by the online store staff**.

#### 7. Products

The website has more than *80 products*, which are sorted by **category, price** and **name**. Each product appears with an image, 
its category (9 categories), its name and price. The product of interest can be accessed by clicking on its image.

The categories are as follows:

- Accessories
- Alfajores
- Candies
- Combos
- Cookies
- Dulce de Leche
- Empanadas
- Misc
- Yerba Mate

When the user types a keyword in the **search bar**, it will search through all the products on the website, trying to match that word with a 
product, otherwise, a message will appear that will let the user know that there is nothing related to the search done.

Inside each selected product you will find an image of it, the product name, its price, its category, a brief description of it, an input field 
to select the desired quantity, and 2 buttons, one to return and continue shopping and the other is to add the product into the shopping cart.

#### 8. Shopping Cart

The shopping cart page displays all the items selected by the user. In this instance the user is responsible for adjusting the shopping cart to 
his/her needs, for example the customer can update the quantity of a selected product by pressing the *"update"* button, or delete products from 
the shopping cart by pressing the *"remove"* button. 

In addition the shopping cart displays information about the shopping order such as information about the **selected items, weight, subtotal, 
delivery costs** and **total price**. It also has 2 buttons, one for *"continue shopping"* and the other for *"proceed to checkout"*.
At the bottom of the shopping cart page is an information bar, which consists of motivating the customer to continue shopping.

If there are **no items in the shopping cart**, an image of an empty shopping cart will appear with a message warning that there are no items 
selected, and at the bottom there will appear a button whose purpose is to motivate the user to continue shopping.

#### 9. Checkout

On the Checkout page, the user must fill out a form with essential information to be able to make the purchase and these are:

* **Your Details**
    - Full Name
    - Email Address

* **Shipping Information**
    - Phone Number
    - Street Address 1
    - Street Address 2
    - Town or city
    - County
    - Postal Code
    - Select Country

* **Payment**

In the form will appear a checkbox that will allow to save this information in the user's profile in case he/she is logged in. 
Also if the user is logged in, in the text fields of full name and email will be filled with information provided at the time 
of registering with the website.

At the end of the form 2 buttons will appear. The first one is to adjust the shopping cart and the second one to finalize the purchase.

Also the customer will be able to see a small summary of the products he/she is going to buy.

Once the purchase has been successful, the user will be taken to a page where the **order confirmation will be displayed**. Besides 
that, the user will receive a message in his/her email confirming that the purchase has been successfully completed.

#### 10. Register an Account

The user has the possibility to register for free and create his/her own account. To do so, this project makes use of the 
**Django-Allauth** library for account authentication. To do this the user must fill out a form containing the following data:

- Email Address
- Email Address Confirmation
- Username
- First Name
- Last Name
- Password
- Password (again)

Once the account is registered, the user will receive a confirmation email so he/she can start using the profile account created.

#### 11. Log In

Once the user has created an account, he/she has the possibility to log in as many times as needed by entering his/her email 
address or user name and adding his/her password. 

#### 12. Reset Password

If the user for some reason has forgotten his/her password, the website gives him/her the possibility to reset his/her password. 
To do so, the user must fill in a small form with his/her email address and click on the button that confirms that he/she wants 
to reset the password. When he/she does this, he/she will receive a message in his/her e-mail, with a link that will allow 
him/her to reset his/her password.

#### 13. User Profile

Inside the user's profile page you will find the following features:

- A cover image, with a card on top that welcomes the user with his/her username, you will also find an avatar image there.

- About me box, in which the user has the possibility to write a little about him/herself.

- A form with text fields prefilled by the user and containing information about deliveries.

- A section of historical orders placed by the user, which can be reviewed as many times as needed by the customer.

The user can update his/her profile as many times as he/she wants, for this purpose there is a button that says *"Edit my profile"*, 
which when pressed, will show a modal window with the data that he/she wants to modify. The data that can be modified are the following:

- Select an image
- Edit Bio
- Edit delivery information

Users who have a profile account created, have access to extra features offered by the website, and these are the following:

- Comment within a blogpost (once the comment is made, the user must wait for his comment to be moderated by the website staff).
- Leave a review about the service offered by the online store (the user must also wait for the review to be moderated).
- Each time the customer makes a purchase, the checkout form will be autocompleted.

#### 14. Super User Profile

This profile contains the same as the common user profiles, but with the difference that this user can manage the website 
products or manage blogpost.

When this user logs in, the following links will appear in the profile icon:
- Product Management
- Blog Management
- My Profile
- Logout

**The product management** consists of the following:

* Inside Product management you will find a form to complete in order to add new products. The form contains the following fields:
    - Category
    - Product Code
    - Product Name
    - Description
    - Price
    - Weight
    - Weight Unit
    - Select Image

* Inside the product page, below each product you will find 2 links, one is "edit" and the other is "delete'. The edit link 
will take you to a form similar to the one for adding products, but if you select the delete link, an alert message will appear 
asking if you want to delete the selected product.
* When viewing a product in detail, 2 extra buttons will appear under the product description. The first button is to edit the product, 
and the second is to delete the product. When you press the delete button, a message will appear in a modal window asking if you want 
to delete the selected product.

**The blog management** consists of the following:

* Inside Blog Management you will find a form to add new blogposts. The form contains the following:
    - Title
    - Slug
    - Author
    - Content
    - Snippet
    - Status
    - Select Image

* Inside the blog page, below each blog you will find 2 links, one is "edit" and the other is "delete'. The edit link will take you to a 
form similar to the one to add blogposts, but if you select the delete link, an alert message will appear asking if you want to delete the 
selected blogpost.
* When viewing a blogpost in detail, 2 extra buttons will appear next to the buttons to return to the blog page or to return to the home page. 
The first button is for editing a blogpost, and the second is for deleting a blogpost. When you press the delete button, a message will appear 
in a modal window asking if you want to delete the selected blogpost.

#### 15. Admin Panel

This feature is part of the **Django framework**. Inside the panel are all the modules created and that are part of this website. The Admin panel 
is composed of:

* **Accounts**
    - Email Address
* **Authentication and Authorization**
    - Groups
    - Users
* **Blog**
    - Comments
    - Posts
* **Checkout**
    - Orders
* **Products**
    - Products
    - Categories
* **Profiles**
    - User profiles
* **Reviews**
    - Reviews
* **Sites**
    - Sites
* **Social Accounts**
    - Social accounts
    - Social application tokens
    - Social Applications

In the Admin panel you can change the status of blogposts, as well as moderate comments and reviews left by users.

16. Information pages

These are located in the footer and consist of the following:

- **Privacy Policy:** Contains all the privacy policies within the website.
- **Refund Policy:** Contains the policies that are based on the online store at the time of applying any refund to a customer.
- **Terms of Service:** Contains the terms of service that guide the use of the online store's service.

### Features Left to Implement

The only feature contemplated at the beginning of this project, but due to website features implementation priorities was the 
integration of **3 buttons to share the products on social networks**. It is an interesting feature that I would like to implement 
in the near future.

### Future Features Ideas

Later on I would like to implement the following features:

- The possibility to evaluate the products quality with stars (from 1 to 5 stars).
- Allow users to leave reviews within each product.
- Add a button that allows users to save a product in favorites, and these appear within their user profile.
- Add buttons to share products on social networks.
- Add a like and dislike button within the blog posts.

##### [Back to top](#contents)
---
## Technologies Used

### Languages
* HTML 5
    - The project uses **HTML5** to define the structure of this website.
* CSS 3
    - The project uses **CSS3** to add styling to the website.
* JavaScript 
    - The project uses **Javascript** to add interactivity to the website, to update or delete items from shopping cart and other functionalities.
* <a href="https://www.python.org/" target="_blank">Python</a>
    - The project uses **Python** 3.9.4 to build the backend of this website
* <a href="https://www.djangoproject.com/" target="_blank">Django</a>
    - The project uses **Django** version 3.2 as the framework.

### Databases
* <a href="https://www.postgresql.org/" target="_blank">PostgreSQL</a>
    - The project uses **PostgreSQL** version 13.3 database service provided directly by Heroku.
* <a href="https://www.sqlite.org/index.html" target="_blank">SQlite3</a>
    - The project uses **SQlite3** to program locally, in addition this database is provided by Django.

### Libraries

* <a href="https://jquery.com/" target="_blank">JQuery</a>
    - The project uses **jQuery** version 3.6.0 JavaScript library to simplify HTML DOM manipulation.    
* <a href="https://getbootstrap.com/" target="_blank">Bootstrap</a>
    - The project uses **Bootstrap** version 4.6.0 , to build responsive website.
* <a href="https://popper.js.org/" target="_blank">Popper.js</a>
    - **Popper.js** version 1.16.1 for the Bootstrap components that requires the use of JavaScript to function.
* <a href="https://fontawesome.com/" target="_blank">FontAwesome</a>
    - The project uses **FontAwesome** as icon provider.
* <a href="https://fonts.google.com/" target="_blank">Google Fonts</a>
    - **Google Fonts** is used to style the fonts of the website

### Django Libraries

* <a href="https://django-allauth.readthedocs.io/en/latest/" target="_blank">Django Allauth</a>
    - **Django Allauth** version 0.44.0 to supports multiple authentication schemes, as well as multiple strategies for account verification.
* <a href="https://pypi.org/project/django-ckeditor/" target="_blank">Django Ckeditor</a>
    - **Django Ckeditor** version 6.0.0 to provides a RichTextField and CKEditorWidget.
* <a href="https://pypi.org/project/django-countries/" target="_blank">Django Countries</a>
    - **Django Countries** version 7.1 to provides country choices for use with forms, and a country field for models.
* <a href="https://django-crispy-forms.readthedocs.io/en/latest/install.html" target="_blank">Django Crispy Forms</a>
    - **Django Crispy Forms** version 1.11.2 to style django forms.
* <a href="https://django-storages.readthedocs.io/en/latest/" target="_blank">Django Storages</a>
    - **Django Storages** version 1.11.1 to connects Django to S3 Buckets.

### Tools Used

* <a href="https://code.visualstudio.com/" target="_blank">VS Code</a>
    - **VS Code** version 1.56.2 to write the code for this website.
* <a href="https://github.com/" target="_blank">GitHub</a>
    - **GitHub** is used to host the source code.
* <a href="https://git-scm.com/" target="_blank">Git</a>
    - **Git** is used to control the different versions and history of the code.
* <a href="https://stripe.com/en-se" target="_blank">Stripe API</a>
    - **Stripe API** was used as the payment platform to validate and accept credit card payments in a secure way.
* <a href="https://aws.amazon.com/s3/?nc1=h_ls" target="_blank">AWS S3 Bucket</a>
    - **AWS S3 Bucket** to store images that was entered into the database.
* <a href="https://www.heroku.com/" target="_blank">Heroku</a>
    - **Heroku** used for "platform as a service" for app hosting.
* <a href="https://pypi.org/project/psycopg2/" target="_blank">Psycopg2</a>
    - **Psycopg2** version 2.8.6 as PostgreSQL database adapter for Python
* <a href="https://pypi.org/project/gunicorn/" target="_blank">Gunicorn</a>
    - **Gunicorn** version 20.1.0 as WSGI server implementation used to run Python web application
* <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html" target="_blank">Boto3</a>
    - **Boto3** version 1.17.84 to make use of Amazon S3
* <a href="https://python-pillow.org/" target="_blank">Pillow</a>
    - **Pillow** version 8.2.0 to add support for opening, manipulating, and saving many different image file formats
* <a href="" target="_blank">PIP</a>
    - **PIP** for installation of tools needed in this project.
* <a href="https://pypi.org/project/python-dotenv/" target="_blank">Python Dotenv</a>
    - **Python Dotenv** version 0.17.0 to read key-value pairs from a `.env` file and can set them as environment variables.
* <a href="https://pypi.org/project/black/" target="_blank">Black</a>
    - **Black** version 20.8b1 to fix and format python files.
* <a href="https://www.adobe.com/ie/" target="_blank">Adobe Photoshop</a>
    - **Adobe Photoshop CS6** portable version 13.0.0, to improve the images used in the website.
* <a href="https://www.adobe.com/ie/products/illustrator.html?gclid=EAIaIQobChMI7sax79jo6AIVRuztCh1rOgpzEAAYASAAEgJWMPD_BwE&sdid=88X75SKS&mv=search&ef_id=EAIaIQobChMI7sax79jo6AIVRuztCh1rOgpzEAAYASAAEgJWMPD_BwE:G:s&s_kwcid=AL!3085!3!340697722021!e!!g!!adobe%20illustrator" target="_blank">Adobe Illustrator</a>
    - **Adobe Illustrator CS6** portable version 16.0.0, to draw vectorial images used in the website.
* <a href="https://affinity.serif.com/en-gb/designer/" target="_blank">Affinity Designer</a>
    -  **Affinity Designer** version 1.6.5.123, to make the website logo and typography.
* <a href="https://pencil.evolus.vn/" target="_blank">Pencil</a>
    - **Pencil** version 3.1.0 to create the wireframes.

##### [Back to top](#contents)
---
## Testing

Please view the complete testing process in this separate document <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop/blob/master/documentation/TESTING.md" target="_blank">here</a>.

##### [Back to top](#contents)
---
## Deployment

### Clone Project from GitHub

1. Follow this link to the <a href="https://github.com/cotebarrientos/4th-milestone-project-your-argentine-shop" target="_blank">Project GitHub repository</a>.
2. Scroll to the top of this repository and click on the "clone or download button".
3. Decide whether you want to clone the project using HTTPS or an SSH key and do the following:
    - HTTPS: click on the checklist icon to the right of the URL.
    - SSH key: first click on 'Use SSH' then click on the same icon as above.
4. Open the 'Terminal'.
5. Choose the location for the cloned directory.
6. Type `git clone`, and then paste the clone URL.

    - `git clone https://github.com/USERNAME/REPOSITORY`
7. Press 'Enter' to create your local clone.

### Local Deployment

For local deployment you must have an IDE, like for example **VS Code** (used in this project) and the following to be installed locally on 
your machine: Git, PIP and Python 3. Keep in mind that the python commands described below are intended if you are going to deploy the 
project locally using **Microsoft Windows**, otherwise replace the `python` command with `python3`. Do the same in the case of the `pip` 
command replace it with `pip3`.

1. After cloning this project, navigate to the correct file location after unpacking the files.
    - `cd <path to folder>`
2. Create a `.env` file with your own credentials.
            
            STRIPE_PUBLIC_KEY =  "Your Stripe public key here..."
            STRIPE_SECRET_KEY = "Your Stripe secret key here..."
            STRIPE_WH_SECRET = "Your Stripe WH secret key here..."
            SECRET_KEY = "Your Django secret key here..."
            DEVELOPMENT = True
3. Go to `settings.py` file and add your environment variables.
        	
            import os
            from dotenv import load_dotenv
            load_dotenv() # Necessary to load .env file

            DEBUG = 'DEVELOPMENT' in os.environ
            STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
            STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
            STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
4. Add `.env.py` to `.gitignore` file
5. Then run this command `pip install -r requirements.txt` to install the required modules.
6. Then, run the commands to makemigrations and migrate.
    - `python manage.py makemigrations`
    - `python manage.py migrate`
7. This project contains a fixtures folder, in order to read those JSON files, you have to type the following commands:
    - `python manage.py loaddata categories`
    - `python manage.py loaddata products`
8. Now, run the command to create a super user.
    - `python manage.py createsuperuser` in order to access the *Django Admin Panel*
4. In the terminal, use the following command to launch this Django project:
    - `python manage.py runserver` 
5. After that, this Django project should be running locally on `http//: 127.0.0.1:8000`. 

### Remote Deployment

Once you have the project setup locally, you can proceed to deploy it remotely with the following steps:

1. First, type the command `pip install gunicorn`, which will act as the webserver.
2. Update the `requirements.txt` file using the `pip freeze > requirements.txt` command in the terminal to make all of the installed packages and 
libraries to go in to the file.
3. Then, create a Procfile with the command `echo web: python app.py > Procfile` in the terminal.
4. In Heroku, create a new app. The app must have a unique name.
5. In the new Heroku app, Click on Deploy. In the section Deployment method, click on Github, then choose the correct GitHub repository to 
link it to the Heroku app.
6. In the section Automatic Deploys, click on Enable automatic deploys, from master branch.
7. Go to *setting.py* and update the `ALLOWED_HOSTS` as follows:

        ALLOWED_HOSTS = ['your-argentine-shop.herokuapp.com', 'localhost', '127.0.0.1']
8. Then, we have to temporarily disable collectstatic by using Heroku config set or using the CLI-terminal.  
    - Heroku config vars
        
            DISABLE_COLLECTSTATIC = <1> 

    - CLI-terminal

            $ python manage.py collectstatic
9. After that, go to Resources, within Add-ons search **Heroku Postgres**, choose Hobby Dev - Free version, then click on Provision button.
10. Now go to Settings and click on Reveal config vars, and set the following:

        DATABASE_URL = <The database url>
        DISABLE_COLLECTSTATIC = <1> 

11. Return to terminal  and run `pip install dj_database_url`, and then install `pip install psycopg2`, and update
the *requirements.txt* file using `pip freeze > requirements.txt`.
12. Go to *settings.py* and write the following:

        import os
        import dj_database_url
        from pathlib import Path

        if 'DATABASE_URL' in os.environ:
        DATABASES = {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
        else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
         }


13. After that, run the following commands:

    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py loaddata categories`
    - `python manage.py loaddata products`

14. Then, create a super user.
    - `python manage.py createsuperuser`

15. Sign up for a free Amazon AWS account in order to host your staticfiles and media files. 
16. From the S3 buckets section, you'll need to create a new unique bucket in order to host your
static files. To do that, you have to follow these next steps:
    - Permissions > CORS configuration:

            [
                {
                    "AllowedHeaders": [
                    "Authorization"
                    ],
                    "AllowedMethods": [
                    "GET"
                    ],
                    "AllowedOrigins": [
                    "*"
                    ],
                    "ExposeHeaders": []
                }
            ]

    - Permissions > Bucket Policy:

            {
                "Version": "2012-10-17",
                "Id": "PolicyID",
                "Statement": [
                    {
                    "Sid": "PublicReadGetObject",
                    "Effect": "Allow",
                    "Principal": "*",
                    "Action": "s3:GetObject",
                    "Resource": "arn:aws:s3:::your-bucket-name/*"
                    }
                ]
            }

    - Into  **IAM** section of AWS, you have to create a new group, don't forget to select your existing 
    S3 Bucket details. 
    - Then you have to create a *new policy* and *a new user*. After that, you have to attach these to the Group.
17. Return to terminal and run `pip install django-storages` and `pip install boto3`. Go to settings.py and add 
storages to INSTALLED_APPS.
18. Inside *settings.py* type the following:

        if 'USE_AWS' in os.environ:
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }

        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        # Override static and media URLs in production
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'

19. Return to Heroku, go to Settings and click on Reveal config vars, and set the following:


        AWS_ACCESS_KEY_ID = <Your aws access key>
        AWS_SECRET_ACCESS_KEY = <Your secret aws access key>
        DATABASE_URL = <The database url>
        DEFAULT_FROM_EMAIL = <Your default email>
        DISABLE_COLLECTSTATIC = <1> 
        EMAIL_HOST_PASS = <Your email password>
        EMAIL_HOST_USER = <Your email>
        SECRET_KEY = <Your Django secret key>
        USE_AWS = <True>

20. Login in your **Stripe** account, navigate to Developers section, and get your API keys. Then
type your secret keys in your Heroku config vars.

        AWS_ACCESS_KEY_ID = <Your aws access key>
        AWS_SECRET_ACCESS_KEY = <Your secret aws access key>
        DATABASE_URL = <The database url>
        DEFAULT_FROM_EMAIL = <Your default email>
        DISABLE_COLLECTSTATIC = <1> 
        EMAIL_HOST_PASS = <Your email password>
        EMAIL_HOST_USER = <Your email>
        SECRET_KEY = <Your Django secret key>
        STRIPE_PUBLIC_KEY = <Your Stripe public key>
        STRIPE_SECRET_KEY = <Your Stripe secret key>
        STRIPE_WH_SECRET = <Your Stripe WH secret key>
        USE_AWS = <True>

*Note:* Don't forget that before deploying this project to Heroku, you must do a git commit in order to Heroku 
takes the new changes.
##### [Back to top](#contents)
---
## Credits

#### Content

The products used, as well as the written content within the blog page, as well as general information were consulted from the following websites:

- <a href="https://southamericanshop.com/" target="_blank"> South American Shop</a>
- <a href="https://patagoniaonline.co.uk/" target="_blank">Patagonia Online</a>
- <a href="https://almacenargentino.com/en/" target="_blank">Almacen Argentino</a>
- <a href="https://pampadirect.com/" target="_blank">Pampa direct</a>
- <a href="https://urushop.co.uk/" target="_blank">UruShop</a>


#### Media

- The pictures used for some images cover (Contact page, Shipping and Profile) were obtained from Google images and were improved using Adobe Photoshop.
- Some images used (Reviews cover, carousel images, About us, Reviews form cover) were made using Adobe Photoshop.
- Logotype and images for errors 404 and 500 were made using Adobe Illustrator and Affinity Designer.
- The images from <a href="https://unsplash.com/" target="_blank">Unsplash</a>  were used to create generic fake profile avatars.
- The images from <a href="https://www.iconfinder.com/" target="_blank">Iconfinder</a> were used for the shopping cart information bar and blog page.

#### Code
* These websites were really useful to troubleshooting the issues I faced:
    - <a href="https://stackoverflow.com/" target="_blank">Stackoverflow</a>
    - <a href="https://getbootstrap.com/docs/4.6/getting-started/introduction/" target="_blank">Bootstrap Documentation</a>
    - <a href="https://www.w3schools.com/" target="_blank">w3schools</a>
    - <a href="https://docs.djangoproject.com/en/3.2/" target="_blank">Django documentation</a>
* To build the blog page, comments and reviews
    - <a href="https://djangocentral.com/building-a-blog-application-with-django/" target="_blank">Django Central - Building a Blog</a>
    - <a href="https://djangocentral.com/creating-comments-system-with-django/" target="_blank">Django Central - Creating Comments</a>
* To custom Allauth sign up views
    - <a href="https://www.geeksforgeeks.org/python-extending-and-customizing-django-allauth/" target="_blank">Geeksforgeeks - Extending and customizing django-allauth</a>
    - <a href="https://dev.to/danielfeldroy/customizing-django-allauth-signup-forms-2o1m" target="_blank">Dev - Customizing Django Allauth Signup Forms</a>

* The following YouTubers were really helpful in the most difficult moments doing this project:
    - <a href="https://www.youtube.com/channel/UCFB0dxMudkws1q8w5NJEAmw" target="_blank">Codemy.com</a>
    - <a href="https://www.youtube.com/channel/UCAx4nmhI7S1RcPiaG-Uw0tg" target="_blank">Max Goodridge</a>
    - <a href="https://www.youtube.com/channel/UCTZRcDjjkVajGL6wd76UnGg" target="_blank">Dennis Ivy</a>
    - <a href="https://www.youtube.com/channel/UClXcbBNNhFU9ATAcXB6U7eQ" target="_blank">Lara Code</a>
    - <a href="https://www.youtube.com/channel/UCmOpHGj4JRWCdXhllVTZCVw" target="_blank">The Code Creative</a>
    - <a href="https://www.youtube.com/channel/UC4zS7t0ymP3cqBgDd-e-94A" target="_blank">On Dev</a>
* Part of coding written for this project was based on the source code of the module provided by <a href="https://github.com/ckz8780/boutique_ado_v1" target="_blank">Code Institute Source Code</a>.
#### Acknowledgements

Thank you to the following people who helped with support, inspiration and guidance at different stages in the project:
- My boyfriend.
- My friends and family.
- The guidance and support of my mentor Brian Macharia.

I want to thank **Code Institute**, especially **Student Care** for their support throughout this course, for supporting me in the most difficult moments 
and for giving me the opportunity to finish my studies, since last year was a very complicated year both in the family and personal sphere.
##### [Back to top](#contents)
---

> Disclaimer: The content of this Website is for educational purposes only.
