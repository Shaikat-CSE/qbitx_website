/**
 * QBITX Solutions - Main JavaScript File
 * This file contains all the interactive functionality for the website
 */

(function() {
    'use strict';

    /**
     * Initialize when DOM is ready
     */
    document.addEventListener('DOMContentLoaded', function() {
        // Handle preloader
        handlePreloader();
        
        // Initialize header scroll effect
        initHeaderScroll();
        
        // Back to top button functionality
        initBackToTop();
        
        // Initialize newsletter form
        initNewsletterForm();
        
        // Initialize contact form
        initContactForm();
        
        // Initialize service request form
        initServiceRequestForm();
        
        // Add animation to counters
        initCounterAnimation();
    });

    /**
     * Handle the preloader
     */
    function handlePreloader() {
        const preloader = document.getElementById('preloader');
        if (preloader) {
            // Hide preloader after page is fully loaded
            window.addEventListener('load', function() {
                preloader.classList.add('loaded');
                
                // Remove from DOM after animation
                setTimeout(function() {
                    preloader.style.display = 'none';
                }, 500);
            });
        }
    }

    /**
     * Initialize header scroll effect
     */
    function initHeaderScroll() {
        const header = document.querySelector('.header');
        
        if (header) {
            window.addEventListener('scroll', function() {
                if (window.scrollY > 50) {
                    header.classList.add('scrolled');
                } else {
                    header.classList.remove('scrolled');
                }
            });
            
            // Trigger scroll event on load
            window.dispatchEvent(new Event('scroll'));
        }
    }

    /**
     * Initialize back to top button
     */
    function initBackToTop() {
        const backToTopBtn = document.getElementById('backToTop');
        
        if (backToTopBtn) {
            window.addEventListener('scroll', function() {
                if (window.scrollY > 300) {
                    backToTopBtn.classList.add('show');
                } else {
                    backToTopBtn.classList.remove('show');
                }
            });
            
            backToTopBtn.addEventListener('click', function(e) {
                e.preventDefault();
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        }
    }

    /**
     * Initialize newsletter form with AJAX submission
     */
    function initNewsletterForm() {
        const newsletterForms = document.querySelectorAll('.newsletter-form');
        
        if (newsletterForms.length > 0) {
            newsletterForms.forEach(function(form) {
                form.addEventListener('submit', function(e) {
                    e.preventDefault();
                    
                    const formData = new FormData(form);
                    const submitBtn = form.querySelector('button[type="submit"]');
                    const originalBtnText = submitBtn.innerHTML;
                    
                    // Disable submit button and show loading state
                    submitBtn.disabled = true;
                    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Subscribing...';
                    
                    // Send AJAX request
                    fetch(form.action, {
                        method: 'POST',
                        body: formData,
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    })
                    .then(response => response.json())
                    .then(data => {
                        // Re-enable submit button
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = originalBtnText;
                        
                        if (data.status === 'success') {
                            // Success message
                            showToast(data.message, 'success');
                            form.reset();
                        } else if (data.status === 'info') {
                            // Info message
                            showToast(data.message, 'info');
                        } else if (data.status === 'error') {
                            // Error message
                            showToast(data.errors.email || 'An error occurred. Please try again.', 'error');
                        }
                    })
                    .catch(error => {
                        console.error('Error:', error);
                        submitBtn.disabled = false;
                        submitBtn.innerHTML = originalBtnText;
                        showToast('An error occurred. Please try again.', 'error');
                    });
                });
            });
        }
    }

    /**
     * Initialize contact form with AJAX submission
     */
    function initContactForm() {
        const contactForm = document.querySelector('.contact-form');
        
        if (contactForm) {
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const formData = new FormData(contactForm);
                const submitBtn = contactForm.querySelector('button[type="submit"]');
                const originalBtnText = submitBtn.innerHTML;
                
                // Clear previous error messages
                clearFormErrors(contactForm);
                
                // Disable submit button and show loading state
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Sending...';
                
                // Send AJAX request
                fetch(contactForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    // Re-enable submit button
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                    
                    if (data.status === 'success') {
                        // Success message
                        showToast(data.message, 'success');
                        contactForm.reset();
                    } else if (data.status === 'error') {
                        // Show validation errors
                        for (const field in data.errors) {
                            const inputElement = contactForm.querySelector(`[name="${field}"]`);
                            if (inputElement) {
                                inputElement.classList.add('is-invalid');
                                
                                const feedbackElement = document.createElement('div');
                                feedbackElement.className = 'invalid-feedback';
                                feedbackElement.textContent = data.errors[field];
                                
                                inputElement.parentNode.appendChild(feedbackElement);
                            }
                        }
                        
                        showToast('Please correct the errors in the form.', 'error');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                    showToast('An error occurred. Please try again.', 'error');
                });
            });
        }
    }

    /**
     * Initialize service request form with AJAX submission
     */
    function initServiceRequestForm() {
        const serviceRequestForm = document.querySelector('.service-request-form');
        
        if (serviceRequestForm) {
            serviceRequestForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                const formData = new FormData(serviceRequestForm);
                const submitBtn = serviceRequestForm.querySelector('button[type="submit"]');
                const originalBtnText = submitBtn.innerHTML;
                
                // Clear previous error messages
                clearFormErrors(serviceRequestForm);
                
                // Disable submit button and show loading state
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Submitting...';
                
                // Send AJAX request
                fetch(serviceRequestForm.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest'
                    }
                })
                .then(response => response.json())
                .then(data => {
                    // Re-enable submit button
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                    
                    if (data.status === 'success') {
                        // Success message
                        showToast(data.message, 'success');
                        serviceRequestForm.reset();
                    } else if (data.status === 'error') {
                        // Show validation errors
                        for (const field in data.errors) {
                            const inputElement = serviceRequestForm.querySelector(`[name="${field}"]`);
                            if (inputElement) {
                                inputElement.classList.add('is-invalid');
                                
                                const feedbackElement = document.createElement('div');
                                feedbackElement.className = 'invalid-feedback';
                                feedbackElement.textContent = data.errors[field];
                                
                                inputElement.parentNode.appendChild(feedbackElement);
                            }
                        }
                        
                        showToast('Please correct the errors in the form.', 'error');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                    showToast('An error occurred. Please try again.', 'error');
                });
            });
        }
    }

    /**
     * Initialize counter animation
     */
    function initCounterAnimation() {
        const counterElements = document.querySelectorAll('.counter-value');
        
        if (counterElements.length > 0) {
            const options = {
                threshold: 0.5
            };
            
            const observer = new IntersectionObserver(function(entries) {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const target = entry.target;
                        const countTo = parseInt(target.getAttribute('data-count'));
                        
                        // Animate the counter
                        let current = 0;
                        const duration = 2000; // 2 seconds
                        const increment = countTo / (duration / 16); // 60fps
                        
                        const timer = setInterval(function() {
                            current += increment;
                            target.textContent = Math.floor(current);
                            
                            if (current >= countTo) {
                                target.textContent = countTo;
                                clearInterval(timer);
                            }
                        }, 16);
                        
                        // Unobserve after animation
                        observer.unobserve(target);
                    }
                });
            }, options);
            
            counterElements.forEach(element => {
                observer.observe(element);
            });
        }
    }

    /**
     * Clear all form error messages
     */
    function clearFormErrors(form) {
        const invalidInputs = form.querySelectorAll('.is-invalid');
        const errorMessages = form.querySelectorAll('.invalid-feedback');
        
        invalidInputs.forEach(input => {
            input.classList.remove('is-invalid');
        });
        
        errorMessages.forEach(message => {
            message.remove();
        });
    }

    /**
     * Show toast notification
     */
    function showToast(message, type = 'success') {
        // Create toast container if it doesn't exist
        let toastContainer = document.querySelector('.toast-container');
        
        if (!toastContainer) {
            toastContainer = document.createElement('div');
            toastContainer.className = 'toast-container position-fixed bottom-0 end-0 p-3';
            document.body.appendChild(toastContainer);
        }
        
        // Generate a unique ID for the toast
        const toastId = 'toast-' + Date.now();
        
        // Set the appropriate background color based on type
        let bgClass = 'bg-success';
        if (type === 'error') bgClass = 'bg-danger';
        if (type === 'info') bgClass = 'bg-info';
        if (type === 'warning') bgClass = 'bg-warning';
        
        // Create the toast element
        const toastHtml = `
            <div id="${toastId}" class="toast align-items-center ${bgClass} text-white border-0" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="d-flex">
                    <div class="toast-body">
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
            </div>
        `;
        
        // Add the toast to the container
        toastContainer.insertAdjacentHTML('beforeend', toastHtml);
        
        // Initialize and show the toast
        const toastElement = document.getElementById(toastId);
        const toast = new bootstrap.Toast(toastElement, {
            autohide: true,
            delay: 5000
        });
        
        toast.show();
        
        // Remove toast from DOM after it's hidden
        toastElement.addEventListener('hidden.bs.toast', function() {
            toastElement.remove();
        });
    }

})(); 