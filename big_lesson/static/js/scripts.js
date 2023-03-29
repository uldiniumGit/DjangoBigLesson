document.addEventListener('DOMContentLoaded', () => {
  const newsList = document.querySelectorAll('.news-item');

  newsList.forEach((newsItem) => {
    const newsTitle = newsItem.querySelector('.news-title');
    const newsText = newsItem.querySelector('.news-text');
    newsText.style.display = 'none';
    newsTitle.addEventListener('click', () => {
      newsList.forEach((item) => {
        if (item !== newsItem) {
          item.querySelector('.news-text').style.display = 'none';
        }
      });

      if (newsText.style.display === 'none') {
        newsText.style.display = 'block';
      } else {
        newsText.style.display = 'none';
      }
    });
  });
});