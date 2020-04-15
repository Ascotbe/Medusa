import React from 'react';
import { render } from 'react-dom';
import TwitterIcon from '../assets/twitter.svg';
import WikipediaIcon from '../assets/wikipedia.svg';

document.addEventListener('DOMContentLoaded', () => {
  render(
    <div>
      <TwitterIcon width="100" />
      <WikipediaIcon width="200" />
    </div>,
    document.querySelector('.app')
  );
});
