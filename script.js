document.body.style.overflowX = 'hidden';

// Menu hamburger mobile
document.addEventListener('DOMContentLoaded', function() {
  const mobileMenuToggle = document.getElementById('mobileMenuToggle');
  const navLinks = document.getElementById('navLinks');

  if (mobileMenuToggle && navLinks) {
    mobileMenuToggle.addEventListener('click', function() {
      navLinks.classList.toggle('active');
    });

    // Fermer le menu quand on clique sur un lien
    const navLinksItems = navLinks.querySelectorAll('a');
    navLinksItems.forEach(link => {
      link.addEventListener('click', function() {
        navLinks.classList.remove('active');
      });
    });
  }
});

document.addEventListener('DOMContentLoaded', function() {
  const openModalBtn = document.getElementById('openModalBtn');
  const openModalBtnFooter = document.getElementById('openModalBtnFooter');
  const modal = document.getElementById('modal');
  const closeModal = document.getElementsByClassName('close')[0];

  const openPrivacyModalBtnFooter = document.getElementById('openPrivacyModalBtnFooter');
  const privacyModal = document.getElementById('privacyModal');
  const closePrivacyModal = document.getElementsByClassName('close-privacy')[0];

  openModalBtn.onclick = function() {
    modal.style.display = 'block';
  };

  openModalBtnFooter.onclick = function() {
    modal.style.display = 'block';
  };

  openPrivacyModalBtnFooter.onclick = function() {
    privacyModal.style.display = 'block';
  };

  closeModal.onclick = function() {
    modal.style.display = 'none';
  };

  closePrivacyModal.onclick = function() {
    privacyModal.style.display = 'none';
  };

  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = 'none';
    }
    if (event.target == privacyModal) {
      privacyModal.style.display = 'none';
    }
  };
});





/*myprojects */
document.addEventListener('DOMContentLoaded', () => {
  const portfolioItems = document.querySelectorAll('[data-portfolio-item]');
  const modal = document.querySelector('[data-modal]');
  const modalCloseBtn = document.querySelector('[data-modal-close]');
  const modalImg = document.querySelector('[data-modal-img]');
  const modalTitle = document.querySelector('[data-modal-title]');
  const modalDescription = document.querySelector('[data-modal-description]');
  const modalSource = document.querySelector('[data-modal-source]');
  const modalDemo = document.querySelector('[data-modal-demo]');

  portfolioItems.forEach(item => {
    item.addEventListener('click', () => {
      const imgSrc = item.querySelector('.portfolio-img').src;
      const title = item.querySelector('.portfolio-title').innerText;
      const description =item.querySelector('.portfolio-description').innerText;
      const demoLinkElement = item.querySelector('.portfolio-demo-link');
      const sourceLink = item.querySelector('.portfolio-source');

      modalImg.src = imgSrc;
      modalTitle.innerText = title;
      modalDescription.innerText = description;
      modalSource.href = sourceLink;

      if (demoLinkElement && demoLinkElement.href) {
        modalDemo.href = demoLinkElement.href;
        modalDemo.target = '_blank';
        modalDemo.style.display = 'inline-block';
      } else {
        modalDemo.style.display = 'none';
      }
      if (sourceLink && sourceLink.href) {
        modalSource.href = sourceLink.href;
        modalSource.target = '_blank';
        modalSource.style.display = 'inline-block';
    } else {
      modalSource.style.display='none';
    }


      modal.style.display = 'flex';
    });
  });

  modalCloseBtn.addEventListener('click', () => {
    modal.style.display = 'none';
  });

  window.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.style.display = 'none';
    }
  });
});


