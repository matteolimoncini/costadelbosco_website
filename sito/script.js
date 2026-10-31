// Costa del Bosco — piccole interazioni, il sito funziona anche senza JavaScript

// Menu mobile
const toggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("nav");

toggle.addEventListener("click", () => {
  const open = toggle.getAttribute("aria-expanded") === "true";
  toggle.setAttribute("aria-expanded", String(!open));
  toggle.setAttribute("aria-label", open ? "Apri il menu" : "Chiudi il menu");
  nav.classList.toggle("open", !open);
});

nav.querySelectorAll("a").forEach((link) =>
  link.addEventListener("click", () => {
    toggle.setAttribute("aria-expanded", "false");
    toggle.setAttribute("aria-label", "Apri il menu");
    nav.classList.remove("open");
  })
);

// Bordo dell'header dopo lo scroll
const header = document.querySelector(".site-header");
const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 8);
window.addEventListener("scroll", onScroll, { passive: true });
onScroll();

// Comparsa delle sezioni
const revealables = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -40px 0px" }
  );
  revealables.forEach((el) => observer.observe(el));
} else {
  revealables.forEach((el) => el.classList.add("visible"));
}

// Anno nel footer
document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));
