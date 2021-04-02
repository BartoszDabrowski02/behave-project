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

HOME_PAGE_LOCATORS = {
    "products_on_the_page": {
        "type": "xpath",
        "locator": "//ul[@class='products columns-4']/li",
    },
    "product_number_x": {
        "type": "xpath",
        "locator": "//ul[@class='products columns-4']/li[{product_num}]",
    },
    "product_number_x_add_to_cart_button": {
        "type": "xpath",
        "locator": "//ul[@class ='products columns-4']/li[{product_num}]/a[text()='Add to cart']",
    },
    "product_in_cart_by_id": {
        "type": "xpath",
        "locator": ".//ul[contains(@class,'woocommerce-mini-cart')]//a[@data-product_id='{product_id}']",
    },
}

