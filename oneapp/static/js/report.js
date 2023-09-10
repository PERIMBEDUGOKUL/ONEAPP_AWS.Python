$(document).ready(function() {
    // Show/hide divs when buttons are clicked
    $("#btn1").click(function() {
        $(".button-div").hide();
        $("#btn1-div").show();
    });

    $("#btn2").click(function() {
        $(".button-div").hide();
        $("#btn2-div").show();
    });

    $("#btn3").click(function() {
        $(".button-div").hide();
        $("#btn3-div").show();
    });

    // Handle customer selection
    $("#customer-select").change(function() {
        var selectedCustomer = $(this).val();

        // Hide all button divs
        $(".button-div").hide();

        // Reset button styles (optional)
        $(".buttons button").removeClass("active");

        // Show the buttons for the selected customer
        if (selectedCustomer !== "select-customer") {
            $(".buttons").show();
        } else {
            $(".buttons").hide();
        }
    });
});