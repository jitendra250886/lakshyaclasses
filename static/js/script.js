// static/js/script.js

document.addEventListener("DOMContentLoaded", () => {
    console.log("LakshyaClasses frontend loaded.");

    // Highlight active nav link
    const currentPath = window.location.pathname;
    document.querySelectorAll(".navbar-nav .nav-link").forEach(link => {
        if (link.getAttribute("href") === currentPath) {
            link.classList.add("active");
        }
    });

    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll(".alert");
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.classList.add("fade");
            alert.classList.remove("show");
        }, 5000);
    });
});
