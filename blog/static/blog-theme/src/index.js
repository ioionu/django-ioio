import Macy from 'macy';

document.addEventListener('DOMContentLoaded', () => {
  console.log('Hello Bulma!');
  const macyInstance = Macy({
    container: '.images',
    columns: 3,
    breakAt: {
      940: 3,
      520: 2,
      400: 1
    },
    margin: 10,
  });
});
