    function showLoadingMessage() {
        // Показываем сообщение "Подождите, идет перевод"
        document.getElementById('loading-message').style.display = 'block';

        // Отключаем все кнопки, чтобы избежать повторного нажатия
        const buttons = document.querySelectorAll('#language-form button');
        buttons.forEach(button => button.disabled = true);
    }