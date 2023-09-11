$(document).ready(function () {
    // Initialize zone selection
    var selectedZone = 0;

    // Initialize public and private button options
    var publicOptions = [0, 1];
    var privateOptions = [0, 1, 2];

    // Handle zone button clicks
    $("#zone-btn-1").click(function () {
        selectedZone = 1;
        publicOptions = [0, 1];
        privateOptions = [0, 1, 2];
        updateButtons();
        updateContent();
    });

    $("#zone-btn-2").click(function () {
        selectedZone = 2;
        publicOptions = [0, 2];
        privateOptions = [0, 2, 4];
        updateButtons();
        updateContent();
    });

    $("#zone-btn-3").click(function () {
        selectedZone = 3;
        publicOptions = [0, 3];
        privateOptions = [0, 3, 6];
        updateButtons();
        updateContent();
    });

    // Handle public button clicks
    $("#public-btn-0").click(function () {
        selectedPublic = 0;
        updateContent();
    });

    $("#public-btn-1").click(function () {
        selectedPublic = 1;
        updateContent();
    });

    // Handle private button clicks
    $("#private-btn-0").click(function () {
        selectedPrivate = 0;
        updateContent();
    });

    $("#private-btn-1").click(function () {
        selectedPrivate = 1;
        updateContent();
    });

    $("#private-btn-2").click(function () {
        selectedPrivate = 2;
        updateContent();
    });

    // Function to update button labels
    function updateButtons() {
        $("#public-btn-0").text(publicOptions[0]);
        $("#public-btn-1").text(publicOptions[1]);
        $("#private-btn-0").text(privateOptions[0]);
        $("#private-btn-1").text(privateOptions[1]);
        $("#private-btn-2").text(privateOptions[2]);
    }
});




const btn1 = document.getElementById('zone-btn-1');
const btn2 = document.getElementById('zone-btn-2');
const btn3 = document.getElementById('zone-btn-3');
const selectContainer = document.getElementById('select-container');
let currentSelects = [];

// Function to create and display select tags
function createSelects(num) {
    // Clear the container
    selectContainer.innerHTML = '';
    for (let i = 0; i < num; i++) {
        const select = document.createElement('select');
        select.innerHTML = '<option value="option1">Option 1</option><option value="option2">Option 2</option><option value="option3">Option 3</option>';
        selectContainer.appendChild(select);
        currentSelects.push(select);
    }
}

btn1.addEventListener('click', () => {
    createSelects(1);
    updateSelects();
});

btn2.addEventListener('click', () => {
    createSelects(2);
    updateSelects();
});

btn3.addEventListener('click', () => {
    createSelects(3);
    updateSelects();
});

// Function to update select options
function updateSelects() {
    currentSelects.forEach((select, index) => {
        select.addEventListener('change', (event) => {
            const selectedValue = event.target.value;
            currentSelects.forEach((s, i) => {
                if (i !== index) {
                    // Disable the same option in other select tags
                    s.querySelector(`option[value="${selectedValue}"]`).disabled = true;
                }
            });
        });
    });
}

const publicBtn0 = document.getElementById('public-btn-0');
const publicBtn1 = document.getElementById('public-btn-1');
const publicInputContainer = document.getElementById('public-input-container');

const privateBtn0 = document.getElementById('private-btn-0');
const privateBtn1 = document.getElementById('private-btn-1');
const privateBtn2 = document.getElementById('private-btn-2');
const privateInputContainer = document.getElementById('private-input-container');

function clearInputContainer(container) {
    container.innerHTML = '';
}

publicBtn0.addEventListener('click', () => {
    clearInputContainer(publicInputContainer);
});

publicBtn1.addEventListener('click', () => {
    clearInputContainer(publicInputContainer);
    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('placeholder', 'Public Input');
    publicInputContainer.appendChild(input);
});

privateBtn0.addEventListener('click', () => {
    clearInputContainer(privateInputContainer);
});

privateBtn1.addEventListener('click', () => {
    clearInputContainer(privateInputContainer);
    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('placeholder', 'Private Input');
    privateInputContainer.appendChild(input);
});

privateBtn2.addEventListener('click', () => {
    clearInputContainer(privateInputContainer);
    for (let i = 0; i < 2; i++) {
        const input = document.createElement('input');
        input.setAttribute('type', 'text');
        input.setAttribute('placeholder', 'Private Input ' + (i + 1));
        privateInputContainer.appendChild(input);
    }
});


