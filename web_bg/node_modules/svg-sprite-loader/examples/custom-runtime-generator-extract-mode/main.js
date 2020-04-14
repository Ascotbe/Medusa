import symbolData from '../assets/twitter.svg';
// => {width: string, height: string, viewBox: string, url: string}

console.log(symbolData);

window.addEventListener('DOMContentLoaded', () => {
  const image = `<img src="${symbolData.url}" width="${symbolData.width}" height="${symbolData.height}">`;
  document.body.innerHTML = image;
});
