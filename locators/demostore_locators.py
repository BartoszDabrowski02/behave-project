NAVIGATION_BAR_LOCATORS = {
    "Home": {
        "type": "xpath",
        "locator": ".//ul[@class='nav-menu']//a[text()='Home']",
    },
    "Cart": {
        "type": "xpath",
        "locator": ".//ul[@class='nav-menu']//a[text()='Cart']",
    },
    "Checkout": {
        "type": "xpath",
        "locator": ".//ul[@class='nav-menu']//a[text()='Checkout']",
    },
    "My account": {
        "type": "xpath",
        "locator": ".//ul[@class='nav-menu']//a[text()='My account']",
    },
    "Sample Page": {
        "type": "xpath",
        "locator": ".//ul[@class='nav-menu']//a[text()='Sample Page']",
    },
}

OTHER_LOCATORS = {
    "number_of_items_in_cart": {
        "type": "css",
        "locator": "a.cart-contents span.count",
    },

}