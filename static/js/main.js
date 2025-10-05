// Animação de scroll suave
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Destacar link ativo na navbar
const currentLocation = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-links a');

navLinks.forEach(link => {
    if (link.getAttribute('href') === currentLocation) {
        link.style.color = 'var(--dourado)';
        link.style.borderBottom = '2px solid var(--dourado)';
    }
});

// Animação de fade-in ao scroll
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Aplicar animação aos elementos da galeria
document.addEventListener('DOMContentLoaded', () => {
    const galleryItems = document.querySelectorAll('.gallery-grid img');
    
    galleryItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(30px)';
        item.style.transition = `all 0.6s ease ${index * 0.1}s`;
        observer.observe(item);
    });

    // Validação do formulário de contato
    const contactForm = document.querySelector('.contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            const nome = document.getElementById('nome').value.trim();
            const email = document.getElementById('email').value.trim();
            const mensagem = document.getElementById('mensagem').value.trim();

            if (nome.length < 3) {
                e.preventDefault();
                alert('Por favor, insira um nome válido (mínimo 3 caracteres)');
                return false;
            }

            if (!validateEmail(email)) {
                e.preventDefault();
                alert('Por favor, insira um e-mail válido');
                return false;
            }

            if (mensagem.length < 10) {
                e.preventDefault();
                alert('Por favor, insira uma mensagem mais detalhada (mínimo 10 caracteres)');
                return false;
            }

            // Se chegou aqui, mostra mensagem de sucesso
            alert('Mensagem enviada com sucesso! Entraremos em contato em breve.');
        });
    }
});

// Função para validar e-mail
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

// Efeito parallax suave no hero - REMOVIDO para evitar bugs de sobreposição
// window.addEventListener('scroll', () => {
//     const hero = document.querySelector('.hero');
//     if (hero) {
//         const scrolled = window.pageYOffset;
//         hero.style.transform = `translateY(${scrolled * 0.5}px)`;
//     }
// });

// Adicionar classe ao navbar ao scroll
let lastScroll = 0;
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('.navbar');
    const currentScroll = window.pageYOffset;

    if (currentScroll > 100) {
        navbar.style.padding = '1rem 8%';
        navbar.style.boxShadow = '0 6px 30px rgba(212, 175, 55, 0.4)';
    } else {
        navbar.style.padding = '1.5rem 8%';
    }

    lastScroll = currentScroll;
});

// Lightbox simples para galeria (clique para ampliar)
document.addEventListener('DOMContentLoaded', () => {
    const galleryImages = document.querySelectorAll('.gallery-grid img');
    
    galleryImages.forEach(img => {
        img.style.cursor = 'pointer';
        
        img.addEventListener('click', () => {
            // Criar overlay
            const overlay = document.createElement('div');
            overlay.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(0, 0, 0, 0.95);
                z-index: 9999;
                display: flex;
                align-items: center;
                justify-content: center;
                cursor: pointer;
                animation: fadeIn 0.3s ease;
            `;

            // Criar imagem ampliada
            const enlargedImg = document.createElement('img');
            enlargedImg.src = img.src;
            enlargedImg.alt = img.alt;
            enlargedImg.style.cssText = `
                max-width: 90%;
                max-height: 90%;
                border: 4px solid #d4af37;
                border-radius: 10px;
                box-shadow: 0 0 50px rgba(212, 175, 55, 0.5);
                animation: zoomIn 0.3s ease;
            `;

            overlay.appendChild(enlargedImg);
            document.body.appendChild(overlay);

            // Fechar ao clicar
            overlay.addEventListener('click', () => {
                overlay.style.animation = 'fadeOut 0.3s ease';
                setTimeout(() => overlay.remove(), 300);
            });
        });
    });
});

// Adicionar animações CSS dinamicamente
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes fadeOut {
        from { opacity: 1; }
        to { opacity: 0; }
    }
    @keyframes zoomIn {
        from { 
            transform: scale(0.8);
            opacity: 0;
        }
        to { 
            transform: scale(1);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

console.log('🔥 Barber Guh Portfolio - Loaded Successfully!');