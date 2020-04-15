import symbolData from '../assets/twitter.svg';
// => {id string, width: string, height: string, viewBox: string, url: string}

console.log(symbolData);

window.addEventListener('DOMContentLoaded', () => {
  const image = `<img width="${symbolData.width}" height="${symbolData.height}" src="${symbolData.url}">`;
  const usage = `<svg viewBox="${symbolData.viewBox}"><use xlink:href="${symbolData.url}"></use></svg>`;

  document.body.innerHTML = `${image} ${usage}`;
});
