const customerSelect = document.getElementById('customer');
const selectActionBtn = document.getElementById('select-action');
const actionButtons = document.getElementById('action-buttons');
const customer1Div = document.getElementById('customer1-div');
const customer2Div = document.getElementById('customer2-div');
const customer3Div = document.getElementById('customer3-div');

customerSelect.addEventListener('change', function () {
    const selectedValue = this.value;

    if (selectedValue === "select_customer") {
        selectActionBtn.classList.add('hidden');
        actionButtons.classList.add('hidden');
        hideAllCustomerDivs();
    } else {
        selectActionBtn.classList.remove('hidden');
        actionButtons.classList.add('hidden');
        hideAllCustomerDivs();
    }
});

selectActionBtn.addEventListener('click', function () {
    actionButtons.classList.toggle('hidden');
});

function hideAllCustomerDivs() {
    customer1Div.classList.add('hidden');
    customer2Div.classList.add('hidden');
    customer3Div.classList.add('hidden');
}

function showCustomerDiv(customerDiv) {
    hideAllCustomerDivs();
    customerDiv.classList.remove('hidden');
}

document.getElementById('button1').addEventListener('click', function () {
    showCustomerDiv(customer1Div);
});

document.getElementById('button2').addEventListener('click', function () {
    showCustomerDiv(customer2Div);
});

document.getElementById('button3').addEventListener('click', function () {
    showCustomerDiv(customer3Div);
});