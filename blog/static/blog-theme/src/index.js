import Macy from 'macy';

document.addEventListener('DOMContentLoaded', () => {
  console.log('Hello Bulma!');
  const macyInstance = Macy({
    container: '.images',
    columns: 3,
    margin: 10,
  });
});
