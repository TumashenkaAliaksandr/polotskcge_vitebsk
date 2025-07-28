document.addEventListener('DOMContentLoaded', function() {
    const searchIcon = document.querySelector('.search-icon');
    const searchBox = document.querySelector('.search-box-wrap');
    const searchResultsBlock = document.getElementById('search-results-block');
    const inputSearch = document.getElementById('s');

    if (searchIcon && searchBox) {
        searchIcon.addEventListener('click', e => {
            e.preventDefault();

            if (searchBox.style.display === 'none' || searchBox.style.display === '') {
                searchBox.style.display = 'block';
                inputSearch.focus();
            } else {
                searchBox.style.display = 'none';
                searchResultsBlock.style.display = 'none';
            }
        });
    }

    if (inputSearch) {
        let timer = null;

        inputSearch.addEventListener('input', () => {
            const query = inputSearch.value.trim();

            // Скрываем результаты если пусто
            if (!query) {
                searchResultsBlock.style.display = 'none';
                searchResultsBlock.innerHTML = '';
                if (timer) clearTimeout(timer);
                return;
            }

            // Задержка перед запросом (300мс) чтобы не делать запросы на каждый ввод
            if (timer) clearTimeout(timer);
            timer = setTimeout(() => {
                fetch(`/ru/ajax/search/?s=${encodeURIComponent(query)}`)
                    .then(response => response.json())
                    .then(data => {
                        // Формируем HTML для результатов
                        if (data.results.length > 0) {
                            let html = '<ul class="search-results-list">';
                            data.results.forEach(item => {
                                html += `
                                <li>
                                    <a href="${item.url}">${item.title}</a><br>
                                    <small>${item.date} | ${item.location}</small>
                                    <p>${item.description}...</p>
                                </li>`;
                            });
                            html += '</ul>';

                            searchResultsBlock.innerHTML = html;
                            searchResultsBlock.style.display = 'block';
                        } else {
                            searchResultsBlock.innerHTML = '<p id="no-results-message">Ничего не найдено</p>';
                            searchResultsBlock.style.display = 'block';
                        }
                    })
                    .catch(err => {
                        console.error('Ошибка при поиске:', err);
                        searchResultsBlock.innerHTML = '<p>Ошибка поиска</p>';
                        searchResultsBlock.style.display = 'block';
                    });
            }, 300);
        });
    }
    // Скрываем при клике вне области поиска
    document.addEventListener('click', function(event) {
        const target = event.target;

        const clickInsideSearchBox = searchBox.contains(target);
        const clickInsideResults = searchResultsBlock.contains(target);
        const clickOnIcon = searchIcon.contains(target);

        if (!clickInsideSearchBox && !clickInsideResults && !clickOnIcon) {
            // Клик вне поля поиска, результатов и иконки — скрываем все
            if (searchBox.style.display === 'block') {
                searchBox.style.display = 'none';
            }
            if (searchResultsBlock.style.display === 'block') {
                searchResultsBlock.style.display = 'none';
                searchResultsBlock.innerHTML = '';
            }
        }
    });
});
