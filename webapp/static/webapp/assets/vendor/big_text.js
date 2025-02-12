document.addEventListener('DOMContentLoaded', function() {
    const fontSizeSelector = document.getElementById('fontSizeSelector');

    if (!fontSizeSelector) {
        console.error('Элемент "fontSizeSelector" не найден.');
        return;
    }

    // Функция изменения шрифта
    function changeFontSize(size) {
        localStorage.setItem('fontSize', size);
        document.body.style.fontSize = size + 'px';
    }

    // Устанавливаем сохраненный размер шрифта
    let savedFontSize = localStorage.getItem('fontSize') || 16;
    document.body.style.fontSize = savedFontSize + 'px';

    // Устанавливаем значение в селекте
    fontSizeSelector.value = savedFontSize;

    // Изменение при выборе
    fontSizeSelector.addEventListener('change', function() {
        changeFontSize(this.value);
    });
});
