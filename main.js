/**
 * Main JavaScript for PromoProducts Presentation Tool
 */

document.addEventListener('DOMContentLoaded', function() {
    // Enable tooltips everywhere
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Enable popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Category filter functionality (for product selection page)
    const categoryFilters = document.querySelectorAll('.category-filter');
    if (categoryFilters.length > 0) {
        categoryFilters.forEach(filter => {
            filter.addEventListener('change', function() {
                filterProducts();
            });
        });
    }

    // Function to filter products based on selected categories
    function filterProducts() {
        const selectedCategories = [];
        document.querySelectorAll('.category-filter:checked').forEach(checkbox => {
            selectedCategories.push(checkbox.value);
        });

        // If no categories selected, show all
        if (selectedCategories.length === 0) {
            document.querySelectorAll('.product-category-section').forEach(section => {
                section.style.display = 'block';
            });
            return;
        }

        // Show only selected categories
        document.querySelectorAll('.product-category-section').forEach(section => {
            if (selectedCategories.includes(section.dataset.category)) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        });
    }

    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });

    // Add animation to cards when they enter viewport
    const animateOnScroll = function() {
        const elements = document.querySelectorAll('.animate-on-scroll');
        elements.forEach(element => {
            const position = element.getBoundingClientRect();
            // Check if element is in viewport
            if(position.top < window.innerHeight && position.bottom >= 0) {
                element.classList.add('fade-in');
            }
        });
    };

    // Run animation check on scroll
    window.addEventListener('scroll', animateOnScroll);
    // Initial check for elements in viewport
    animateOnScroll();
});
