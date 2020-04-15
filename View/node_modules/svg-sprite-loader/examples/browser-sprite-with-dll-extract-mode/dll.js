import symbolData from '../assets/facebook.svg';

// => {id string, width: string, height: string, viewBox: string, url: string}

console.log(`dll: ${symbolData}`);
let image;
let usage;

window.addEventListener('DOMContentLoaded', () => {
  image = `<img width="${symbolData.width}" height="${symbolData.height}" src="${symbolData.url}">`;
  usage = `<svg viewBox="${symbolData.viewBox}"><use xlink:href="${symbolData.url}"></use></svg>`;
});

export function dll() {
  console.log('dll module');

  document.body.insertAdjacentHTML('beforeend', `${image} ${usage}`);
}
