document.querySelectorAll('[data-toggle]').forEach((button) => {
  button.addEventListener('click', () => {
    const item = button.closest('[data-faq]');
    const expanded = item.classList.toggle('active');
    button.textContent = expanded ? '–' : '+';
  });
});
