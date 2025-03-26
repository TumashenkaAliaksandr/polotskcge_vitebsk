document.addEventListener('DOMContentLoaded', function() {
    const fontSizeSelector = document.getElementById('fontSizeSelector');
    const DEFAULT_FONT_SIZE = 16;

    if (!fontSizeSelector) {
        console.error('Элемент "fontSizeSelector" не найден.');
        return;
    }

    function resetStyles() {
        document.querySelectorAll(`
            .col-lg-3,
            .col-lg-2,
            .header-search a,
            #footer .footer-top .footer-info,
            #footer .footer-top .footer-info h3,
            #footer .footer-top .footer-info p,
            .news-grid-right2,
            .news-grid-right1,
            .breadcrumbs_contacts ol,
            .breaking-news,
            .iksweb td,
            .footer-links,
            .footer-links h4,
            .footer-links li,
            .navbar a,
            .dropdown-menu a,
            .dropdown-menu li a,
            .features .icon-box h4,
            .features .icon-box p,
            .services .icon-box h6,
            .faq .faq-list i,
            .faq .faq-list .question,
            .contact .info-box p,
            .contact .info-box h3,
            .breadcrumbs ol,
            .count-box p
        `).forEach(element => {
            element.removeAttribute('style');
        });

        document.body.classList.remove('monochrome');
    }

    function changeFontSize(size) {
        resetStyles();

        if (size === 'default') {
            localStorage.removeItem('fontSize');
            document.body.style.fontSize = DEFAULT_FONT_SIZE + 'px';
            return;
        }

        localStorage.setItem('fontSize', size);
        document.body.style.fontSize = size + 'px';

        document.querySelectorAll('.col-lg-3').forEach(element => {
            element.style.width = '33%';
            element.style.marginBottom = '10px';
        });
        document.querySelectorAll('.col-lg-2').forEach(element => {
            element.style.width = '30%';
            element.style.marginBottom = '10px';
        });
        document.querySelectorAll('.count-box p').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.features .icon-box p').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.features .icon-box h4').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.services .icon-box h6').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.faq .faq-list i').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.faq .faq-list .question').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.contact .info-box p').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.contact .info-box h3').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });

        document.querySelectorAll('.breadcrumbs ol').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.dropdown ul .active').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.dropdown li').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });
        document.querySelectorAll('.navbar li').forEach(element => {
            if (size >= 18) {
                element.style.fontSize = `${size * 0.9}px`; // 24px при размере 30px
            } else {
                element.style.fontSize = `${size * 0.7}px`; // 14px при размере 20px
            }
        });

        document.querySelectorAll('.header-search a').forEach(element => {
            element.style.marginLeft = `${size * 2}px`;
        });

        document.querySelectorAll('#footer .footer-top .footer-info').forEach(element => {
            element.style.marginBottom = `${size * 1.5}px`;
        });

        document.querySelectorAll('#footer .footer-top .footer-info h3').forEach(element => {
            element.style.fontSize = `${size * 1.2}px`;
            element.style.marginBottom = `${size * 0.8}px`;
            element.style.lineHeight = '1';
            element.style.fontWeight = '700';
        });

        document.querySelectorAll('#footer .footer-top .footer-info p').forEach(element => {
            element.style.fontSize = `${size * 0.9}px`;
            element.style.lineHeight = `${size * 1.7}px`;
            element.style.marginBottom = '0px';
            element.style.fontFamily = '"Roboto", sans-serif';
        });

        document.querySelectorAll('.news-grid-right2').forEach(element => {
            element.style.margin = `${size * 0.02}em 0 0`;
        });
        document.querySelectorAll('.news-grid-right1').forEach(element => {
            element.style.margin = `${size * 0.0067}em 0 0`;
        });
        document.querySelectorAll('.breadcrumbs_contacts ol').forEach(element => {
            element.style.fontSize = `${size * 0.9}px`;
        });
        document.querySelectorAll('.breaking-news').forEach(element => {
            element.style.padding = `${size * 0.17}px`;
        });
        document.querySelectorAll('.iksweb td').forEach(element => {
            element.style.padding = `${size * 0.5}px ${size * 0.5}px ${size * 0.5}px`;
            element.style.lineHeight = `${size * 1.17}px`;
            element.style.fontSize = `${size * 1}px`;
        });

        document.querySelectorAll('.footer-links').forEach(element => {
            element.style.marginBottom = `${size * 1.5}px`;
        });

        document.querySelectorAll('.footer-links h4').forEach(element => {
            element.style.fontSize = `${size * 1.2}px`;
            element.style.marginBottom = `${size * 0.8}px`;
        });

        document.querySelectorAll('.footer-links li').forEach(element => {
            element.style.fontSize = `${size * 0.7}px`;
            element.style.lineHeight = `${size * 1.7}px`;
            element.style.marginBottom = `${size * 0.5}px`;
        });

        document.querySelectorAll('.navbar a').forEach(element => {
            if (element.parentElement.classList.contains('navbar-brand')) {
                element.style.fontSize = `${size * 0.6}px`;
            } else {
                element.style.fontSize = `${size * 0.6}px`;
            }
        });

        // Установка монохромного стиля для Aa2 и Aa3
        if (size >= 18) {
            document.body.classList.add('monochrome');
        }
    }

    let savedFontSize = localStorage.getItem('fontSize');
    if (!savedFontSize || savedFontSize === 'default') {
        document.body.style.fontSize = DEFAULT_FONT_SIZE + 'px';
        fontSizeSelector.value = 'default';
    } else {
        document.body.style.fontSize = savedFontSize + 'px';
        fontSizeSelector.value = savedFontSize;
        changeFontSize(savedFontSize);
    }

    fontSizeSelector.addEventListener('change', function() {
        if (this.value === 'default') {
            resetStyles();
            document.body.style.fontSize = DEFAULT_FONT_SIZE + 'px';
            localStorage.removeItem('fontSize');
        } else {
            changeFontSize(this.value);
        }
    });
});
