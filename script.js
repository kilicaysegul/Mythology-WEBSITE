document.addEventListener('DOMContentLoaded', function() {
    // --- BİLGİLER ---
    const facts = [
        "Zeus is the king of the gods in Greek mythology.",
        "Hercules was born as a demi-god, the son of Zeus and Alcmene.",
        "The Minotaur was a creature with the body of a man and the head of a bull.",
        "The Trojan War lasted for ten years.",
        "Athena is the goddess of wisdom and war.",
        "Medusa was one of the three Gorgons, whose gaze turned people to stone."
    ];

    let currentFact = 0;

    function changeText() {
        const factElement = document.getElementById('fact');
        if (factElement) {
            factElement.textContent = facts[currentFact];
            currentFact = (currentFact + 1) % facts.length;
        }
    }

    changeText();
    setInterval(changeText, 3000);

    // --- SLIDER ---
    const slides = document.querySelectorAll(".slide");
    const nextBtn = document.querySelector(".next");
    const prevBtn = document.querySelector(".prev");
    let currentIndex = 0;
    let slideInterval;

    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove("active"));
        slides[index].classList.add("active");
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }

    if (nextBtn && prevBtn) {
        nextBtn.addEventListener("click", () => {
            nextSlide();
            resetInterval();
        });

        prevBtn.addEventListener("click", () => {
            prevSlide();
            resetInterval();
        });
    }

    function startInterval() {
        slideInterval = setInterval(nextSlide, 3000);
    }

    function resetInterval() {
        clearInterval(slideInterval);
        startInterval();
    }

    showSlide(currentIndex);
    startInterval();
});
























