// avaScript script that updates the text color of the <header> element to red
const header = document.querySelector('header');

if (header) {
    header.style.color = '#FF0000';
} else {
    console.error('Header element not found.');
}
