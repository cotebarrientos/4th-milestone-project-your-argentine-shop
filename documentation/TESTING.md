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
- **base.css** has 14 **warnings**.

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

##### [Back to top](#testing-contents)
---
## Browser Compatibility

In order to ensure that the website would work properly in the following browsers, responsiveness tests, button and link checks were done, as well 
as tests on the look of the website to ensure that the colors, images and fonts used would display correctly.

| Browser       | Responsiveness | Appearance    |
| :-----------: | :-----------:  | :-----------: |
| Chrome        |  |  |
| Firefox       |  |  |
| Avast Secure  |  |  |
| Edge          |  |  |
| IE            |  |  |
| Safari        |  |  |

##### [Back to top](#testing-contents)
---
## Responsiveness

I made the following response tests in order to ensure that the website operates correctly and at the same time that its components are seen harmoniously 
arranged in different screen sizes, so that I used the following tools to help me.

* **Mozilla Firefox DevTools**: This browser was used to check the behavior of the web page in different screen sizes using the Developer Tools. Tests consisted in testing the appearance of the fonts used, the aspect of colors and backgrounds, the order and space used by the different elements that make up the web page.

* **Google Chrome DevTools**: This browser was used to check the behavior of the web page in different screen sizes using the Developer Tools. As in the previous browser, different tests were performed checking the aspect of the font used, colors and backgrounds, and finally, the space used by the elements of the website. In addition, a contrast was made between both browsers, checking for any existing differences.

* **Xiaomi Mi A1**: This mobile device was used to test the behavior of the website, using browsers such as *Chrome, Mozilla Firefox* and *DuckDuckGo*.

* **Xiaomi Poco x3**: This mobile device was used to test the behavior of the website, using browsers such as Chrome, Mozilla Firefox and DuckDuckGo.

* **Iphone S20**: This mobile device was used to test the behavior of the website, using browsers such as *Chrome* and *Safari*.

* **Ipad Mini 2**: This device was used to test the behavior of the website, using browsers such as *Chrome* and *Safari*.


| Device            | Responsiveness | Type           |
| :---------------: | :------------: | :------------: |  
| Desktop >1200px   |  | Virtual |
| Desktop 1024px    |  | Virtual |
| Ipad PRO          |  | Virtual |
| Ipad              |  | Virtual |
| Ipad Mini         |  | Virtual |
| Iphone 6/7/8 plus |  | Virtual |
| Iphone 6/7/8      |  | Virtual |
| Iphone 5          |  | Virtual |
| Xiaomi Mi A1      |  | Physical Device |
| Xiaomi Poco x3    |  | Physical Device |
| Iphone S20        |  | Physical Device |
| Ipad Mini 2       |  | Physical Device |


##### [Back to top](#testing-contents)
---
## Manual Testing

### Links Functionality
### User Stories Functionality
### Defensive Design
### Issues during project development
### Tested devices

##### [Back to top](#testing-contents)
---